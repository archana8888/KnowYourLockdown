import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#Specify credientials for drive and sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'ibm-hack-281412-af7fffea1c18.json', scope)
gc = gspread.authorize(credentials)

ws_og_tweet = gc.open("Tweets").worksheet("Master")
previous_tweets = pd.DataFrame(ws_og_tweet.get_all_records())

print(previous_tweets['date'].unique())

