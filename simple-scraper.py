import argparse
import re
from multiprocessing.pool import ThreadPool as Pool
import requests
import bs4

root_url = 'http://pyvideo.org'
index_url = root_url + '/events/pycon-us-2014.html'


def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return [a.attrs.get('href') for a in soup.select("article > a[href^='/pycon']")]


def get_video_data(video_page_url):
    video_data = {}
    response = requests.get(root_url + video_page_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    video_data['title'] = soup.select(".entry-title")[0].get_text().replace("\n", "").strip()
    video_data['speakers'] = soup.select(".author a")[0].get_text()

    # initialize counters
    video_data['views'] = 0
    video_data['likes'] = 0
    video_data['dislikes'] = 0

    try:
        video_data['youtube_url'] = soup.select(".details-content li:nth-of-type(3) a")[0].get('href')
        response = requests.get(video_data['youtube_url'], headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'})
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        video_data['views'] = int(re.sub('[^0-9]', '', soup.select('.watch-view-count')[0].get_text().split()[0]))
        video_data['likes'] = int(re.sub('[^0-9]', '', soup.select('.like-button-renderer-like-button-unclicked > span')[0].get_text().split()[0]))
        video_data['dislikes'] = int(re.sub('[^0-9]', '', soup.select('like-button-renderer-dislike-button-unclicked > span')[0].get_text().split()[0]))
    except:
        # some or all of the counters could not be scraped
        pass
    return video_data


def parse_args():
    parser = argparse.ArgumentParser(description='Show PyCon 2014 video statistics.')
    parser.add_argument('--sort', metavar='FIELD', choices=['views', 'likes', 'dislikes'], default='views', help='sort by the specified field. Options are views, likes and dislikes.')
    parser.add_argument('--max', metavar='MAX', type=int, help='show the top MAX entries only.')
    parser.add_argument('--csv', action='store_true', default=False, help='output the data in CSV format.')
    parser.add_argument('--workers', type=int, default=8, help='number of workers to use, 8 by default.')
    return parser.parse_args()

def show_video_stats(options):
    pool = Pool(options.workers)
    video_page_urls = get_video_page_urls()
    results = sorted(pool.map(get_video_data, video_page_urls), key=lambda video: video[options.sort], reverse=True)
    
    print("Total scraped entries: " + str(len(results)))
    print("-------------------------------------")
    
    max = options.max
    if max is None or max > len(results):
        max = len(results)
    if options.csv:
        print(u'"title","speakers", "views","likes","dislikes"')
    else:
        print(u' Views  +1  -1   |Speakers|                               Title\n')
    for i in range(max):
        if options.csv:
            print(u'"{0}","{1}",{2},{3},{4}'.format(
                results[i]['title'], results[i]['speakers'], results[i]['views'],
                results[i]['likes'], results[i]['dislikes']))
        else:
            print(u'{0:6d} {1:3d} {2:3d} {3:20} ({4})'.format(
                results[i]['views'], results[i]['likes'], results[i]['dislikes'], results[i]['speakers'] ,results[i]['title']))

if __name__ == '__main__':
    show_video_stats(parse_args())