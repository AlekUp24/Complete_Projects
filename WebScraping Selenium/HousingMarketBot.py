import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
zapisuj do db wszystkie dane (moze wiecej kolumn)
nie nadpisuj istniejacych id i tworz dobry set danych
"""

# set vars
sciezkaSelen = "C:/SeleniumDrivers/chromedriver.exe"
webURL = "https://otodom.pl" 
teraz = str(datetime.datetime.now())

city =  "Warszawa"
max_price = 800000
min_price = 450000
max_space = 80
min_space = 40

# set driver
driver = webdriver.Chrome(sciezkaSelen)
driver.get(webURL)

# results table
finalTable = pd.DataFrame({ 'ID':[],
                            'Posting Date':[],
                            'Space':[],
                            'Price':[],
                            'Location':[],
                            'URL':[]})


# accept cookies window
try:
    acceptCookies = driver.find_element_by_id("onetrust-accept-btn-handler")
    if acceptCookies.is_displayed():
        print("Cookies Accepted!")
        acceptCookies.click()
except:
    print("No Cookies to accept!")


# locate sales tab to continue
sales_tab = driver.find_element_by_id("sell")
if sales_tab.is_displayed():
    print("Sales tab found!")
else:
    print("Sales tab not found!")
    exit()

# select city 
popular_city = driver.find_element_by_id(f"sellPopularLocation{city}")
sales_tab.click()
popular_city.click()

# get parameters boxes
max_price_input_box = driver.find_element_by_id("priceMax")
min_price_input_box = driver.find_element_by_id("priceMin")
max_area_input_box = driver.find_element_by_id("areaMax")
min_area_input_box = driver.find_element_by_id("areaMin")

# input search criteria
max_price_input_box.send_keys(max_price)
min_price_input_box.send_keys(min_price)
max_area_input_box.send_keys(max_space)
min_area_input_box.send_keys(min_space)

searchButton = driver.find_element_by_id("search-form-submit")
searchButton.click()

try:
    sort_asc_button = driver.find_element(By.XPATH, "//button[@value='PRICE-ASC'][@role='radio']")
    sort_asc_button.click()
except:
    print("No sort button found")

try:
    listings = driver.find_elements(By.XPATH, "//div[@name='search.listing.organic']")
    print(listings)
except:
    print("no listings found")
