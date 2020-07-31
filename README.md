<h1>Project Title: KnowYourLockdown!</h1>

<h3><a href = "https://knowyourlockdown.us-south.cf.appdomain.cloud/"> Click here to view working Website</a></h3>
<br>
<img src = "https://i.imgur.com/N0B3N4u.png">
<br>
<img src = "https://i.imgur.com/qZfMwvy.gif">


<h2>Demonstration Video:</h2>

[![Watch the video](https://img.youtube.com/vi/PaBOmoSr_10/0.jpg)](https://youtu.be/PaBOmoSr_10)

<ul>
 <li>An Interactive dashboard which visualizes data on the Indian Map drilled down to each district. It shows the sentiments of people regarding lockdown (Positive, Negative, Neutral), mental health of population during lockdown & live patient count. The website will allow the government to know which region faces which problems(Food Shortage, Transportation, Economic, Daily services, Others ).</li>

 <li>It is a one stop destination to get an overview of the effect of COVID-19 in India. Reports can be generated as required to find general trends by applying various filters ( eg: date wise filter to find how each state/district reacted in the particular time period).</li>
</ul>

<h2>Technologies Used</h2>
<ul>
 <li><b>Django</b></li>
 <li><b>Python</b></li>
 <li><b>Pandas</b></li>
 <li><b>VADER Sentimet Analysis</b></li>
 <li><b>Tweepy & Twitter API</b></li>
 <li><b>Google Sheets API</b></li>
 <li><b>HTML</b></li>
 <li><b>CSS</b></li>
 <li><b>JavaScript & Jquery</b></li>
 <li><b>Apexcharts.js</b></li>
</ul>

<h2>To run the program:</h2>
<ol>
 <li>Paste your Twitter API credentials in cred.py</li>
 <li>Generate the credentials json file from Google Sheets API and replace ibm-hack...json file with it</li>
 <li>Install the required pacakeges with `pip install requirements.txt`</li>
 <li>Open a terminal in Know_Your_Lockdown folder</li>
 <li>Run the following command : `python manage.py runserver`</li>
 <li>That's it! The program is now runing. </li>
 <li>Type 127.0.0.1:8000 in browser to access the dashboard.</li>
 <li>To extract tweeets and patient related data run realtime.py file. </li>
 <li>For real time data keep the realtime.py file running in background.</li>
</ol>
