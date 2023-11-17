import requests
from bs4 import BeautifulSoup
import random
import time
import csv

#REQUESTS
first_url_portion = 'https://www.safeway.com/shop/product-details.'
#first instance of soda that could be found on Safeway's website
int_soda_id = 108010222
last_url_portion = '.html'

#CSV
soda_data = open('soda_data.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(soda_data)
writer.writerow(['Soda Name', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient', 'Ingredient'])

#Removing junk from Soda Names    
def clean_up_name(s):
    for i, char in enumerate(s):
        if not char.isalpha() and char != ' ' and char != '-':
            return s[:i].rstrip()
    return s

#Removing junk from soda ingredients
def clean_up_ingredients(s):
    s = s.replace('(TO PROTECT TASTE)', "")
    s = s.replace('.', '')
    s = s.lower()
    s = s.title()
    s = s.split(',')
    return s


#Main Loop
num_pages_to_scrape = 1000  

for i in range(num_pages_to_scrape):

    #incrementing url as safeway uses simple URL system to count throw and see all sodas
    current_soda_id = int_soda_id + i

    #using requests class to grab page data
    safeway_page = requests.get(first_url_portion+str(current_soda_id)+last_url_portion)
    if safeway_page.status_code == 200:
        print('Connected to page...')
    else:
        print('We have critical failure!')


    #'souping' up the page
    downloaded_page = BeautifulSoup(safeway_page.text, 'html.parser')


    # Soda Name
    soda_name_classes = ['h1']
    soda_name = downloaded_page.find('h1')

    if len(soda_name) > 0:

        if soda_name:
            soda_name = soda_name.text.strip()
            soda_name = clean_up_name(soda_name)

            print('Soda name printed to CSV')
        else:
            print("Soda name not found for ID:", soda_id)


        #Ingredients Gathering
        ingredient_list_target = 'body-text col-12 col-sm-12 col-md-6 col-lg-6 col-xl-6 ingredient-value'
        ingredient_element = downloaded_page.find(class_=ingredient_list_target)
            
        if ingredient_element:
            ingredients = ingredient_element.get_text().strip()
            ingredients = clean_up_ingredients(ingredients)

            print('Ingredients printed to CSV')

        #CSV Writing
        #Putting Soda name and ingredients on same row
        row = []
        row.append(soda_name)
        row.extend(ingredients)        
        writer.writerow(row)

        #Rate Limiting
        sleeping_time = random.uniform(1,3)
        print(f'Pausing for {sleeping_time}')
        time.sleep(sleeping_time)

        #clean up
        print(f'Successfully accessed page {i+1}\n')
    
    else:
        print(f'No soda found on page{i+1}\n')
        sleeping_time = random.uniform(1,3)
        print(f'Pausing for {sleeping_time}')
        time.sleep(sleeping_time)
        continue

