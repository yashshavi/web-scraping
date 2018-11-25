# web-scraping
multiple-site web crawler ,take input any site url and perform web page scraping , on using scrapy command to execute or start crawler the program first ask the user to enter the url of the site ,of which user want to scrap then the crawler will start crawling and perform web scraping ,the log file can be gernated by using command line argument LOG_FILE = 'name of file'.The setting for format is done in setting.py file uploded .
# folders and file containing
new.py : This file contain python code for the program.
setting.py : This file contain the setting for output format, here we want output in 'json' format hence the FEED_FORMAT and FEED_URI is                set according to requirment, and extension.feedexport.FeedExporter settings.
