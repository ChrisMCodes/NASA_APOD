#!/usr/bin/env
# Queries astronomy picture of the day from NASA
# You'll need an API Key from https://api.nasa.gov
# Use 'pip install requests pprint urllib3' prior to use

# Imports appropriate modules
import datetime
import requests
import webbrowser as wb
from urllib.request import urlretrieve
from pprint import PrettyPrinter


# A couple variables
pp = PrettyPrinter()
api_key = "DEMO_KEY" # Key is a string. You can get an api key at https://api.nasa.gov/

def get_date():
    ''' Queries for date of APOD '''
    print("If you would like to see today's Astronomy photo of the day, press enter.")
    print("Otherwise, enter the date that you would like to query.")
    print("Use only yyyy-mm-dd format\n")
    try: # Handles errors
        change_date = input()
    except Exception:
        print("Sorry, the date you entered was not recognized. Your date has been initialized to {}.".format(datetime.date.today()))
        change_date = datetime.date.today()
    if change_date == '':
        return datetime.date.today()
    else:
        return change_date

def get_apod(date, pp, api_key):
    ''' Queries the Astronomy Picture of the Day from NASA '''
    URL = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': api_key, 'date': date, 'hd': True} # These params are defined by the API
    response = requests.get(URL, params=params).json()
    pp.pprint(response)
    return response

# Main method of program

# Saves user-inputted date to query_date
query_date = get_date()

# Saves JSON data to new_response and handles exceptions (probably created by incorrect date formatting)
try:
    new_response = get_apod(query_date, pp, api_key)
except Exception:
    print("Something went wrong. Did you format your date yyyy-mm-dd? Please restart the program and try again.")
    exit()

# Queries HD URL for APOD from JSON data and saves it to hd_url
hd_url = new_response['hdurl']

# Opens HD URL in default web browser (new tab)
wb.open(hd_url, new=2) 
