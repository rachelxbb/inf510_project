import requests
from bs4 import BeautifulSoup
import json
from pandas import Series,DataFrame
import pandas as pd
import sys
import argparse
import numpy as np

def scrap_webpages(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    
    return soup

def user_input():
    recipes_number = [n for n in range(1, 24)]
    recipe1 = '1. Turmeric-Tahini Dressing\n'
    recipe2 = '2. Lemon-Anchovy Vinaigrette\n'
    recipe3 = '3. Green Sauce No.4\n'
    recipe4 = '4. Creamy Lemon-Mustard Vinaigrette\n'
    recipe5 = '5. Gribiche (Hard-Boiled Egg) Dressing\n'
    recipe6 = '6. Peanut Dressing\n'
    recipe7 = '7. Easy Homemade Caesar Dressing\n'
    recipe8 = '8. Soy-Seasame Dressing\n'
    recipe9 = '9. Grilled Green Salad with Coffee Vinaigrette\n'
    recipe10 = '10. Buttermilk Ranch Dressing\n'
    recipe11 = '11. Herby Lime Dressing\n'
    recipe12 = '12. Sesame-Miso Vinaigette\n'
    recipe13 = '13. Charred Corn Husk Oil Dressing\n'
    recipe14 = '14. Canal House Green Goddess Dressing\n'
    recipe15 = '15. Miso-Turmeric Dressing\n'
    recipe16 = '16. Simplest Asian Dressing\n'
    recipe17 = '17. Fresh Chive Vinaigrette\n'
    recipe18 = '18. Creamy Herb Dressing\n'
    recipe19 = '19. Citrus Vinaigrette\n'
    recipe20 = '20. Cashew Caesar Dressing\n'
    recipe21 = '21. Buttermilk Green Goddess Dressing\n'
    recipe22 = '22. Miso, Carrot, and Sesame Dressing\n'
    recipe23 = '23. Creamy Dijon Vinaigrette'

    print('Here are our 23 creative salad dressing recipes:\n\n', recipe1, recipe2, recipe3, recipe4, recipe5, recipe6, recipe7, recipe8, recipe9, recipe10, recipe11, recipe12, recipe13, recipe14, recipe15, recipe16, recipe17, recipe18, recipe19, recipe20, recipe21, recipe22, recipe23)
    recipes_input = input('Please choose your recipe number: (once a time) ')
    try:
        int(recipes_input) in recipes_number
    except (TypeError, ValueError, IndexError):
        print('Your chosen recipe does not exist.')
        recipes_input = input('Please enter the recipe number again: ')

    else:
        recipes_input = str(int(recipes_input) - 1)
        age_input = int(input('\nPlease enter your age: '))
        if age_input < 0:
            age_input = int(input('Please enter valid number: '))
        gender_input = input('\nPlease choose your gender (Female or Male): ')
        if gender_input != ('Female' or 'Male'):
            gender_input = input('Please enter valid gender: ')

        return (recipes_input, age_input, gender_input)

def recipes_scrap():
    recipe_content = scrap_webpages('https://www.bonappetit.com/recipes/slideshow/salad-dressings-summer')
    main_table = recipe_content.find_all('a', {"aria-label": "View Recipe"})

    link_list = []
    for i in range(len(main_table)):
        link_list.append(main_table[i].get('href'))
    return link_list

def recipe1():
    recipe = scrap_webpages(recipes_scrap()[0])
    ingr1 = [recipe.select("[data-reactid='165']")[0].text, recipe.select("[data-reactid='167']")[0].text, 
    recipe.select("[data-reactid='169']")[0].text, recipe.select("[data-reactid='171']")[0].text,
    recipe.select("[data-reactid='173']")[0].text]
    ingr1_l = str(ingr1)

    return ingr1_l

def recipe2():
    recipe = scrap_webpages(recipes_scrap()[1])
    ingr2 = [recipe.select("[data-reactid='165']")[0].text, recipe.select("[data-reactid='167']")[0].text, 
    recipe.select("[data-reactid='169']")[0].text, recipe.select("[data-reactid='171']")[0].text,
    recipe.select("[data-reactid='173']")[0].text]
    ingr2_l = str(ingr2)
    
    return ingr2_l

def recipe3():
    recipe = scrap_webpages(recipes_scrap()[2])
    ingr3 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text, recipe.select("[data-reactid='180']")[0].text,
    recipe.select("[data-reactid='182']")[0].text, recipe.select("[data-reactid='184']")[0].text]
    ingr3_l = str(ingr3)

    return ingr3_l

def recipe4():
    recipe = scrap_webpages(recipes_scrap()[3])
    ingr4 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text]
    ingr4_l = str(ingr4)

    return ingr4_l

def recipe5():
    recipe = scrap_webpages(recipes_scrap()[4])
    ingr5 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text]
    ingr5_l = str(ingr5)

    return ingr5_l

def recipe6():
    recipe = scrap_webpages(recipes_scrap()[5])
    ingr6 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text]
    ingr6_l = str(ingr6)

    return ingr6_l

def recipe7():
    recipe = scrap_webpages(recipes_scrap()[6])
    ingr7 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text]
    ingr7_l = str(ingr7)

    return ingr7_l

def recipe8():
    recipe = scrap_webpages(recipes_scrap()[7])
    ingr8 = [recipe.select("[data-reactid='157']")[0].text, recipe.select("[data-reactid='159']")[0].text, 
    recipe.select("[data-reactid='161']")[0].text, recipe.select("[data-reactid='163']")[0].text, 
    recipe.select("[data-reactid='165']")[0].text, recipe.select("[data-reactid='167']")[0].text]
    ingr8_l = str(ingr8)

    return ingr8_l

def recipe9():
    recipe = scrap_webpages(recipes_scrap()[8])
    ingr9 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text]
    ingr9_l = str(ingr9)

    return ingr9_l

def recipe10():
    recipe = scrap_webpages(recipes_scrap()[9])
    ingr10 = [recipe.select("[data-reactid='156']")[0].text, recipe.select("[data-reactid='158']")[0].text, 
    recipe.select("[data-reactid='160']")[0].text, recipe.select("[data-reactid='162']")[0].text, 
    recipe.select("[data-reactid='164']")[0].text, recipe.select("[data-reactid='166']")[0].text,
    recipe.select("[data-reactid='168']")[0].text, recipe.select("[data-reactid='170']")[0].text]
    ingr10_l = str(ingr10)

    return ingr10_l

def recipe11():
    recipe = scrap_webpages(recipes_scrap()[10])
    ingr11 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text, recipe.select("[data-reactid='180']")[0].text,
    recipe.select("[data-reactid='182']")[0].text, recipe.select("[data-reactid='184']")[0].text,
    recipe.select("[data-reactid='186']")[0].text, recipe.select("[data-reactid='188']")[0].text,
    recipe.select("[data-reactid='190']")[0].text]
    ingr11_l = str(ingr11)

    return ingr11_l

def recipe12():
    recipe = scrap_webpages(recipes_scrap()[11])
    ingr12 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text, recipe.select("[data-reactid='180']")[0].text,
    recipe.select("[data-reactid='182']")[0].text]
    ingr12_l = str(ingr12)

    return ingr12_l

def recipe13():
    recipe = scrap_webpages(recipes_scrap()[12])
    ingr13 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text]
    ingr13_l = str(ingr13)

    return ingr13_l

def recipe14():
    recipe = scrap_webpages(recipes_scrap()[13])
    ingr14 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text]
    ingr14_l = str(ingr14)

    return ingr14_l

def recipe15():
    recipe = scrap_webpages(recipes_scrap()[14])
    ingr15 = [recipe.select("[data-reactid='161']")[0].text, recipe.select("[data-reactid='163']")[0].text, 
    recipe.select("[data-reactid='165']")[0].text, recipe.select("[data-reactid='167']")[0].text, 
    recipe.select("[data-reactid='169']")[0].text, recipe.select("[data-reactid='171']")[0].text,
    recipe.select("[data-reactid='173']")[0].text]
    ingr15_l = str(ingr15)

    return ingr15_l

def recipe16():
    recipe = scrap_webpages(recipes_scrap()[15])
    ingr16 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text]
    ingr16_l = str(ingr16)

    return ingr16_l

def recipe17():
    recipe = scrap_webpages(recipes_scrap()[16])
    ingr17 = [recipe.select("[data-reactid='164']")[0].text, recipe.select("[data-reactid='166']")[0].text, 
    recipe.select("[data-reactid='168']")[0].text, recipe.select("[data-reactid='170']")[0].text, 
    recipe.select("[data-reactid='172']")[0].text, recipe.select("[data-reactid='174']")[0].text,
    recipe.select("[data-reactid='176']")[0].text, recipe.select("[data-reactid='178']")[0].text,
    recipe.select("[data-reactid='180']")[0].text]
    ingr17_l = str(ingr17)

    return ingr17_l

def recipe18():
    recipe = scrap_webpages(recipes_scrap()[17])
    ingr18 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text]
    ingr18_l = str(ingr18)

    return ingr18_l

def recipe19():
    recipe = scrap_webpages(recipes_scrap()[18])
    ingr19 = [recipe.select("[data-reactid='164']")[0].text, recipe.select("[data-reactid='166']")[0].text, 
    recipe.select("[data-reactid='168']")[0].text, recipe.select("[data-reactid='170']")[0].text, 
    recipe.select("[data-reactid='172']")[0].text, recipe.select("[data-reactid='174']")[0].text]
    ingr19_l = str(ingr19)

    return ingr19_l

def recipe20():
    recipe = scrap_webpages(recipes_scrap()[19])
    ingr20 = [recipe.select("[data-reactid='161']")[0].text, recipe.select("[data-reactid='163']")[0].text, 
    recipe.select("[data-reactid='165']")[0].text, recipe.select("[data-reactid='167']")[0].text, 
    recipe.select("[data-reactid='169']")[0].text, recipe.select("[data-reactid='171']")[0].text,
    recipe.select("[data-reactid='173']")[0].text]
    ingr20_l = str(ingr20)

    return ingr20_l

def recipe21():
    recipe = scrap_webpages(recipes_scrap()[20])
    ingr21 = [recipe.select("[data-reactid='164']")[0].text, recipe.select("[data-reactid='166']")[0].text, 
    recipe.select("[data-reactid='168']")[0].text, recipe.select("[data-reactid='170']")[0].text, 
    recipe.select("[data-reactid='172']")[0].text, recipe.select("[data-reactid='174']")[0].text,
    recipe.select("[data-reactid='176']")[0].text]
    ingr21_l = str(ingr21)

    return ingr21_l

def recipe22():
    recipe = scrap_webpages(recipes_scrap()[21])
    ingr22 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text]
    ingr22_l = str(ingr22)

    return ingr22_l

def recipe23():
    recipe = scrap_webpages(recipes_scrap()[22])
    ingr23 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text]
    ingr23_l = str(ingr23)

    return ingr23_l

def recipe24():
    recipe = scrap_webpages(recipes_scrap()[23])
    ingr24 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text]
    ingr24_l = str(ingr24)

    return ingr24_l

def recipe25():
    recipe = scrap_webpages(recipes_scrap()[24])
    ingr25 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text,
    recipe.select("[data-reactid='178']")[0].text]
    ingr25_l = str(ingr25)

    return ingr25_l

def recipe26():
    recipe = scrap_webpages(recipes_scrap()[25])
    ingr26 = [recipe.select("[data-reactid='163']")[0].text, recipe.select("[data-reactid='164']")[0].text, 
    recipe.select("[data-reactid='166']")[0].text, recipe.select("[data-reactid='168']")[0].text, 
    recipe.select("[data-reactid='170']")[0].text, recipe.select("[data-reactid='172']")[0].text,
    recipe.select("[data-reactid='174']")[0].text, recipe.select("[data-reactid='176']")[0].text]
    ingr26_l = str(ingr26)

    return ingr26_l

def recipe27():
    recipe = scrap_webpages(recipes_scrap()[26])
    content = recipe.select("[data-reactid='163']")[0].text
    temp_content = content.split(' ')
    temp_content
    temp_ingr = []
    remove_list = ['a', 'Pulse', 'and', 'With', 'motor', 'running', 'slowly', 'add', 'then',
                   'Season', 'to', 'taste', 'with', 'blender', 'in', 'to', 'combine.']
    for word in temp_content:
        if word not in remove_list:
            temp_ingr.append(word)
        else:
            continue

    ingr = ' '.join(temp_ingr)
    temp_ingr27 = ingr.split(', ')
    temp_ingr27.append(temp_ingr27[-1][:-35])
    temp_ingr27.append(temp_ingr27[-2][-33:-1])
    temp_ingr27.pop(-3)

    ingr27 = temp_ingr27
    ingr27_l = str(ingr27)

    return ingr27_l

def ingredient_list():
    ingredient_list = [recipe1(), recipe2(), recipe3(), recipe4(), recipe5(), recipe6(), 
                       recipe7(), recipe8(), recipe9(), recipe10(), recipe11(), recipe12(), 
                       recipe13(), recipe14(), recipe15(), recipe16(), recipe17(), recipe18(), 
                       recipe19(), recipe20(), recipe21(), recipe22(), recipe23(), recipe24(), 
                       recipe25(), recipe26(), recipe27()]
    return ingredient_list

def translate_recipe():
    i1 = ingredient_list()
    i_list = []
    r_list = []
    cal_list = []
    recipe_to_nutri = {'recipes': 0, 'ingredients': 0, 'calories': 0}

    recipes_list = ['Turmeric-Tahini Dressing', 'Lemon-Anchovy Vinaigrette', 
                'Green Sauce No.4', 'Creamy Lemon-Mustard Vinaigrette', 
                'Gribiche (Hard-Boiled Egg) Dressing', 'Peanut Dressing', 
                'Cherry Tomato Vinaigrette', 'Classic French Dressing', 
                'Easy Homemade Caesar Dressing', 'Soy-Seasame Dressing', 
                'Grilled Green Salad with Coffee Vinaigrette', 'Buttermilk Ranch Dressing', 
                'Herby Lime Dressing', 'Sesame-Miso Vinaigette', 'Charred Corn Husk Oil Dressing', 
                'Simone Shallot Vinaigrette', 'Canal House Green Goddess Dressing', 
                'Miso-Turmeric Dressing', 'Simplest Asian Dressing', 'Herb Dressing', 
                'Fresh Chive Vinaigrette', 'Creamy Herb Dressing', 'Citrus Vinaigrette', 
                'Cashew Caesar Dressing', 'Buttermilk Green Goddess Dressing', 
                'Miso, Carrot, and Sesame Dressing', 'Creamy Dijon Vinaigrette']
    for i in range(len(i1)):
        recipe_to_nutri_con = {
            'title': recipes_list[i],
            'ingr': eval(i1[i])
        }
        recipe = json.dumps(recipe_to_nutri_con)

        url = "https://api.edamam.com/api/nutrition-details?app_id=b7132d5d&app_key=040fb7ac1136156809d1ee31de9b69c7"
        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers = headers, data = recipe)

    
        if "error" in r.text:
            continue
        else:
            stat = r.text
            ser = stat.split('  ')[2].strip(',\n')
            cal = stat.split('  ')[3].strip(',\n')
            ind_ser = ser.find(':')+2
            ind_cal = cal.find(':')+2
            ser_number = eval(ser[ind_ser:])
            cal_number = eval(cal[ind_cal:])
            cal_per_ser = cal_number /ser_number
            cal_list.append(cal_per_ser)
            i_list.append(i1[i])
            r_list.append(recipes_list[i])

    recipe_to_nutri['recipes'] = r_list
    recipe_to_nutri['ingredients'] = i_list
    recipe_to_nutri['calories'] = cal_list

    return recipe_to_nutri
    
def access_nutri():
    hg = requests.get('https://health.gov/dietaryguidelines/2015/guidelines/appendix-7/')
    soup_hg = BeautifulSoup(hg.content, 'lxml') 
    soup_title = soup_hg.find('thead').find_all('th')
    soup_cal = soup_hg.find('tbody').find('tr').find_all('th')
    key_list = []
    value_list = []
    for n in range(len(soup_title)):
        key_list.append(soup_title[n].text)
        s = soup_cal[n].text.strip(',').split(' ')
        value_list.append(s)
    key_list = key_list[1:]
    value_list = value_list[1:]
    health_goal = dict(zip(key_list, value_list))
    
    df = DataFrame(health_goal)
    df.index = ['Calories Goal']
    return df

def local_nutri():
    nutri_infor = access_nutri().to_csv('nutrition_goal.csv')
    return nutri_infor

def local_calories():
    recipe_to_nutri = translate_recipe()
    df = DataFrame(recipe_to_nutri)
    csv1 = df.to_csv('recipe_to_nutri.csv')
    return csv1

def get_local():
    u = user_input()
    age_input = u[1]
    gender_input = u[2]
    recipe_input = u[0]
    age_range = ' '
    if 1 <= age_input <= 3:
        cal_standard = df['Child 1-3'][0]
    elif 4 < age_input <= 8:
        age_range = '4-8'
    elif 8 < age_input <= 13:
        age_range = '9-13'
    elif 14 < age_input <= 18:
        age_range = '15-18'
    elif 18 < age_input <= 30:
        age_range = '19-30'
    elif 30 < age_input <= 50:
        age_range = '31-50'
    elif 50 < age_input:
        age_range = '51+'
    
    nutrition_df = pd.read_csv('nutrition_goal.csv')
    cal_standard = nutrition_df[gender_input + ' ' + age_range][0]
    t = list(cal_standard)
    number_list = [ ]

    for i in range(len(t)):
        if len(t) > 5 and (i == 5 or i == 11):
            t[i] = " "
        elif len(t) <= 5:
            cal_goals = int(cal_standard.replace(',', ''))
        else:
            cal1 = ''.join(t).strip(',').split(' ')
            if len(cal1) > 1:
                for number in cal1:
                    number_list.append(int(number.replace(',', '')))
                    cal_goals = int(np.mean(number_list))
    
    cal_df = pd.read_csv('recipe_to_nutri.csv')
    cal_num = cal_df['calories'][int(recipe_input)]
    cal_to_goal = cal_num / cal_goals
    
    return cal_to_goal

def get_remote():
    u = user_input()
    inputs = int(u[0])
    # recipes_scrap()
    cal_num = translate_recipe()['calories'][inputs]

    age_input = u[1]
    gender_input = u[2]
    age_range = ' '
    if 1 <= age_input <= 3:
        cal_standard = df['Child 1-3'][0]
    elif 4 < age_input <= 8:
        age_range = '4-8'
    elif 8 < age_input <= 13:
        age_range = '9-13'
    elif 14 < age_input <= 18:
        age_range = '15-18'
    elif 18 < age_input <= 30:
        age_range = '19-30'
    elif 30 < age_input <= 50:
        age_range = '31-50'
    elif 50 < age_input:
        age_range = '51+'

    df = access_nutri()
    cal_standard = df[gender_input + ' ' + age_range][0]
    t = list(cal_standard)
    number_list = [ ]

    for i in range(len(t)):
        if len(t) > 5 and (i == 5 or i == 11):
            t[i] = " "
        elif len(t) <= 5:
            cal_goals = int(cal_standard.replace(',', ''))
        else:
            cal1 = ''.join(t).strip(',').split(' ')
            if len(cal1) > 1:
                for number in cal1:
                    number_list.append(int(number.replace(',', '')))
                    cal_goals = int(np.mean(number_list))
    
    cal_to_goal = cal_num / cal_goals
    return cal_to_goal

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-source', choices=['local', 'remote'], help='This is what the data source')
    args = parser.parse_args()

    location = args.source
    if location == 'local':
        cal_to_goal = get_local()
        print(cal_to_goal)
    else:
        cal_to_goal = get_remote()
        print(cal_to_goal)

else:
    cal_to_goal = get_remote()
    print(cal_to_goal)