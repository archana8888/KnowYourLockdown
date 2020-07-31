import tweepy
import string
import pandas as pd
from fuzzywuzzy import fuzz
import re
import nltk
from prob_class_model import *
from district_finder import *
from cred import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread_dataframe as gd
from datetime import date
from datetime import timedelta
import datetime
import schedule
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from func_timeout import func_timeout,FunctionTimedOut
import time

#Specify credientials for drive and sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'ibm-hack-281412-af7fffea1c18.json', scope)
gc = gspread.authorize(credentials)





#tokenize string
def clean_text(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split()) 


analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    print(lb)
    if lb >= 0.4:
        return 'positive'
    elif (lb > -0.05) and (lb < 0.05):
        return 'neutral'
    elif(lb <= -0.05) or ((lb >= 0.05) and (lb < 0.4)):
        return 'negative'

#specify credentials for twitter API
consumer_key,consumer_secret, access_token, access_token_secret = get_twitter_cred()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=False)

#find id for india
places = api.geo_search(query="INDIA", granularity="country")
place_id = places[0].id

#count the number of sentiments for each district for today
def real_time_sentiments():
    ws_live = gc.open("Sentiment live").worksheet("Master")
    ws_live.clear()
    tweets_ws = gc.open('Real time tweets').worksheet('Master')
    realtime_tweets = pd.DataFrame(tweets_ws.get_all_records())
    
    count_df = pd.DataFrame(columns=['State','District','positive_count','negative_count','neutral_count','hour',])
    #find all states
    state_dist = pd.read_excel('State&Districts.xlsx')
    states = state_dist['State/UT'].unique()
    
    hours=realtime_tweets['hour'].unique()
    
    places = realtime_tweets['district'].unique()
    

    for hour in hours :
            for state in states:
                total_places=state_dist[state_dist['State/UT']==state]
                locations = total_places['Districts'].unique()
                for district in locations:
                    count_positive = 0
                    count_neutral = 0
                    count_negative = 0
                    count_pfs = 0  
                    count_pt = 0  
                    count_pds = 0  
                    count_pe = 0  
                    count_po = 0  
                    for place in places:
                        #fuzzy matching to avoid mismatch due to whitespace
                        if(fuzz.token_sort_ratio(district,place)>80):
                            total=realtime_tweets[realtime_tweets['district']==place]
                            total = total[total['hour']==hour]
                            count_positive=len(total[total['sentiment']=='positive'])
                            count_neutral=len(total[total['sentiment']=='neutral'])
                            count_negative=len(total[total['sentiment']=='negative'])
                    count_df.loc[len(count_df)]=[state,district.strip(),count_positive,count_negative,count_neutral,hour]

    print(count_df)
    
    gd.set_with_dataframe(ws_live,count_df)


#extract tweets
def real_time_tweets():
    ws_og_tweet = gc.open("Tweets").worksheet("Master")
    previous_tweets = pd.DataFrame(ws_og_tweet.get_all_records())
    tweets_ws = gc.open('Real time tweets').worksheet('Master')
    realtime_tweets = pd.DataFrame(tweets_ws.get_all_records())
    
    if(realtime_tweets.empty):
        realtime_tweets = pd.DataFrame(columns=['content','date','district','hour','minutes','place','sentiment','tweetid'])
    print(len(realtime_tweets))
    id_current='1'
    count=0
    duplicate=0
    while(count!=7):
        if(realtime_tweets.empty):
            realtime_tweets = pd.DataFrame(columns=['content','date','district','hour','minutes','place','sentiment','tweetid'])
        count = count+1
        try:
            tweets = api.search(q="place:%s AND covid OR lockdown" % place_id,lang='en',count = 100,result_type='recent',max_id=int(id_current)-1)
        except Exception as e:
            print(e)
            break
        print('---------------------------------start--------------------------------')       
        for tweet in tweets:
            try:
                print(tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place")
                date = tweet.created_at
                hours1 = date.hour
                minutes1 =date.minute
                current_date =datetime.datetime.now()
                current_hour = current_date.hour
                print(hours1, minutes1)
                if(current_hour<hours1):
                    break
                if(hours1 == 0 and minutes1<30 and current_hour <= 7 ):
                    print('---clear---')
                    print(realtime_tweets)
                    
                    tweets_ws.clear()
                    realtime_tweets = pd.DataFrame(tweets_ws.get_all_records())
                    break
                    
                id_current = tweet.id_str
                ids = realtime_tweets['tweetid'].unique().tolist()
                if(id_current not in ids):
                    if(sentiment_analyzer_scores(clean_text(tweet.text)) == 'negative'):
                            problem = classify(tweet.text)
                    else:
                        problem = 'null'
                    if(problem == ''):
                        problem = "null"
                    if(tweet.user.verified):
                        #find district of the place
                        district = place_to_district(tweet.text)
                    else:
                        district = place_to_district(tweet.place.name)
                    if(district==''):
                        continue
                    realtime_tweets.loc[len(realtime_tweets)]=[tweet.text,tweet.created_at.strftime('%Y-%m-%d'),district.strip(),hours1,minutes1,tweet.place.name,sentiment_analyzer_scores(clean_text(tweet.text)),tweet.id_str]
                    previous_tweets.loc[len(previous_tweets)]=[tweet.text,tweet.created_at.strftime('%Y-%m-%d'),district.strip(),tweet.place.name,problem,sentiment_analyzer_scores(clean_text(tweet.text)),tweet.id_str]
                else:
                    duplicate = 1
                    print("Duplicate--------------------------------------------")
                    break
            except:
                continue
            
        if (duplicate):
            break
        print('---------------------------------end--------------------------------')    
        previous_tweets.to_csv(r'tweetsy.csv',index=False,header= True)
        
        gd.set_with_dataframe(tweets_ws,realtime_tweets)
        gd.set_with_dataframe(ws_og_tweet,previous_tweets)
    if(realtime_tweets.empty):
        realtime_tweets = pd.DataFrame(columns=['content','date','district','hour','minutes','place','sentiment','tweetid'])

def format_data(district,html,count):
	if(count == 0):
	    return district
	elif(count == 1):
		value = html.find_all('div', attrs = {'class' : 'td-tc'})
		print(value)
		if(value == []):
			value = html.find_all('div', attrs = {'class' : 'td-sc'})
			if(value == []):
				value = html.find_all('div', attrs = {'class' : 'td-dc'})
		value = value[0].get_text()
		value = value.strip()
		return value
	elif(count == 2):
	    
		value = html.find_all('div', attrs = {'class' : 'td-tr'})
		print(value)
		if(value == []):
			value = html.find_all('div', attrs = {'class' : 'td-sr'})
			if(value == []):
				value = html.find_all('div', attrs = {'class' : 'td-dr'})
		value = value[0].get_text()
		value = value.strip()
		return value
	elif(count == 3):
		value = html.find_all('div', attrs = {'class' : 'td-ta'})
		print(value)
		if(value == []):
			value = html.find_all('div', attrs = {'class' : 'td-sa'})
			if(value == []):
				value = html.find_all('div', attrs = {'class' : 'td-da'})
		value = value[0].get_text()
		value = value.strip()
		return value
	elif(count == 4):
		value = html.find_all('div', attrs = {'class' : 'td-td'})
		print(value)
		if(value == []):
			value = html.find_all('div', attrs = {'class' : 'td-sd'})
			if(value == []):
				value = html.find_all('div', attrs = {'class' : 'td-dd'})
		value = value[0].get_text()
		value = value.strip()
		return value
	else:
	    return district
#get patient count
def live_patient_count():
    url = "https://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/"

    df_patient = pd.DataFrame(columns=['Active','Cured','Deaths','District','State','Total','hour'])

    #Open already stored sheet
    ws_p = gc.open("Real time patients").worksheet("Master")
    
    df_patient = pd.DataFrame(ws_p.get_all_records())
    print(df_patient)
    if(df_patient.empty):
        df_patient = pd.DataFrame(columns=['Active','Cured','Deaths','District','State','Total','hour'])
    hours = df_patient['hour'].unique().tolist()
    ws_all = gc.open("Corona Patient").worksheet("Master")
    
    df_p = pd.DataFrame(ws_all.get_all_records())
    
    #Get names of all states
    state_dist = pd.read_excel('State&Districts.xlsx')
    all_states = state_dist['State/UT'].unique()
    print(all_states)
    end = len(df_p) - 1
    current_date =datetime.datetime.now()
    if(current_date.hour==0):
        df_patient = df_patient.iloc[0:0]
        ws_p.clear()
        df_patient = pd.DataFrame(ws_p.get_all_records())
    if(df_patient.empty):
        df_patient = pd.DataFrame(columns=['Active','Cured','Deaths','District','State','Total','hour'])
    #get html of the specified website
    request = requests.get(url)
    soup = BeautifulSoup(request.text,'html.parser')
    result = soup.find_all('div', attrs = {'class' : 'skgm-td'})

    data = []
    data_patient=[]
    state = 'Total'
    count = 0
    for district in result:
        html = district
        if(len(data)!=0):
            district = re.sub(r"\W", "", district.get_text())
        else:
            district = district.get_text()
            district = district.strip()
            if(district in all_states):
                state = district
            


        if(district=='Districts' or district=='Cases' or district=='Cured' or district=='Active' or district=='Deaths' or district=='State/UT'):
            continue

        data.append(format_data(district,html,count))
        data_patient.append(format_data(district,html,count))
        count = count +1
        if (len(data)== 5):
            data.append(state)
            data_patient.append(state)
            current_date =datetime.datetime.now()
            data.append(current_date.hour)
            data_patient.append(date.today())
            
            
            df_patient.loc[len(df_patient)]=[data[3],data[2],data[4],data[0],data[5],data[1],data[6],]
            df_p.loc[len(df_p)]=[data_patient[3],data_patient[2],data_patient[6],data_patient[4],data_patient[0],data_patient[5],data_patient[1]]
            
            data.clear()
            data_patient.clear()
            count=0
        
    
    hours = df_patient['hour'].unique().tolist()
    if(21 in hours):
        gd.set_with_dataframe(ws_all,df_p)
    gd.set_with_dataframe(ws_p,df_patient)

#del old data for better visualisation
def delete_data():
        ws_og_tweet = gc.open("Tweets").worksheet("Master")
        df = pd.DataFrame(ws_og_tweet.get_all_records())

        ws_og_patient = gc.open("Corona Patient").worksheet("Master")
        df_patient  = pd.DataFrame(ws_og_patient.get_all_records())

        df.sort_values(by=['date'],inplace = True)
        df_patient.sort_values(by=['Date'],inplace = True)



        df_patient.to_csv(r'patient.csv',index=False,header= True)

        dates = df['date'].unique().tolist()
        datesP = df_patient['Date'].unique().tolist()
        
        for date in dates:
                if(len(df['date'].unique().tolist()) > 8 ):
                        df = df[df.date!=date]
                else:
                        break
        for datep in datesP:
                if(len(df_patient['Date'].unique().tolist()) > 9):
                        df_patient = df_patient[df_patient.Date!=datep]
                else:
                        break
        
        gd.set_with_dataframe(ws_og_tweet,df)
        gd.set_with_dataframe(ws_og_patient,df_patient)


#count the number of sentiments for each district for each date
def calc_sentiment():
    ws = gc.open("Tweets").worksheet("Master")
    df = pd.DataFrame(ws.get_all_records())
    ws2 = gc.open("Sentiment").worksheet("Master")
    df2 = pd.DataFrame(ws2.get_all_records())
    count_df = pd.DataFrame(columns=['State','District','positive_count','negative_count','neutral_count','pfs','pt','pds','pe','po','Date'])

    #find all states
    state_dist = pd.read_excel('State&Districts.xlsx')
    states = state_dist['State/UT'].unique()
    print(states)
    dates=df['date'].unique()
    print(dates)
    places = df['district'].unique()
    print(places)

    for date in dates :
            for state in states:
                total_places=state_dist[state_dist['State/UT']==state]
                locations = total_places['Districts'].unique()
                for district in locations:
                    count_positive = 0
                    count_neutral = 0
                    count_negative = 0
                    count_pfs = 0  
                    count_pt = 0  
                    count_pds = 0  
                    count_pe = 0  
                    count_po = 0  
                    for place in places:
                        #fuzzy matching to avoid mismatch due to whitespace
                        if(fuzz.token_sort_ratio(district,place)>80):
                            total=df[df['district']==place]
                            total = total[total['date']==date]
                            count_positive=len(total[total['sentiment']=='positive'])
                            count_neutral=len(total[total['sentiment']=='neutral'])
                            count_negative=len(total[total['sentiment']=='negative'])
                            count_pfs = len(total[total['problem']=="['Food Shortage']"]) 
                            count_pt = len(total[total['problem']=="['Transpotation']"])  
                            count_pds = len(total[total['problem']=="['Daily Services']"]) 
                            count_pe = len(total[total['problem']=="['Economic']"])  
                            count_po = len(total[total['problem']=="['Others']"])  
                    count_df.loc[len(count_df)]=[state,district.strip(),count_positive,count_negative,count_neutral,count_pfs,count_pt,count_pds,count_pe,count_po,date]

    print(count_df)
    gd.set_with_dataframe(ws2,count_df)


#sequence to run all the functions 
def todo():
    try:
        func_timeout(1800,real_time_tweets,args=())
        time.sleep(300)
    except Exception as e:
        print(e) 
        print('Timed out')
    try:
        real_time_sentiments()
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(300)
        try:
            real_time_sentiments()
            time.sleep(300)
        except Exception as e:
            print(e)
            time.sleep(300)
            
    try:
        calc_sentiment()
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(300)
        try:
            calc_sentiment()
            time.sleep(300)
        except Exception as e:
            print(e)
            time.sleep(300)
    try:
        live_patient_count()
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(300)
        try:
            live_patient_count()
            time.sleep(300)
        except Exception as e:
            print(e)
            time.sleep(300)
            
    try:
        delete_data()
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(300)
        try:
            delete_data()
            time.sleep(300)
        except Exception as e:
            print(e)
            time.sleep(300)
             
    
    
    
    

todo()
#to extract tweets every 3 hrs(1hr is required for the todo function to complete)
schedule.every(2).hours.do(todo)

while True:
   schedule.run_pending()