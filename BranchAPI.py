import requests
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Make a GET request to the API endpoint
server = "https://medux-test.topdesk.net"
endpoint = "/tas/api/branches?fields=id,name,postalAddress"

url = server+endpoint
headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
payload = {}
response = requests.request("GET", url, headers=headers, data=payload)


# Check if the request was successful (status code 200)
if response.status_code == 200 or response.status_code == 206:
    # Convert the JSON response to a Python dictionary
    data = response.json()
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    df.to_excel('branches.xlsx', index=False)
    # Print the DataFrame
    print(df)

else:
    # Print an error message if the request was unsuccessful
    print('Error accessing API:', response.status_code)

# filter rows where 'Text' column contains any of the words 'test', 'home', 'improvement'
df = df[~df['name'].str.contains(r'Dummy|Standaard|Improvement', na=False, regex=True, case=False)]

# Assuming your dataframe is df and the address column is 'Address'
geolocator = Nominatim(user_agent="geoapiExercises")

# Create a geocoding function with rate limiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Apply the geocoder with the rate limiter
df['name'] = df['name'].str.split(',', expand=True)[0]
df['location'] = df['name'].apply(geocode)

# Get latitude and longitude
df['latitude'] = df['location'].apply(lambda loc: loc.latitude if loc else None)
df['longitude'] = df['location'].apply(lambda loc: loc.longitude if loc else None)

# Remove the temporary 'location' column
df = df.drop('location', axis=1)

df.to_excel('branches.xlsx', index=False)
