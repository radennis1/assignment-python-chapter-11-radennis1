import requests
import config
# Get data from Yelp using API calls
# Need to watch Mosh' video 10.4 AND 10.5 to understand this code.
# Dr. Humpherys added different ways to filter and loop through the data

url = "https://api.yelp.com/v3/businesses/search"
# Ryan Dennis


headers_dictionary = {
    "authorization": "bearer " + config.api_key
}
params_dictionary = {
    "term": "plumbing",
    "location": "amarillo, tx"
}
response = requests.get(url, headers=headers_dictionary,
                        params=params_dictionary)
# Convert the json object to a dictionary
result = response.json()

# return the value of the dictionary key "businesses"
businesses = result["businesses"]
print(type(businesses))
# Note. The businesses variable is a list containing dictionaries where
# each dictionary contains data regarding one business
# dictionary keys are case sensitive.
# business["name"] is not the same as business["Name"]
for business in businesses:
    print(business["name"], business["rating"], business["review_count"])

print("-" * 30)
# Use string interpolation to format the output
for business in businesses:
    # Must use single quotes inside the dictionary['key_name'] because
    # business['name'] is inside the double quotes of the string interpolation
    print(f"Name: {business['name']}. Avg Rating: {business['rating']}")

print("-" * 30)
print("---Businesses with reviews >= 4.5")
# Use list comprehension to filter the data using one line of code
# names is a list of strings
names = [business["name"]
         for business in businesses if business["rating"] >= 4.5]
print(names)

print("-" * 30)
print("---Businesses with reviews >= 4.0")
# great_businesses is a list of dictionaries so we have lots of API data
# besides just the name of the business as previously demonstrated
great_businesses = [
    business for business in businesses if business['rating'] >= 4]
for business in great_businesses:
    print(f"Name: {business['name']}. Avg Rating: {business['rating']}")

"""
Try changing the API call to search for businesses in Canyon, TX or Amarillo TX
change the value of "location": "nyc" to
    "location": "canyon, tx"
or
    "location": "amarillo, tx"

Try changing the API call to search for different types of businesses
change the "term": "barber" to
    "term": "sushi"
or
    "term": "pizza"
or
    "term": "plumbing"

Try changing the data printed. View a list of all the possible variables at
https://www.yelp.com/developers/documentation/v3/business_search
Look in the table under the section called "Response Body"
That table lists all the possible data about a business returned by Yelp
For example "businesses[x].display_phone" is the phone number
formated nicely for display to users. 'display_phone' is the variable/property name.
Access this variable/property in your code with
    print(business['display_phone'])

"""
