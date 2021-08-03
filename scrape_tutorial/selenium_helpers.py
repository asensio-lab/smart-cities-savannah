from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4_helpers

# These functions create a simulated version of Google Chrome that allow us to replicate a person searching and clicking a web page. This is necessary for us to be able to search for information on each unique parcel ID

directory = 'chromedriver.exe'
driver = webdriver.Chrome(directory)
driver.get('https://www.chathamtax.org/PT/search/commonsearch.aspx?mode=realprop')

# driver = webdriver.Chrome()
# driver.get('https://www.chathamtax.org/PT/search/commonsearch.aspx?mode=realprop')


# Enters a parcel ID and locate page with info to be scraped
def locate_page(parid):
    button = driver.find_element_by_id('btAgree')
    button.click()
    search = driver.find_element_by_id('inpParid')
    search.send_keys(parid)
    search.send_keys(Keys.RETURN)
    results = driver.find_element_by_class_name('SearchResults')
    results.click()
    
    
# Uses bs4 function to obtain tax info
def scrape_tax(parid):
    bs4_helpers.extract_tax(parid, driver.page_source)

    
# Uses bs4 function to obtain appraised info
def scrape_appraised(parid):
    value = driver.find_element_by_link_text('Value History')
    value.click()
    bs4_helpers.extract_appraised(parid, driver.page_source)

    
# Uses bs4 function to obtain assessed info 
def scrape_assessed(parid):
    bs4_helpers.extract_assessed(parid, driver.page_source)

    
# go back to original starting page
def walk_back():
    for _ in range(4):
        driver.back()
    
    
def scrape_chatham(parid):
    locate_page(parid)
    scrape_tax(parid)
    scrape_appraised(parid)
    scrape_assessed(parid)
    walk_back()