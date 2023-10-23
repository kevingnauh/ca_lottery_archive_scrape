import time

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
        'All Games': 'ALL', 
        'Powerball': '101',               # 7
        'Powerball Double Play': '101D',  # 6
        'MEGA Millions': '113',           # 6
        'SuperLotto Plus': 'CA1',         # 6
        'Fantasy 5': 'CA2',               # 5
        'Daily Derby': 'CA3',             # 4
        'Daily 4': 'CAB',                 # 4
        'Daily 3 Midday': 'CAC',          # 3 
        'Daily 3 Evening': 'CAA'          # 3
    }
    
    return all_forms[selection]