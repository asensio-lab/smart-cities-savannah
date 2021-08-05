# Chatham County Assessor Database Scraping

## Description

## Set Up

### Installing Python

- If you do not have a verion of Python3 installed, download can be found [here](https://www.python.org/downloads/release/python-396/)
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
  C:\Users\edwardchen>cd smart_cities_savannah\scrape_tutorial
  ```
- After changing directories, perform the following command:
```
pip install -r requirements.txt
```


### Google Chrome and Chromedriver

- Make sure you have Google Chrome in your system
- ChromeDriver download can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Download the version associated with the version of Chrome you’re using
  - To find which version you’re using, go to to the three dots at the top right corner of the Chrome browser, go to “**Help**” then “**About Google Chrome**”
- After downloading, extract the chomedriver and move it into the scrape_tutorial folder


## Executing script

All the necessary tools should now be downloaded. Run “**python scrape_chatham.py**” on your command prompt/terminal under the scrape_tutorial directory. For example:
```
C:\Users\edwardchen\smart_cities_savannah\scrape_tutorial> python scrape_tutorial.py
```
Once you confirm that it works for those 5 entries go to parid_helpers.py and replace ‘test.txt’ with ‘parcel_ids.txt”. The script should now run for the rest of the parcel ID’s.

