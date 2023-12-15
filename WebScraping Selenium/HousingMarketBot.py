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
sales_tab.click()
driver.find_element_by_id(f"sellPopularLocation{city}").click()

# get parameters boxes
driver.find_element_by_id("priceMax").send_keys(max_price)
driver.find_element_by_id("priceMin").send_keys(min_price)
driver.find_element_by_id("areaMax").send_keys(max_space)
driver.find_element_by_id("areaMin").send_keys(min_space)

driver.find_element_by_id("search-form-submit").searchButton.click()

# sort price ascending
try:
    sort_asc_button = driver.find_element(By.XPATH, "//button[@value='PRICE-ASC'][@role='radio']").click()
except:
    print("No sort button found")


# get offers (data)
composed = [] # list of all offers as nested lists 

try:
    listings = driver.find_elements(By.XPATH, "//li[@data-cy='listing-item']")
    for each in listings[:10]:  # get only first 10
        listURL = driver.find_element_by_link_text(each.text).get_attribute("href")
        listID = listURL[-5:]
        x = str(each.text).split(chr(10))
        for i in x[::-1]:
            if "DODANE" in str(i).upper() or "PODBITE" in str(i).upper():
                x.remove(i)
        x.insert(5,listURL)
        x[0] = listID
        composed.append(x[0:6]) 
except:
    print("no listings found")
    exit()

# prepare results table
finalTable = pd.DataFrame({ 'ID':[],
                            'Description':[],
                            'Address':[],
                            'Price':[],
                            'Offer from':[],
                            'URL':[]})

# put all data into dataframe
for each in composed:
    finalTable = finalTable.append({'ID':[each[0]],
                                    'Description':[each[1]],
                                    'Address':[each[2]],
                                    'Price':[each[3]],
                                    'Offer from':[each[4]],
                                    'URL':[each[5]]},
                                    ignore_index=True)
    
print(finalTable)