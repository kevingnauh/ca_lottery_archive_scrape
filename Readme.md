# Lottery Data Scraper

This Python application scrapes data from the California Lottery archive website and extracts the winning numbers for the Mega Millions game within a specified date range. The archive only displays data in 30 day increments. This app utilizes the Selenium web driver for dynamic web scraping and BeautifulSoup for parsing HTML content. The application allows users to specify the start and end dates for data extraction, and saves the results in JSON format.


## Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

```python
python src/main.py
```

## Inputs
In 'main.py', make the following selections:
1. Lotto type: 
- Powerball  
- Powerball Double Play  
- MEGA Millions  
- SuperLotto Pl  
- Fantasy 5  
- Daily Derby  
- Daily 4  
- Daily 3 Midday  
- Daily 3 Evening  
2. Date range:  
- Start and end date
  * Can be datetime object or the following date format: 'MM/DD/YYYY'
3. Chromedriver
- Update path to chromedriver

## Additional 
Run the following script to combine the monthly json files. 
```python
python src/combine_json.py
```
