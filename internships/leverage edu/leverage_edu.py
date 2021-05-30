#Leverage edu

#import important libraries
import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import urllib
import time
import nltk
import re

#using browser: put your driver path here
driver = webdriver.Chrome(executable_path = 'C:\webdrivers\chromedriver')

#putting the university link here
driver.get("https://studyabroad.shiksha.com/netherlands/universities")
time.sleep(10)
#making columns
name = []
location = []
university_type = []
overview = []
column_in_table = []
column2_in_table = []
highlights = []
all_courses = []
ranking = []
adm_reqs_column1 = []
adm_reqs_column2 = []
on_campus = []
off_campus = []
contact = []
video_links = []
fees = []

for i in range(1, 28):
    try:
        
        name_page_1_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[6]/table[2]/tbody/tr['+str(2*i)+']/td[2]/p/a/strong')
        name.append(name_page_1_element.text)

        location_page_1_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[6]/table[2]/tbody/tr['+str(2*i)+']/td[3]')
        location.append(location_page_1_element.text)

        university_type_page_1_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[6]/table[2]/tbody/tr['+str(2*i)+']/td[4]/p[1]')
        university_type.append(university_type_page_1_element.text )
    except:
        continue
    
    driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[6]/table[2]/tbody/tr[2]/td['+str(2*i)+']/p/a').click()
    time.sleep(5)

    for j in range(1, 10):
        try:
        
            column = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/table/tbody/tr['+str(j)+']/td[1]')
            column_in_table.append(column.text)
            column2 = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/table/tbody/tr['+str(j)+']/td[2]')
            column2_in_table.append(column2.text)
    
        except:
            break
    

    highlights_1_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/ul')
    highlights.append(highlights_1_element.text)

    ranking_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[4]/div[2]/div')
    ranking.append(ranking_element.text)

    for j in range(1, 8):
        try:
            
            column = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[10]/div[2]/div[1]/table/tbody/tr['+str(j)+']/td[1]')
            adm_reqs_column1.append(column.text)
            column2 = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[10]/div[2]/div[1]/table/tbody/tr['+str(j)+']/td[2]')
            adm_reqs_column2.append(column2.text)
        except:
            break
        
    on_campus_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[13]/div[2]')
    on_campus.append(on_campus_element.text)

    off_campus_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[14]/div[2]')
    off_campus.append(off_campus_element.text)

    contact_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]')
    contact.append(contact_element.text)

    fees_element = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[2]/div[1]/div[6]/div[2]')
    fees.append(fees_element.text)

    driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[1]/div[2]/a[2]').click()
    time.sleep(5)

    all_courses_1_element = driver.find_element_by_xpath('//*[@id="courseBox"]/div[2]')
    all_courses.append(all_courses_1_element.text)

    driver.get("https://studyabroad.shiksha.com/usa/universities")
    time.sleep(5)

#converting into csv
"""import csv
import pandas as pd



df = pd.DataFrame(list(zip(*[name, location, university_type, overview, columns_in_table, column2_in_table, highlights, all_courses, ranking, adm_reqs_column1, adm_reqs_column2, on_campus, off_campus, contact, video_links, fees))).add_prefix('Col')

df.to_csv('file.csv', index=False)

print(df) 
import csv
with open('leverage_edu.csv', 'wb+') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(('name', 'location', 'university_type', 'overview', 'columns_in_table', 'column2_in_table', 'highlights', 'all_courses', 'ranking', 'adm_reqs_column1', 'adm_reqs_column2', 'on_campus', 'off_campus', 'contact', 'video_links', 'fees'))
    rcount = 0
    for row in name:
        wr.writerow((name[rcount], location[rcount], university_type[rcount], overview[rcount], columns_in_table[rcount], column2_in_table[rcount], highlights[rcount], all_courses[rcount], ranking[rcount], adm_reqs_column1[rcount], adm_reqs_column2[rcount], on_campus[rcount], off_campus[rcount], contact[rcount], video_links[rcount], fees[rcount]))
        rcount = rcount + 1
    myfile.close()"""