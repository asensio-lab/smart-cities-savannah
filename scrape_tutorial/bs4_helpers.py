from bs4 import BeautifulSoup
import pandas as pd

# These functions allow us to extract the html content of the webpage using BeautifulSoup, 
# and save the desired info as a CSV file into its respective folder


# Uncomment this section for Windows users
'''
tax_directory = 'tax\\'
assessed_directory = 'assessed_values\\'
appraised_directory = 'appraised_values\\'
sales_directory = 'sales\\'
'''


# Uncomment this section for Mac Users
'''
tax_directory = 'tax/'
assessed_directory = 'assessed_values/'
appraised_directory = 'appraised_values/'
sales_directory = 'sales/'
'''

# Extract information formatted as a table
def extract_table(table):
    trs = table.find_all('tr')
    values = []
    for tr in trs:
        tds = tr.find_all('td')
        tds = [x.text for x in tds]
        if len(tds) < 2:
            continue
        values.append(tds)
    return values


# Scrape appraised values and save them as a CSV
def extract_appraised(parid, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    appraised_values_table = soup.find(id='Appraised Values')
    appraised_values = extract_table(appraised_values_table)    
    df = pd.DataFrame(appraised_values[1:], columns = appraised_values[0])
    df.to_csv('%s%s.csv'%(appraised_directory, parid))
                
              
# Scrape assessed values and save them as a CSV
def extract_assessed(parid, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    assessed_values_table = soup.find(id='Assessed Values')
    assessed_values = extract_table(assessed_values_table)   
    df = pd.DataFrame(assessed_values[1:], columns = assessed_values[0])
    df.to_csv('%s%s.csv'%(assessed_directory, parid))
                      

# Scrape tax values and save them as a CSV
def extract_tax(parid, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    tax_table = soup.find(id='Tax (Penalties and Interest Included through Current Date)')
    tax_values = extract_table(tax_table)      
    df = pd.DataFrame(tax_values[1:], columns = tax_values[0])
    df.to_csv('%s%s.csv'%(tax_directory, parid))
    
    
# Scrape sales history and save as a CSV
def extract_sales(parid, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    sales_table = soup.find(id='Sales')
    sales_values = extract_table(sales_table)
    df = pd.DataFrame(sales_values[1:], columns = sales_values[0])
    df.to_csv('%s%s.csv'%(sales_directory, parid))
