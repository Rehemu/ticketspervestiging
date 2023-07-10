import requests
import pandas as pd

behandelaar = "Werkplekbeheer"
status = "'Afgesloten','Wachten op goedkeuring','Geannuleerd','Afgewezen'"
last_date = '2022-10-07T08:20:25Z'
fields = '?fields=id,changeType'

page_size = 5000
url = f'https://medux.topdesk.net/tas/api/operatorChanges?page_size={page_size}&' \
      f'query=simple.assignee.groupName=={behandelaar};open==true'

headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
response = requests.get(url, headers=headers)

if response.status_code == 200 or response.status_code == 206:
    data = response.json()
    print(response.status_code)
    if data:
        df = pd.DataFrame(data)
    else:
        print("No data received")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

df.to_excel('changes.xlsx', index=False)
