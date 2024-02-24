"""
Description:
    To automate form selection and scrape historical lotto results. 

Author: Kevin H

Contents:
    - Uses selenium to automate accessing the webpage and form selections.
    - Extracts data from results page and saves to json file.
    - Repeats process for each month specified in the date range inputs. 

Usage:
    $ python main.py

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from web_scraper import extract_and_save_data , BeautifulSoup
from utils import generate_random_number, time, select_forms, parse_arguments

# Inputs
## Path to chromedriver
path_to_chromedriver = "D:/Users/Documents/chromdriver/chromedriver-win64/chromedriver-win64/chromedriver.exe"

args = parse_arguments()

## Select date range: datetime object or 'MM/DD/YYYY' 
if args.months:
    start_date = datetime.now() - relativedelta(months=args.months)
elif args.years:
    start_date = datetime.now() - relativedelta(years=args.years)
end_date = datetime.now()  

## Select lotto type
lotto_type = args.lotto_type

## Webpage url
page_url = "https://www.lottostrategies.com/cgi-bin/winning_select_state/205/CA/california-lottery-numbers-archive.html"

# Formatting Inputs
output_filename = lotto_type.lower().replace(' ','_')  # i.e. 'mega_millions_MM_YYYY.json'
lotto_form_code = select_forms(lotto_type)

selection_date = datetime.strptime(start_date, '%m/%d/%Y') if not isinstance(start_date, datetime) else start_date
end_date = datetime.strptime(end_date, '%m/%d/%Y') if not isinstance(end_date, datetime) else end_date

# chromedriver settings
service = Service(path_to_chromedriver) 
service.start()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5)

# Run all steps
while selection_date <= end_date:
    filename = f"{output_filename}_{selection_date.strftime('%Y_%m')}.json"
    driver.get(page_url)

    # find form elements
    # mega millions is 113
    driver.find_element(By.CSS_SELECTOR, f'form[name="FORM2"] input[value="{lotto_form_code}"]').click()

    month_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'form[name="FORM2"] select[name="em"]'))
    year_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'form[name="FORM2"] select[name="ey"]'))

    # make date range selections
    month_dropdown.select_by_value(str(selection_date.month))
    year_dropdown.select_by_value(str(selection_date.year))
    time.sleep(generate_random_number())

    # submit form
    driver.find_element(By.CSS_SELECTOR, 'form[name="FORM2"] input[type="SUBMIT"]').click()

    # wait for next page to load and save data table contents
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'datagrid')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    extract_and_save_data(soup, filename)

    # increment time
    selection_date = selection_date + relativedelta(months=1)

driver.quit()
print("Process Finished!")
