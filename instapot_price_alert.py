#import libraries

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
import os


#create an instance of the webdriver
driver = webdriver.Edge()

#open the web page
driver.get('https://appbrewery.github.io/instant_pot/')

#the price is actually in a hidden element that cannot be accessed using the .text property
#aok-offscreen class is usually used for screen-reader / hidden accessibility text
#So even if Selenium finds the element, .text often returns "", because Selenium only reads visible rendered text.
get_price = driver.find_element(By.CLASS_NAME,'aok-offscreen')

#need to use this instead
price_text = get_price.get_attribute('textContent')

# print(price_text)

final_price = float(price_text.split('$')[1].strip())
# print(final_price)


#function to send the email alert
def send_alert():
    from_email = os.environ.get('FROM_EMAIL')
    to_email = os.environ.get('TO_EMAIL')
    password = os.environ.get('PASSWORD')

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs= to_email,
                            msg='Instapot price alert\n\nPrice below $100\nTime to buy!')
        
if final_price < 100:
    send_alert()