"""To combine the monthly json files into 1 large file for use"""

import os
import json
from web_scraper import create_folder_path
import argparse

parser = argparse.ArgumentParser(description='Combine monthly json files to 1 master file')
parser.add_argument('--outname', dest='output_file_name', type=str,
                        help='Specify name for output file.')
args = parser.parse_args()

def combine_json_files(output_path):
    # define directory path
    directory = output_path

    all_data = []

    # iterate through each file in directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                all_data.extend(data)

    output_file = f"{args.output_file_name}.json" if args.output_file_name else 'combined_data.json'
    subfolder = "output/combined_data"
    filepath = create_folder_path(output_file, subfolder)

    with open(filepath, 'w') as f:
        json.dump(all_data, f, indent=4)


combine_json_files(r'output')