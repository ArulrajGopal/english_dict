from googleapiclient.discovery import build
from Credentials import *
import json


youtube =  build("youtube","v3",developerKey=api_key)


request =youtube.channels().list(part="snippet,contentDetails,statistics", id="UC7fQFl37yAOaPaoxQm-TqSA")
response = request.execute()

json = json.dumps(response, indent=4)
string = str(response)

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(json)

# print(string)
    