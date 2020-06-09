READ ME
NASA_APOD apod.py

Last update by creator: 2020-06-09

Purpose: This program queries and prints the NASA Astronomy Photo of the Day (APOD) JSON results including the HD URL 
         to the console. It then opens the HD URL in a new browser tab.

Required: Python 3, pip (for requests, pprint, urllib3), a NASA API Key (free and easy to obtain at https://api.nasa.gov)

Pitfalls: I created this for my own use, so there isn't much exception handling on the date. Dates must be formatted
          as YYYY-MM-DD to function; otherwise the program will simply exit. API Key must come from api.nasa.gov

FUNCTIONS:
         get_date: Gets the date the user wants to query. Date must be entered as YYYY-MM-DD, otherwise the program will just exit.
         get_API_Key: Queries your API Key. (free and easy to obtain at https://api.nasa.gov)
         get_apod: Parameters include date, pp, api_key. Queries the Astronomy Picture of the Day from NASA and returns JSON results.

Licensing: This program is absolutely free to use, distribute, branch, copy, and modify. If it gets used in an app, let me know
           so that I can admire your work.
