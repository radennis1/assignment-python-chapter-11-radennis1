import requests
"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"

# Ryan Dennis
# Create response variable for API call
response = requests.get(url)

# Convert the json object to a dictionary
data = response.json()

# Return the value of the dictionary with key "Global"
global_stats = data['Global']

# Return the value of the dictionary with key "TotalDeaths"
deaths = global_stats['TotalDeaths']

# Return the value of the dictionary with key "TotalConfirmed"
cases = global_stats['TotalConfirmed']

# Calculate Mortality Rate
mortality_rate = deaths / cases

# Print Output
print(
    f"Total Deaths: {deaths:,} \nTotal Confirmed Cases: {cases:,} \nMortality Rate: {mortality_rate:.3f}")
