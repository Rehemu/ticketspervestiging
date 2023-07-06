import requests
import pandas as pd
from tabulate import tabulate

behandelaar = "Werkplekbeheer"
status = ('Gereed', 'Afgegesloten')
last_date = '2022-10-07T08:20:25Z'

page_size = 5000
url = f'https://medux-test.topdesk.net/tas/api/incidents?page_size={page_size}&query=operatorGroup.name=="{behandelaar}"' \
      f';processingStatus.name=out={status};creationDate=gt={last_date}'

headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
response = requests.get(url, headers=headers)

if response.status_code == 200 or response.status_code == 206:
    data = response.json()
    print(response.status_code)
    if data:
        df = pd.DataFrame(data)
        print(tabulate(df, headers='keys', tablefmt='psql'))
    else:
        print("No data received")
else:
    print(f"Request failed with status code {response.status_code}")

df.to_excel('tickets.xlsx',index=False)
