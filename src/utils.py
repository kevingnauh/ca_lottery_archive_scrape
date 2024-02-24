import time
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Automate form selection and scrape historical lotto results.')

    parser.add_argument('--type', dest='lotto_type', required=True, choices=['all', 'powerball', 'powerball_double_play', 'mega_millions','superlotto_plus','fantasy5','daily_derby','daily4','daily3_midday','daily3_evening'],
                        help='Specify the type of lotto.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--months', dest='months', type=int,
                        help='Specify the number of months for the date range.')
    group.add_argument('--years', dest='years', type=int,
                        help='Specify the number of years for the date range.')

    args = parser.parse_args()
    return args

# generate a random number to use as wait time for selenium actions
def generate_random_number():
    """
        Returns a number in range 0.001 to 0.0015. 
        Uses current time as seed.
    """
    seed = int(str(time.time()).replace('.', ''))
    random_number = (seed % 500) / 1000000  
    if random_number < 0.001:
        random_number += 0.001
    return round(random_number, 4) 


def select_forms(selection):
    all_forms = {
        'all': 'ALL', 
        'powerball': '101',               # 7
        'powerball_double_play': '101D',  # 6
        'mega_millions': '113',           # 6
        'superlotto_plus': 'CA1',         # 6
        'fantasy5': 'CA2',                # 5
        'daily_derby': 'CA3',             # 4
        'daily4': 'CAB',                  # 4
        'daily3_midday': 'CAC',           # 3 
        'daily3_evening': 'CAA'           # 3
    }
    
    return all_forms[selection]