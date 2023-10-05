from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pyperclip

import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()



url = "https://play.mungmeelt.com/latte"

driver.get(url)

login_bar = driver.find_element(By.ID,'username-login')
login_bar.send_keys('289456maximum289456')

pwd_bar = driver.find_element(By.ID,'pw-login')
pwd_bar.send_keys('789454')

login_btn = driver.find_element(By.CLASS_NAME,'login-pf-settings')
login_btn.click()

time.sleep(5)



game_bar = driver.find_element(By.XPATH,'//*[@id="CARD_GAME_COIN"]/div[1]/div[2]')

input("Please Click Game Bar : ")




while True: 

    # D = LOW 
    # H = High

    history_latest = driver.find_element(By.CSS_SELECTOR,'div.lead-high-low-content')
    print(history_latest.get_attribute('innerHTML'))

    latest_hist_col = history_latest.find_element(By.CSS_SELECTOR,'div.flex-column')

    all_history  =  []

    dot_high = [ j.get_attribute('innerHTML') for j in latest_hist_col.find_elements(By.CSS_SELECTOR,'.HIGH')]

    dot_low = [ j.get_attribute('innerHTML') for j in latest_hist_col.find_elements(By.CSS_SELECTOR,'.LOW')]

    win_lose_hist = driver.find_element(By.CSS_SELECTOR,'button.yellow')
    win_lose_hist.click()
    
    latest_round_row = driver.find_element(By.CSS_SELECTOR,'tbody').find_elements(By.CSS_SELECTOR,'tr')[1]
    lisx = latest_round_row.find_elements(By.CSS_SELECTOR,'td')
    lat_round_result = lisx[4].text
    lat_round_guess = lisx[2].text 
    
    close_pop = driver.find_element(By.CSS_SELECTOR,'div.v-overlay__content > button')


    


    btn20 = [  p for p in driver.find_elements(By.CSS_SELECTOR,'.price-button')][1]

    print(btn20.get_attribute('innerHTML'))
    

    btn50 = [  p for p in driver.find_elements(By.CSS_SELECTOR,'.price-button')][2]
    print(btn50.get_attribute('innerHTML'))

    print(lat_round_result)
    print(lat_round_guess)

    print("LOW")
    print(dot_low,len(dot_low))

    print("HIGH")
    print(dot_high,len(dot_high))

    try:
        close_pop.click()
        time.sleep(3)
    except: 
        pass 
    
    
    guess_card_lis = driver.find_element(By.CSS_SELECTOR,'div.justify-space-around').find_elements(By.CSS_SELECTOR,'div.rounded-lg')
    print("--------------")
    print(guess_card_lis)
    
    
    
    print("High BTN")
    high_btn = guess_card_lis[0]
    print(high_btn.get_attribute('innerHTML'))
    
    #high_btn.click()

    low_btn = guess_card_lis[1]
    print(low_btn.get_attribute('innerHTML'))
    
    if len(dot_low) == 3:  #D

        try:
            time.sleep(3)
            btn20.click()
            high_btn.click()
        except:
            pass

        print("Guess High")

    
    elif len(dot_high) == 3:
        try:
            time.sleep(3)
            btn20.click()
            low_btn.click()
        except:
            pass         
        print("Guess Low")


    elif len(dot_low) == 4:  #D 4 
        try:
            time.sleep(3)
            btn50.click()
            high_btn.click()
            
        except: 
            pass

        print("Guess High")



    elif len(dot_high) == 4: #H 4

        try:
            time.sleep(3)
            btn50.click()
            low_btn.click()
            
        except: 
            pass

        print("Guess Low")
           



print('hehe')

