import requests
import pandas as pd

behandelaar = "Werkplekbeheer"
status = "'Afgesloten','Wachten op goedkeuring','Geannuleerd','Afgewezen'"
last_date = '2022-10-07T08:20:25Z'
fields = '?fields=id,changeType'

page_size = 5000
size_query = "?page_size="
url = "https://medux.topdesk.net"
endpoint = "/tas/api/operatorChanges"
groupNameQuery = f'query=simple.assignee.groupName=={behandelaar};open==true'
fields = "requester.branch.name,simple.assignee.name,simple.assignee.groupName,number"
fields_query = f'fields={fields}'
built_url = f"{url}{endpoint}{size_query}{page_size}&{groupNameQuery}&{fields_query}"
print(built_url)

headers = {'Authorization': 'Basic VE9QREVTS0FQSToyM3J6ay1hNGlkdy1qbmsyay14d3h5Zy1pdHY0NA=='}
response = requests.get(built_url, headers=headers)

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
