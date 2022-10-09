from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pandas as pd
import config

os.environ['PATH']+=r'chromedriver.exe'

driver= webdriver.Chrome()
driver.get(config.url)
driver.implicitly_wait(30)
even = driver.find_elements(By.CLASS_NAME,'even')
odd = driver.find_elements(By.CLASS_NAME,'odd')

data=[]
for i in [odd,even]:
    for k in i:
        data.append([k.text for k in k.find_elements(By.TAG_NAME,'td')])
columns_votes=[ 'count', 'PC Name',	'No',	'Type',	'State',	'Winning Candidate',	'Party'	,'Electors',	'Votes',	'Turnout',	'Margin',	'Margin_percenatge']
  
df=pd.DataFrame(data,columns=columns_votes)

df.to_csv('loksabha.csv',index=False)

