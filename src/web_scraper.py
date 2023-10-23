import os
import json
from bs4 import BeautifulSoup


def create_folder_path(filename, output_folder_name="output"):
    """create output folder in current directory and returns full path"""
    subfolder = output_folder_name
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    filepath = os.path.join(subfolder, filename)

    return filepath

def extract_and_save_data(soup, filename):
    """Extract data table from results page"""

    filepath = create_folder_path(filename)

    # Extract and save contents
    data = []
    div_element = soup.find('div', class_='datagrid')
    if div_element:
        table = div_element.find('table')
        if table:
            rows = table.find_all('tr')
            for row in rows[2:]:
                columns = row.find_all('td')
                if len(columns) == 2:
                    date = columns[0].text.strip()
                    numbers = columns[1].text.strip().split('-')
                    data.append({
                        'date': date,
                        'numbers': numbers
                    })
            with open(filepath, 'w') as outfile:
                json.dump(data, outfile, indent=4)
                print(f"Successfully saved file {filename} to {os.getcwd()}")
        else:
            print("Table not found on the page.")
    else:
        print("Div element with class 'datagrid' not found on page.")



