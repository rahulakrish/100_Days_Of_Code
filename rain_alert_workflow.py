#!/usr/bin/env python
# coding: utf-8

# ### Modifying the twilio code for Github workflow instead

# In[2]:


import json
import requests
import os 
import smtplib


# In[2]:


#retrieve environment variables
OWM_API_KEY = os.environ.get('OWM_API_KEY')


# In[3]:


#set lat & long to a location where it's raining
lat = 30.406401
long = -87.682083


# In[7]:


#getting the data from the open weather API
api_call= f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={OWM_API_KEY}&units=metric"
response = requests.get(url=api_call)
weather_data = response.json()


# In[1]:


#if it's raining bring an umbrella.
#here, create a flag that is set to true.
#this way, only one print statement gets printed if it's raining within the next 12 hours
will_rain = False

#setting the range because you only need to check for the next 12 hours.
for i in range(0, 4):
    #weather id's b/w 500 and 600 denote raing per the API docs
    if 500 <= weather_data['list'][i]['weather'][0]['id'] < 600:
        will_rain = True

        
        
def send_alert():
    from_email = os.environ.get('FROM_EMAIL')
    to_email = os.environ.get('TO_EMAIL')
    password = os.environ.get('PASSWORD')
    
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr = from_email,
                             to_addr = to_email,
                             msg = "Subject: Rain Alert\n\nForecast is for rain. Don't forget to take an umbrella")
        
def all_clear():
    from_email = os.environ,get('FROM_EMAIL')
    to_email = os.environ.get('TO_EMAIL')
    password = os.environ.get('PASSWORD')
    
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr = from_email,
                             to_addr = to_email,
                             msg = "Subject: All clear\n\nNo rain forecast for today.")
        

if will_rain == True:
    send_alert()
    
else:
    all_clear()
    


# In[ ]:




