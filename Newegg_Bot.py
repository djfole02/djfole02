# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:59:28 2020
Newegg 3080 Bot
@author: Danny
"""

#########################
#CHANGE THESE 
URL_Search = 'https://www.newegg.com/p/pl?d=rtx+3000&N=4021%204022'  #change this to whatever search results you were looking at 
cvv = '' #change this to your CVV number on your card
email = ''
password = ''
########################



#######################################################################
#DO NOT TOUCH
#DO NOT TOUCH
#DO NOT TOUCH
#DO NOT TOUCH
######################################################################
URL_Checkout = 'https://secure.newegg.com/shop/cart?Submit=view'
import time
import find_xpath
import emailbot
from selenium import webdriver

def login(driver, email, password):
    time.sleep(2)
    find_xpath.once_look1_click1(driver,'//a[@id="popup-close"]')
    find_xpath.inf_look1_click1(driver, '//div[@class="nav-complex-title"]')
    find_xpath.inf_look1_send1(driver,'//input[@type="email"]', email)
    find_xpath.inf_look1_click1(driver, '//button[@id="signInSubmit"]')
    find_xpath.inf_look1_send1(driver, '//input[@type="password"]', password)
    find_xpath.inf_look1_click1(driver,'//button[@id="signInSubmit"]')
    time.sleep(1) 

def check_availability(driver, cnt, URL):
    while(cnt>-1):
        cnt += 1
        driver.get(URL)
        while(1):
            if len(driver.find_elements_by_xpath('//p[text() = "Error Code: 3"]'))==0:
                if len(driver.find_elements_by_xpath('//button[@class="btn btn-primary btn-mini"]'))>0:#searches for an add to cart button
                    driver.find_element_by_xpath('//button[@class="btn btn-primary btn-mini"]').click()#clicks the add to cart button 
                    if len(driver.find_elements_by_xpath('//button[@class="close"]'))>0:
                        driver.find_element_by_xpath('//button[@class="close"]').click()
                        break
                    cnt = -1 #exits the while loop
                    emailbot.bot(2) #will email 
                    print('Added to Cart potentially')
                    time.sleep(.2)
                else: 
                    time.sleep(.5)
                    print('Refreshed: ' + str(cnt) +' times' )#gives refreshes count in terminal
                    break
            else:
                emailbot.bot(1)
                input("Press Enter to Continue Once You Have Changed The VPN")
                break

def checkout(driver, credit, URL):
    driver.get(URL)
    cnt = 0
    while(1):
        if len(driver.find_elements_by_xpath('//button[@class="btn btn-mini btn-tertiary"]'))>0: #checks for a remove button on the item
            driver.find_element_by_xpath('//button[@class="btn btn-primary btn-wide"]').click() #clicks checkout if there is an item 
            break
        
        else:
            if len(driver.find_elements_by_xpath('//button[@class = "btn btn-secondary"]'))>0:
                driver.find_element_by_xpath('//button[@class = "btn btn-secondary"]').click()
            driver.get(URL_Checkout)
            cnt += 1
            print("Refreshed: " + str(cnt) + " times")

    while(1):
        if len(driver.find_elements_by_xpath('//input[@class="form-text mask-cvv-4"]'))>0:
            driver.find_element_by_xpath('//input[@class="form-text mask-cvv-4"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//input[@class="form-text mask-cvv-4"]').send_keys(credit)
            time.sleep(.5)
            print('I think you got one')
            break
    
    while(1):
        if len(driver.find_elements_by_xpath('//button[@id="btnCreditCard"]'))>0:
            driver.find_element_by_xpath('//button[@id="btnCreditCard"]').click()
            break          
    emailbot.bot(3)
    
def Newegg():
    driver_newegg1 = webdriver.Edge(executable_path=r'C:\msedgedriver.exe')
    driver_newegg1.get(URL_Search)
    driver_newegg1.maximize_window()
    input("Press Enter To Continue After Logging In")
    driver_checkout = webdriver.Edge(executable_path=r'C:\msedgedriver.exe')
    driver_checkout.get(URL_Checkout)
    driver_checkout.maximize_window()
    input("Press Enter To Continue After Logging In")
    check_availability(driver_newegg1, 0, URL_Search)
    checkout(driver_checkout, cvv, URL_Checkout) 

Newegg()

