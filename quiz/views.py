from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path
import gspread_dataframe as gd
from .services import allowed_services
from .news import get_news
import random
import numpy as np
# Create your views here.


my_path=os.path.abspath(os.path.dirname(__file__))
credential_path=os.path.join(my_path,"ibm-hack-281412-af7fffea1c18.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scope)
gc = gspread.authorize(credentials)

spreadsheet_key = '1yXp18xyRVbTmx0BHCfUhtYc-SD7JPG5qYXGtiJ_VpI4'
wks_name = 'Master'

    #get tweets sheet to calculate
ws = gc.open("Sentiment").worksheet("Master")
df = pd.DataFrame(ws.get_all_records())

ws2 = gc.open("Corona Patient").worksheet("Master")
df_patient  = pd.DataFrame(ws2.get_all_records())

datasentiment = df.sort_values(by=['Date'])
dates_sentiment =datasentiment['Date'].unique()
print(dates_sentiment)
date_sentient = dates_sentiment.tolist().pop()
currentdatasentiment = datasentiment[datasentiment['Date']==date_sentient]
pos_sent = currentdatasentiment['positive_count'].sum()
neu_sent = currentdatasentiment['neutral_count'].sum()
neg_sent = currentdatasentiment['negative_count'].sum()
total_sent = pos_sent + neg_sent + neu_sent

datapatient = df_patient.sort_values(by=['Date'])
dates_patient =datapatient['Date'].unique()
print(dates_patient)
date_patient = dates_patient.tolist().pop()
currentdatapatient = datapatient[datapatient['Date']==date_patient]
datacount = currentdatapatient[currentdatapatient['District']=='Total']
total_patient_count = datacount['Total'].max()
active_patient_count = datacount['Active'].max()
cured_patient_count = datacount['Cured'].max()
death_patient_count = datacount['Deaths'].max()

def show_quiz(request):
    sheet = gc.open("Mental Health").worksheet("Form Responses 1")
    mh_df = pd.DataFrame(sheet.get_all_records())
    total = int(mh_df.Negative_Effect.count())
    data = mh_df[mh_df['Negative_Effect']=='Yes']
    lockdown_yes = int(data.Negative_Effect.count())
    lockdown_no = int(mh_df[mh_df['Negative_Effect']=='No'].Negative_Effect.count())
    lockdown_maybe = int(mh_df[mh_df['Negative_Effect']=='Maybe'].Negative_Effect.count())
    female = int(data[data['Gender']=='Female'].Negative_Effect.count())
    male = int(data[data['Gender']=='Male'].Negative_Effect.count())
    other = int(data[data['Gender']=='Other'].Negative_Effect.count())
    age = int(data[data['Age']=='18-30 years'].Negative_Effect.count())
    age_below = int(data[data['Age']=='Below 18 years'].Negative_Effect.count())
    age_above = int(data[data['Age']=='Above 30 years'].Negative_Effect.count())
    no_percent = (lockdown_no/total)*100
    yes_percent = (lockdown_yes/total)*100
    maybe_percent = (lockdown_maybe/total)*100
    male_percent = (male/lockdown_yes)*100
    female_percent = (female/lockdown_yes)*100
    other_percent = (other/lockdown_yes)*100
    age_percent = (age/lockdown_yes)*100
    age_below_percent = (age_below/lockdown_yes)*100
    age_above_percent = (age_above/lockdown_yes)*100
    context = {
        'yes': yes_percent,
        'no':no_percent,
        'maybe':maybe_percent,
        'age':age_percent,
        'age_above':age_above_percent,
        'age_below':age_below_percent,
        'male':male_percent,
        'female':female_percent,
        'other':other_percent,
        'tcount':total_sent,
        'theading':'Sentiments',
        'rcount':neg_sent,
        'rheading':'Negative',
        'ycount':neu_sent,
        'yheading':'Neutral',
        'gcount':pos_sent,
        'gheading':'Positive',
    }
    
    return render(request, 'quiz/quiz.html',context)


def home(request):
    return render(request, 'quiz/home.html')

def get_chart(request):
    print(df)
    cdf,state_df =get_country_data()
    patient_total,patient_top10 = total_patient()
    context = {
        'cdf':cdf,
        'state_df':state_df,
        'patient_total':patient_total,
        'patient_top10':patient_top10,
        'tcount':total_sent,
        'theading':'Sentiments',
        'rcount':neg_sent,
        'rheading':'Negative',
        'ycount':neu_sent,
        'yheading':'Neutral',
        'gcount':pos_sent,
        'gheading':'Positive',
    }
    return render(request, 'quiz/chart.html',context)



    #get specific sheet


def get_location_data(state):
    sdf = pd.DataFrame(columns=['Date','pos','neu','neg'])
    state_patient = pd.DataFrame(columns=['Date','total','active','cured','deaths'])
    data= df[df['State']==state]
    dates = data['Date'].unique()
    for date in dates:
        data1= data[data['Date']==date]
        pos = data1['positive_count'].sum()
        neu = data1['neutral_count'].sum()
        neg = data1['negative_count'].sum()
        sdf.loc[len(sdf)] = [date,pos,neu,neg]
    
    data_patient = df_patient[df_patient['District']==state] 
    dates_patient = data_patient['Date'].unique()
    for date in dates_patient:
        data = data_patient[data_patient['Date']==date]
        
        total = data['Total'].sum()
        active = data['Active'].sum()
        cured = data['Cured'].sum()
        deaths = data['Deaths'].sum()
        state_patient.loc[len(state_patient)]=[date,total,active,cured,deaths]
    return sdf, state_patient


def get_country_data():
    cdf = pd.DataFrame(columns=['Date','pos','neu','neg'])
    district_df= pd.DataFrame(columns=['state','district','pos','neu','neg'])
    for date in df['Date'].unique():
        data= df[df['Date']==date]
        pos = data['positive_count'].sum()
        neu = data['neutral_count'].sum()
        neg = data['negative_count'].sum()
        cdf.loc[len(cdf)] = [date,pos,neu,neg]
    states = df['State'].unique()
    dates = df['Date'].unique()
    state_df = pd.DataFrame(columns=['state','pos','neu','neg'])
    for state in states:
            data= df[df['State']==state]
            pos = data['positive_count'].sum()
            neu = data['neutral_count'].sum()
            neg = data['negative_count'].sum()
            state_df.loc[len(state_df)] = [state,pos,neu,neg]
  
    state_df=state_df.sort_values(by = ['pos','neu','neg'],ascending=False)
    
    return cdf,state_df.head(10)


def total_patient():
    patient_total = pd.DataFrame(columns=['Date','total','active','cured','deaths'])
    patient_top10 = pd.DataFrame(columns=['state','total','active','cured','deaths'])
    for date in df_patient['Date'].unique():
        data= df_patient[df_patient['Date']==date]
        data = data[data['District']=='Total']
        total = data['Total'].sum()
        active = data['Active'].sum()
        cured = data['Cured'].sum()
        deaths = data['Deaths'].sum()
        patient_total.loc[len(patient_total)]=[date,total,active,cured,deaths]
    dates =  df_patient['Date'].unique()
    currentdate = '2020-07-02'
    data1 = df_patient[df_patient['Date']==currentdate]
    
    states = data1['State'].unique()
    
    for state in states:
        if(state != 'Total'):
            data = data1[data1['District']==state]
            total = data['Total'].sum()
            active = data['Active'].sum()
            cured = data['Cured'].sum()
            deaths = data['Deaths'].sum()
            patient_top10.loc[len(patient_top10)]=[state,total,active,cured,deaths]
    patient_top10=patient_top10.sort_values(by = ['total'],ascending=False)
    return patient_total,patient_top10.head(10)


def get_district_data(district,state):
    district_sentiment = pd.DataFrame(columns=['Date','pos','neu','neg'])
    district_patient = pd.DataFrame(columns=['Date','total','active','cured','deaths'])
    data= df[df['State']==state]
    dates = data['Date'].unique()
    for date in dates:
       
        data1= data[data['Date']==date]
        data_district = data1[data1['District']==district]
        
        pos = data_district['positive_count'].sum()
        neu = data_district['neutral_count'].sum()
        neg = data_district['negative_count'].sum()
        district_sentiment.loc[len(district_sentiment)] = [date,pos,neu,neg]
    
    
    if(district=='Bangalore Urban' or district == 'Bangalore Rural'):
        place =district.split(' ')
        place[0]= 'Bengaluru'
        district = place[0] +" "+ place[1]
    data_patient = df_patient[df_patient['State']==state] 
    dates_patient = data_patient['Date'].unique()
    for date in dates_patient:
        data = data_patient[data_patient['Date']==date]
        data_district = data[data['District']==district]
        
        total = data_district['Total'].sum()
        active = data_district['Active'].sum()
        cured = data_district['Cured'].sum()
        deaths = data_district['Deaths'].sum()
        district_patient.loc[len(district_patient)]=[date,total,active,cured,deaths]
       
    return district_sentiment, district_patient


def submit(request):
    data=[]
    sheet_key = '1YKDFlcMWo0Hkm_FZe7Lmnsn3ttE0eqC6Mo02NymkJrc'
    sheet = gc.open("Mental Health").worksheet("Form Responses 1")
    mh_df = pd.DataFrame(sheet.get_all_records())
    data.append(request.GET.get('state').strip())
    data.append(request.GET.get('district').strip())
    data.append(request.GET.get('age'))
    data.append(request.GET.get('gender'))
    data.append(request.GET.get('negative_effect'))
    data.append(request.GET.get('help'))
    mh_df.loc[len(mh_df)]=data
    print(data)
    gd.set_with_dataframe(sheet, mh_df)
    
    return render(request, 'quiz/quiz.html',)

def getdata(request):
    state = request.POST.get('state')
    district = request.POST.get('district')
    print(state,district)
    if(district!=None):
        district=district.strip()
    sdf,state_patient = get_location_data(state)
    cdf ,state_df= get_country_data()
    district_sentiment, district_patient = get_district_data(district,state)
    patient_total,patient_top10 = total_patient()
    context = {
        'sdf':sdf,
        'cdf':cdf,
        'state':state,
        'state_df':state_df,
        'patient_total':patient_total,
        'patient_top10':patient_top10,
        'state_patient':state_patient,
        'district_sentiment':district_sentiment,
        'district_patient':district_patient,
        'district' : district,
        'tcount':total_sent,
        'theading':'Sentiments',
        'rcount':neg_sent,
        'rheading':'Negative',
        'ycount':neu_sent,
        'yheading':'Neutral',
        'gcount':pos_sent,
        'gheading':'Positive',
    }
    return render(request, 'quiz/chart.html',context)

file_path=os.path.join(my_path,"tweetsy.csv")
tweets = pd.read_csv(file_path)
tweets = tweets.sort_values(by=['date'])
dates = tweets['date'].unique()
print(dates)
date = dates.tolist().pop()
data = tweets[tweets['date']==date]
positive_data = data[data['sentiment']=='positive']
negative_data = data[data['sentiment']=='negative']
pos_ids = positive_data['tweetid'].unique()
neg_ids = negative_data['tweetid'].unique()    
pos_ids = pos_ids.tolist()
neg_ids = neg_ids.tolist()    
pos_random_ids = random.sample(pos_ids,3)
neg_random_ids = random.sample(neg_ids,3)
data = get_news()
data = random.sample(data,6)
number_pos = []
number_neg = []
for id in pos_random_ids:
    number_pos.append(format(id,"0.0f"))
for id in neg_random_ids:
    number_neg.append(format(id,"0.0f"))

def info(request):
    context = {
        'allowed_services': allowed_services,
        'data':data,
        'id1':number_pos[0],
        'id2':number_pos[1],
        'id3':number_neg[2],
        'id4':number_pos[2],
        'id5':number_neg[0],
        'id6':number_neg[1],
        'tcount': total_patient_count,
        'theading':'Cases',
        'rcount': death_patient_count,
        'rheading':'Deaths',
        'ycount':active_patient_count,
        'yheading':'Active',
        'gcount':cured_patient_count,
        'gheading':'Cured',
        }
    return render(request, 'quiz/info.html', context)

def map(request):
    context = {
        'tcount':total_sent,
        'theading':'Sentiments',
        'rcount':neg_sent,
        'rheading':'Negative',
        'ycount':neu_sent,
        'yheading':'Neutral',
        'gcount':pos_sent,
        'gheading':'Positive',
    }
    return render(request, 'quiz/map.html',context)