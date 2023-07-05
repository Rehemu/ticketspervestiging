import requests
import pandas as pd

# Make a GET request to the API endpoint
server = "https://medux-test.topdesk.net"
endpoint = "/tas/api/locations"
url = server+endpoint
headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
payload = {}
response = requests.request("GET", url, headers=headers, data=payload)


# Check if the request was successful (status code 200)
if response.status_code == 200:
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

response.json()