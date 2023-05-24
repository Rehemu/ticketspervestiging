import requests
import pandas as pd
import openpyxl
import warnings
import json
import datetime as dt
from tabulate import tabulate

behandelaar = "Werkplekbeheer"
status = ('Gereed', 'Afgegesloten')
last_date = '2022-10-07T08:20:25Z'

url = f'https://medux-test.topdesk.net/tas/api/incidents?query=operatorGroup.name=="{behandelaar}"' \
      f';processingStatus.name=out={status};creationDate=gt={last_date}'
print(url)

payload = {}
headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code

meldingen_lijst = []
if response != '':
    clean_response = response.text[1:-1]
    meldingen_lijst.append([clean_response])

response = meldingen_lijst
resultaat_clean = []
for n in response:
    if n[0] != '':
        list_n = n[0]
        list_n = f"[{list_n}]"
        resultaat_clean.append(list_n)

resultaat_clean_flat = []
for n in resultaat_clean:
    x = json.loads(n)
    if len(x) > 1:
        for i in x:
            resultaat_clean_flat.append(i)
    else:
        resultaat_clean_flat.append(x[0])

df = pd.DataFrame(resultaat_clean_flat)
df = df[["number", "creationDate"]]

print(tabulate(df, headers='keys', tablefmt='psql'))
