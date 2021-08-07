# Chatham County Assessor Database Scraping

This is a Python script that scrapes assessed, appraised, and tax values on the [Chatham County Assessor Database](https://www.chathamtax.org/PT/search/commonsearch.aspx?mode=realprop) on the parcel ID level.



## Description

  In order to automate the process of data collection for civic data analysis, we've created a Python script that utilizes [Selenium](https://www.selenium.dev/selenium/docs/api/py/api.html) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape the Chatham County Assessor Database. Selenium is a framework often used to test web applications, as it can automate webpage interactions. With Selenium, we're able to create functions that can automatically navigate (clicking) through the assessor database in order to find pages that fit our data needs. Selenium uses a chromedriver through Google Chrome for the process of webpage automation. To scrape information on the webpage, we used BeautifulSoup, a Python library that is used to parse HTML and XML documents. In our case, we created functions with BeautifulSoup so that we could parse HTML content on the assessor database to get specific data we needed. Finally, with the use of [pandas](https://pandas.pydata.org/docs/), a Python library used for data manipulation and analysis, we converted the data into individual dataframes that could be saved as csv files.



## Dependencies

- The main program being run, "**scrape_chatham.py**", uses three other sets of helper functions: "**selenium_helpers.py**", "**bs4_helpers.py**", and "**parid_helpers.py**"
- Code has been tested using **Selenium 4.0. 0 Alpha 5**, **Beautifulsoup v4.9.3**, and **pandas v1.3.1**
- Chromedriver has been tested with Google Chrome version 92 and 93



## Set Up

### Installing Python

- If you do not have a version of Python3 installed, download can be found [here](https://www.python.org/downloads/release/python-396/)
- **Windows users**:
  - Download the version according to your system type (whether it's 64-bit or 32-bit)
  - This information can be found by going Settings, System, and then About
- **Mac users**: download “macOS 64-bit Intel installer” (make sure you’re running on macOS 10.9 and later)
- When you begin installing Python, on the opening screen, make sure to check off “**Add Python 3.9 to PATH**”. Then go ahead and install.
- You can check to make sure you have Python with the correct version by going to your command prompt/terminal and doing the following command:
```
python --verson
```


### Installing libraries

- From your command prompt/terminal, change the directory so that it is pointing to the scrape_tutorial folder
  - To change directory, type "cd" followed by the path that leads to the folder. For example:
  ```
  C:\Users\name>cd smart_cities_savannah\scrape_tutorial
  ```
- After changing directories, perform the following command:
```
pip install -r requirements.txt
```


### Google Chrome and Chromedriver

- Make sure you have Google Chrome in your system
- Chromedriver download can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Download the version associated with the version of Chrome you’re using
  - To find which version you’re using, go to to the three dots at the top right corner of the Chrome browser, go to “**Help**” then “**About Google Chrome**”
- After downloading, extract the chomedriver
- For **Windows users**: After extracting the chromdriver, move the "chromedriver.exe" file into the scrape_tutorial folder
- For **Mac users**:
  - Open Finder, click “⌘” + “Shift” + “G” and search for “/usr/local/”
  - Check if there is a “bin” folder. If not, create one
  - Move the “chromedriver.exe” file to the “/usr/local/bin” folder




## Editing the code for Windows users

- Open "**selenium_helpers.py**" and uncomment the following block
```
directory = 'chromedriver.exe'
driver = webdriver.Chrome(directory)
```
- To uncomment code, simply delete the quotation marks that surround the block of code
- Open "**bs4_helpers.py**" and uncomment the following block
```
tax_directory = 'tax\\'
assessed_directory = 'assessed_values\\'
appraised_directory = 'appraised_values\\'
```




## Editing the code for Mac users

- Open "**selenium_helpers.py**" and uncomment the following block
```
driver = webdriver.Chrome()
```
- To uncomment code, simply delete the quotation marks that surround the block of code
- Open "**bs4_helpers.py**" and uncomment the following block
```
tax_directory = 'tax/'
assessed_directory = 'assessed_values/'
appraised_directory = 'appraised_values/'
```




## Executing script

All the necessary tools should now be downloaded. Run “**python scrape_chatham.py**” on your command prompt/terminal under the scrape_tutorial directory. For example:
```
C:\Users\name\smart_cities_savannah\scrape_tutorial> python scrape_chatham.py
```
Once you confirm that it works for those 5 entries and want to run it on the rest of the parcel ID's, go to **parid_helpers.py** and replace ‘**test.txt**’ with ‘**parcel_ids.txt**”. The script should now run for the rest of the parcel ID’s.
