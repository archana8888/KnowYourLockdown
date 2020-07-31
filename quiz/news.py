from bs4 import BeautifulSoup
import requests

def get_news():
    url = "https://www.ndtv.com/india"

    request = requests.get(url)
    soup = BeautifulSoup(request.text,'html.parser')
    result = soup.find_all('div', attrs = {'class' : 'nstory_header'})
    link = []
    title =[]
    image_link = []
    data = []
    for news in result:
        news_link = news.find('a', href = True)
        news_title = news.find('a').get_text().strip()
        title.append(news_title)
        link.append(news_link['href'])
    result2 = soup.find_all('div',attrs ={'class' : 'new_storylising_img'})
    for images in  result2:
        image = images.find('img', src = True)
        image_link.append(image['src'])
    
    for i in range(0,len(link)):
        if(link[i]!="" and title[i]!="" and image_link[i] != ""):
            data.append({'title' : title[i], 'link' :link[i], 'image':image_link[i]})
           
    return data