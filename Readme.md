# Lottery Data Scraper

This Python application scrapes data from the California Lottery archive website and extracts the winning numbers for the desired lottery game within a specified date range. This app utilizes Selenium for dynamic web scraping and BeautifulSoup for parsing HTML content. 


## Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

Update path to chromedriver in `main.py`
 
## Usage
To scrape the winning Powerball numbers for a specific duration (in months), you can use the following command:
```python
python src/main.py --type powerball --months <number_of_months>
```
Alternatively, you can specify the duration in years using the --years option:
```python
python src/main.py --type powerball --years <number_of_years>
```
#### Help
To view the available options and usage information, you can use the --help option:
```python
python src/main.py --help
```


## Additional 
Run the following script to combine the monthly json files into 1 dataset for analysis. 
```python
python src/combine_json.py
```