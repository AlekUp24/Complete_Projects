import datetime
import pandas as pd
from selenium import webdriver
from tkinter import filedialog
import tkinter

"""

zapisuj do db wszystkie dane (moze wiecej kolumn)
nie nadpisuj istniejacych id i tworz dobry set danych

"""


# set vars
sciezkaSelen = "C:/SeleniumDrivers/chromedriver.exe"
webURL = "https://otodom.pl" 
teraz = str(datetime.datetime.now())

city =  "Warszawa"
max_price = 500000
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


# locate search button
searchButton = driver.find_element_by_id("search-form-submit")
if searchButton.is_displayed():
    print("Search button found!")
    #newsList = newsTable.text
else:
    print("Search button not found!")
    exit()

