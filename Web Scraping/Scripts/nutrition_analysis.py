import pandas as pd
from pandas import Series,DataFrame
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import argparse
import numpy as np

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
        gender_input = input('\nPlease choose your gender: (Please follow the format: Female or Male) ')
        if gender_input != 'Female' and gender_input != 'Male':
            gender_input = input('Please enter valid gender: (Please follow the format: Female or Male) ')

        return (recipes_input, age_input, gender_input)

def cal_percentage():
    n_df = pd.read_csv('nutrition_goal_1.csv', index_col = [0])
    u = user_input()
    age_input = u[1]
    gender_input = u[2]
    recipe_input = u[0]
    age_range = ' '
    if 1 <= age_input <= 3:
        cal_standard = n_df['Calories Goal'][0]
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

    g_a = gender_input + ' ' + age_range
    for a in range(len(n_df["Age-Sex Groups"])):
        if g_a == n_df['Age-Sex Groups'][a]:
            cal_standard = n_df['Calories Goal'][a]
    
    cal_df = pd.read_csv('recipe_to_nutri_1.csv')
    cal_num = cal_df['calories'][int(recipe_input)]
    cal_to_goal = cal_num / int(cal_standard)
    
    return cal_to_goal

def viz_cal():
    cal_infor = pd.read_csv('recipe_to_nutri_1.csv', index_col = [0])
    viz_cal = cal_infor.sort_values('calories').plot.barh(x = 'recipes', y = 'calories')
    plt.axvline(x = 120.0, c = "r", ls = "--", lw = 2)
    return viz_cal

def viz_nut():
    n_infor = pd.read_csv('nutrition_goal_1.csv', index_col = [0])
    viz_nut = n_infor.plot.barh(x = 'Age-Sex Groups', y = 'Calories Goal')
    plt.axvline(x = 116 / 0.06, c = "r", ls = "--", lw = 2)
    plt.axvline(x = 198 / 0.06, c = "g", ls = "--", lw = 2)
    return viz_nut

if __name__ == "__main__":
    cal_per = cal_percentage()
    print(cal_per)
    if cal_per >= 0.06:
        print("Watch Out! Your recipe's calories exceed daily limits of 6%!")
    else:
        left = str(round(100 * (0.06 - cal_per), 2))
        print("Your recipe's calories have not exceeded daily limits of 6%.")
        print('You still have ' + left + '%' + ' calories left.')

    graph_input = input('Do you want to see graphs? - Yes or No ')

    if graph_input == 'Yes' or graph_input == 'Y' or graph_input == 'yes' or graph_input == 'y':
        print('Please check the Barchart at /data folder.')
    elif graph_input == 'No' or graph_input == 'N' or graph_input == 'no' or graph_input == 'n':
        print('Thank you for letting me know that you don not like beautiful graphs.')
    else:
    	graph_input = input('Please input your answer again: ')
else:
	print('This file was imported as a module! __name__ is', __name__)