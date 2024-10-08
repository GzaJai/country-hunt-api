import json, random

with open('./countries.json', 'r') as file:
    countries =  json.load(file)

keys_list = list(countries.keys())

def get_country():
    '''Get a random country key'''
    random_int = random.randint(0, len(keys_list))
    return keys_list[random_int]


def get_countries_options():
    '''Returns a list of countries keys'''
    options = []
    
    while len(options) < 4:
        option = get_country()
        if option not in options:
            options.append(countries[option])

    return options

def get_key_by_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None

def get_response():
    options_list = get_countries_options()
    correct_aswer = options_list[0]

    random.shuffle(options_list)

    flag_url = f'https://flagpedia.net/data/flags/w580/{get_key_by_value(countries, correct_aswer)}.webp'

    response = {
        'variants': options_list,
        'correct_answer': correct_aswer,
        'flag': flag_url
    }

    return response