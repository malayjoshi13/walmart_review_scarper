# walmart_review_scraper

# About
Its a Python and Selenium based scraper to scrape product reviews from a Walmart product link:- https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365

# Steps involved in implementation of scraper
1) Installed selenium library with other required libraries using ```pip```.
2) Installed chrome driver.
3) Imported required libraries like ```selenium```, ```pandas``` and ```time``` in ```scraper.py``` Python script. 
4) Redirected to target URL.
5) Then scrolled down to bottom of page to activate ```See all reviews``` button.
6) Extracted location of ```See all reviews``` button and clicked it by help of Selenium's function of ```.click()```.
7) Selected ```newest to oldest``` option from ```Sort``` drop-down to get reviews in order of most recent to the oldest one.
8) Calling ```scrape_details``` function. This function scrape details like only for dates after January 2021. When review-date reach December 2020 then this function is stopped from further scrapping.
9) After this, all the scraped data is saved to ```output.csv``` file by help of ```savedata_closebrowser``` function.

# Input
![bandicam 2021-12-26 18-39-34-684](https://user-images.githubusercontent.com/71775151/147409161-d2de7b65-0931-4c80-b2d8-cdc874ebf512.jpg)

# Output
![bandicam 2021-12-26 18-41-27-878](https://user-images.githubusercontent.com/71775151/147409165-6d466b96-88ad-4689-92a9-146849836f88.jpg)
