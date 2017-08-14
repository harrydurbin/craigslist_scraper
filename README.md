## Scrape ads from craigslist using Scrapy

To run:
1) cd to craigslist-scraper directory
2) $ pip install -r requirements.txt 
3) $ scrapy crawl bostongigs -a location="[SELECT A LOCATION]" -o [NAME FOR CSV FILE]

Where 'SELECT A LOCATION' is one of the following:
gbs (for boston/camb/brook)
bmw (for metro west)
nos (for north shore)
nwb (for northwest/merrimack)
sob (for south shore)

Where 'NAME FOR CSV FILE' is for example: gbs.gigs.csv.


