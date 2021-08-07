# importing libraries
import selenium
from selenium import webdriver as wb
import pandas as pd
import time


# this function scrape details like review date, reviewer name, review title, review description and rating 
def scrape_details():
    # initialisng list to save scraped data
    alldetails=[]
    
    while True:
        # variable that will help us to stop execution
        time_to_break_out_of_a = False
        
        # from the "see all reviews" page get location of all review boxes/cards
        boxes = wbD.find_elements_by_class_name("Grid.ReviewList-content")

        # one-by-one enumerating to all review boxes
        for i in range(len(boxes)):
            
            # extracting date from first review box
            date=boxes[i].find_element_by_class_name('review-date-submissionTime').text
            # splitting the data into format ["July", "29,", "2020"]
            date_split = date.split(" ")
            # checking if the date of review is not of before January 2021
            # if review date starts from January 2021, then execute following code
            if date_split[0]!="December" and date_split[2]!="2020":
                # stores review date
                review_date = date
                
                # stores reviewer name
                reviewer_name = boxes[i].find_element_by_class_name('review-footer-userNickname').text
                
                # stores review title
                try:
                    review_title = boxes[i].find_element_by_class_name('review-title.font-bold').text
                except:
                    review_title = "Null"

                # stores review description
                review_description = boxes[i].find_element_by_class_name('review-text')
                review_description_text = review_description.find_element_by_tag_name('p').text

                # stores rating given by user
                rating = boxes[i].find_element_by_class_name('visuallyhidden.seo-avg-rating').text

                # stores scraped information in a dictionary as a key-value pair
                temp ={
                'Review_date':review_date,
                'Reviewer_name':reviewer_name,
                'Review_title':review_title,
                'Review_description':review_description_text,
                'Rating':rating}   

                # append dictionary corresponding to each review box in "alldetails" list
                alldetails.append(temp)

            # if review date is of before January 2021, then execute following code
            elif date_split[0]=="December" and date_split[2]=="2020":  
                # set the variable as "True"
                time_to_break_out_of_a = True
                # exit the for loop
                break

        # after exiting "for" loop, break from "while" loop as well if "time_to_break_out_of_a" variable is set "True"
        # which is indication of the fact that December 2020 is reached
        if time_to_break_out_of_a:
            break
        else:
            # if date of review is of after December 2020 then keep moving to next page
            time.sleep(12)
            wbD.find_element_by_class_name("paginator-btn.paginator-btn-next").click()
            
    return alldetails


# this function saves the scraped data in output.csv file and close the browser
def savedata_closebrowser(alldetails): 
    # convert the entries in "alldetails" list into dataframe format
    data = pd.DataFrame(alldetails)
    # saving this data in csv format in output.csv file
    data.to_csv('output.csv',index=False)
    # closing the broswer through which selenium is scraping data
    wbD.close()
    # returning back message of success
    text = "Web browser closed...Scraping process is completed...Scraped data saved to 'output.csv'"
    return text




# driver code

wbD = wb.Chrome('chromedriver.exe')
# redirect to target url
wbD.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')
# a pause of 6sec to prevent server blocking
time.sleep(6)

# scrolling to bottom of page as "see all reviews" button present at bottom get activate when scrolled through them
wbD.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# a pause of 6sec to prevent server blocking
time.sleep(6)

# getting location of "see all reviews" button
see_all_reviews_button_location = wbD.find_element_by_class_name('button.ReviewBtn-container.ReviewsHeaderWYR-seeAll.button--primary')
# getting link attached to "see all reviews" button
see_all_reviews_button_link = see_all_reviews_button_location.get_attribute('href')
# redirecting to the link obtained from "see all reviews" button
wbD.get(see_all_reviews_button_link)
# a pause of 6sec to prevent server blocking
time.sleep(6)

# selecting "newest to oldest" option from sort by drop-down
wbD.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/select").send_keys("newest to oldest")

# calling function to scrape required details 
alldetails = scrape_details()

# calling function to save the scraped data in output.csv file, close the broswer and 
# displaying message after successful execution 
message = savedata_closebrowser(alldetails)
print(message)