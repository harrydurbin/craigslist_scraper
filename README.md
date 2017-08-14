## Scrape ads from craigslist using Scrapy

To run:
1) cd to craigslist-scraper directory
2) $ pip install -r requirements.txt (in virtual env)
3) $ scrapy crawl bostongigs -a location="[SELECT A LOCATION]" -o [NAME FOR CSV FILE]

Where 'SELECT A LOCATION' is one of:   
 + gbs (for boston/camb/brook)   
 + bmw (for metro west)   
 + nos (for north shore)    
 + nwb (for northwest/merrimack)  
 + sob (for south shore)  

And 'NAME FOR CSV FILE' is one of: 
 + gbs.gigs.csv
 + bmw.gigs.csv
 + nos.gigs.csv
 + nwb.gigs.csv
 + sob.gigs.csv
