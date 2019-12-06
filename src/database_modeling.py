import requests
from bs4 import BeautifulSoup
import json
from pandas import Series,DataFrame
import pandas as pd

def access_nutri():
    hg = requests.get('https://health.gov/dietaryguidelines/2015/guidelines/appendix-7/')
    soup_hg = BeautifulSoup(hg.content, 'lxml')
    soup_title = soup_hg.find('thead').find_all('th')
    soup_cal = soup_hg.find('tbody').find('tr').find_all('th')
    health_goal = {'Age-Sex Groups': 0, 'Calories Goal': 0}
    group_list = []
    value_list = []
    
    for n in range(len(soup_title)):
        group_list.append(soup_title[n].text)
        s = soup_cal[n].text.strip(',').split(' ')
        s1 = " ".join(s)
        value_list.append(s1)
    
    group_list = group_list[1:]
    value_list = value_list[1:]
    health_goal['Age-Sex Groups'] = group_list
    health_goal['Calories Goal'] = value_list
    
    df = DataFrame(health_goal)
    nutri_infor = df.to_csv('nutrition_goal_1.csv')
    return nutri_infor

def perfect_database():
    cal_df = pd.read_csv('recipe_to_nutri.csv')
    i_list = []
    for ing in cal_df['ingredients']:
        ing1 = ing.replace("[", "").replace("]", "").replace("'", "")
        i_list.append(ing1)
    cal_df['ingredients'] = i_list
    cal_df.drop(cal_df.filter(regex="Unname"),axis=1, inplace=True)
    cal_infor = cal_df.to_csv('recipe_to_nutri_1.csv')
    return cal_df