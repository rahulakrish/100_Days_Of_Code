
#this file will be used to run a GitHub workflow

import requests
import pandas as pd
import json
import smtplib
import os

stock_api_key = os.environ.get('STOCK_API_KEY')
news_api_key = 'abc345'
symbol='TSLA'


# making the API call to get stock data
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={stock_api_key}"
r = requests.get(url)
data = r.json()

#converting to a df for further use
df = pd.DataFrame(data['Time Series (Daily)'])

#transposing the data to make it readable
df=df.T

#sorting the index in ascending order
df=df.sort_index(ascending=True)
#renaming columns
df.columns = ['Open','High','Low','Close','Volume']


#convert all the column dataypes to numeric to do calculations
df = df.apply(pd.to_numeric)

#creating a new column to calculate the closing price difference using diff() 
df['closing_difference'] = df['Close'].diff()

#changing the value of the last row from NaN to 0
#diff() will calculate the the difference w.r.t the previous row. First row has no previous value and hence will always be NaN
#replacing the NaN with 0
df['closing_difference'].fillna(0,inplace=True)

#same analogy with pct_change. First change will always be Nan
df['closing_pct_change'] = round(df['Close'].pct_change()*100,2)
#filling in the empty row value with 0
df['closing_pct_change'].fillna(0,inplace=True)


#getting the abs value of the change. You want to be notified of a swing > 5%, whether its +ve or -ve
df['absolute_change'] = abs(df['closing_pct_change'])

#use reset_index to have the dates as a column.
#this will make it easier to use as a ref when making api calls
df.reset_index()

#using inplace argument to modify the df
df.reset_index(inplace=True)

#renaming the column
df.rename(columns={'index': 'Date'},inplace=True)

#changing the Date data type to str to parse into api calls
df['Date'] = df['Date'].astype(str)


def send_alert():
    from_email = os.environ.get('FROM_EMAIL')
    to_email = os.environ.get('TO_EMAIL')
    password = os.environ.get('PASSWORD')

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr = from_email,
                            to_addrs = to_email,
                            msg = 'Subject: TSLA alert\n\nChange from the previous day > $3.\nFind out why')
        
        
#get the last value in the absolute change column.
#this will correspond to the previous day's closing change.
if df.iloc[-1,-1] >= 1:
    send_alert()   
