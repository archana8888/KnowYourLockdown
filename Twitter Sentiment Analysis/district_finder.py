import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import string
from bs4 import BeautifulSoup
import requests


stop_words = set(stopwords.words('english'))

emails = '[A-Za-z0-9]+@[a-zA-z].[a-zA-Z]+'
websites = '(http[s]*:[/][/])[a-zA-Z0-9]+'
mentions = '@[A-Za-z0-9]+'

#to check if the place found belongs to India
def get_district(location) :
    parts = location.split(',')
    if(parts[-1]==' India'):
        parts[-2] = parts[-2].strip()
        if(parts[-2].isnumeric()==True):
            district = parts[-4].strip()
            district = simpilfy(district)
            
        else :
            district = parts[-3].strip()
            district = simpilfy(district)
            
    return district

#get html from the website for specified district
def get_soup(entity):
    url = "https://nominatim.openstreetmap.org/search.php?q="+ entity
    request = requests.get(url)
    soup = BeautifulSoup(request.text,'html.parser')
    result = soup.find_all('div', attrs = {'class' : 'result'})
    return result

#chck if given place is a valid for a district
def valid_place(entity_type):
    if (entity_type == '(City)' or entity_type == '(Suburb)' or entity_type == '(Village)' or entity_type == '(Attraction)'or entity_type == '(Tertiary)'or entity_type == '(County)' or entity_type == '(Station)'):
        return True
    else:
        return False
    
    
def clean(text):
    text = re.sub(emails, '', text)#remove emails
    text = re.sub(websites, '', text)# remove urls
    text = re.sub(mentions, '', text)#remove mentions
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc) #remove numbers
    tokens = nltk.word_tokenize(text_rc)    # tokenization
    text = [word for word in tokens if word not in stop_words]  # remove stopwords
    return text

#remove any abbrevations the district name has
def simpilfy(district_full):
    district = district_full.split()
    if(district!=""):
        if(district[-1]=='District' or district[-1]=='Suburban' or district[-1]=='City' or district[-1]=='Urban' or district[-1]=='district'):
            del district[-1]
        else:
            return district_full
        for place in district:
            location =place + " "
        return location

#find district of given place    
def place_to_district(text):
    try:
        district =''
        place = clean(text)
        for i in range(0,len(place)) :
            #if name has two words
            for j in range(0,2):
                if(i!=len(place)-1 and j==0):
                    entity = place[i] + " " + place[i+1] 
                else:
                    entity = place[i]
                try:
                    result = get_soup(entity)
                except:
                    return ''
                if (result == [] or result == None):
                    continue
                for block in result:
                    if (block == []):
                        continue
                    else : 
                        
                        try :
                            entity_type = block.find('span', attrs = {'class' : 'type'}).get_text()
                            if(valid_place(entity_type)):
                                location = block.find('span', attrs = {'class' : 'name'}).get_text()
                                district = get_district(location)
                                
                        except :
                            print('Nothing')
                    if(district != ''):
                        break
                if(district != ''):
                    break
            if(district != ''):
                break
        return district
    except:
        return ''
