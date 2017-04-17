# simple-scraper for demonstrating purposes only

If running on Linux or MAC OS, call the script like this:

`python simple-scraper.py`

or if you want additional settings, do this:

`python simple-scraper.py --workers 12 --max 25 --sort likes --csv > data.csv`

this will tell the script to use 12 pool workers (run the script asincrouniously), show the top 25 results sorted by likes and export the data in csv file named data.csv


Sample result from the above command:

Total scraped entries: 140
-------------------------------------
 Views  +1  -1   |Speakers|                               Title

 65332 445  15 Jessica McKellar     (Hands-on intro to Python for beginning programmers)
 40962 403  14 David Beazley        (Discovering Python)
 26605 386  13 Ned Batchelder       (Getting Started Testing)
 50953 358  16 Richard Jones        (Introduction to game programming)
 18284 347  22 Julie Pagano         (It's Dangerous to Go Alone: Battling the Invisible Monsters in Tech)
 35544 310  20 Miguel Grinberg      (Flask by Example)
 34520 268   5 Alex Gaynor          (Fast Python, Slow Python)
 25781 247  12 Justin Abrahms       (Computer science fundamentals for self-taught programmers)
 30991 243  18 Guido Van Rossum     (Keynote - Guido Van Rossum)
 20665 223   3 Miguel Grinberg      (Writing RESTful web services with Flask)
 21820 214   5 Melanie Warrick      (How to Get Started with Machine Learning)
 39556 212   7 Kenneth Love         (Getting Started with Django, a crash course)
 13828 202  24 Kate Heddleston      (So you want to be a full-stack developer? How to build a full-stack python)
 26190 185   1 Katharine Jarmul     (Introduction to Web (and data!) Scraping with Python)
 13090 179   4 Brandon Rhodes       (All Your Ducks In A Row: Data Structures in the Standard Library and Beyond)
 23635 175  20 Jake Vanderplas      (Exploring Machine Learning with Scikit-learn)
 22729 174  16 David Beazley        (Generators: The Final Frontier)
 19299 171   8 Colton Myers         (Decorators: A Powerful Weapon in your Python Arsenal)
 11505 165   1 Brandon Rhodes       (The Day of the EXE Is Upon Us)
 31276 146   8 Michael Dehaan       (Ansible - Python-Powered Radically Simple IT Automation)
 17327 142  12 Julia Evans          (Diving into Open Data with IPython Notebook & Pandas)
 10338 113   5 Christophe Pettus    (PostgreSQL Proficiency for Python People)
 18780 106  23 Mike Bayer           (Introduction to SQLAlchemy)
 .......
