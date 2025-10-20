from bs4 import BeautifulSoup as bs
import lxml 
import random
import pandas as pd


data_file = ['fresh_food.txt','frozen_food.txt','department_store.txt','home_and_life.txt','stationery.txt','health_and_beauty.txt','mother_and_baby.txt','electronics.txt','fashion.txt']
cnt=0
products_list = []
for file_html in data_file:
    with open(file_html, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = bs(content, 'lxml')
    products = soup.find_all('div', class_='qlNqs90CLlvAqJr6YLMK')
    for product in products:
        cnt+=1
        if file_html == 'fresh_food.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'fresh food',
                'image_url': prod_img,
                'stock' : random.randint(100,1000),
            }
            products_list.append(product_info)
        elif file_html == 'frozen_food.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'frozen food',
                'image_url': prod_img,
                'stock' : random.randint(100,1000),
            }
            products_list.append(product_info)
        elif file_html == 'department_store.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'department store',
                'image_url': prod_img,
                'stock' : random.randint(36,200),
            }
            products_list.append(product_info)
        elif file_html == 'home_and_life.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'home and life',
                'image_url': prod_img,
                'stock' : random.randint(100,500),
            }
            products_list.append(product_info)
        elif file_html == 'stationery.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'stationery',
                'image_url': prod_img,
                'stock' : random.randint(50,100),
            }
            products_list.append(product_info)
        elif file_html == 'health_and_beauty.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'health and beauty',
                'image_url': prod_img,
                'stock' : random.randint(100,200),
            }
            products_list.append(product_info)
        elif file_html == 'mother_and_baby.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'mother and baby',
                'image_url': prod_img,
                'stock' : random.randint(100,200),
            }
            products_list.append(product_info)
        elif file_html == 'electronics.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'electronics',
                'image_url': prod_img,
                'stock' : random.randint(10,100),
            }
            products_list.append(product_info)
        elif file_html == 'fashion.txt':
            prod_price = prod_price = product.find('span', class_='g-sr-only').text
            if product.find('span', class_='g-sr-only').text[0]=='D':
                prod_price = product.find('span', class_='g-sr-only').text[20:]
            if product.find('span', class_='g-sr-only').text.find('</0>')!=-1:
                start = product.find('span', class_='g-sr-only').text.find('<0>') + 3
                end = product.find('span', class_='g-sr-only').text.find('</0>')
                prod_price=product.find('span', class_='g-sr-only').text[start:end]
            prod_img = product.find('img', class_='ac5jAXEzjgAvJGypDW47')['src']
            if (prod_img.find('https:')!=-1):
                start = prod_img.find('https:')
                prod_img = prod_img[start:]
            product_info = {
                'product_id': cnt,
                'name': product.h2.text,
                'price': prod_price,
                'category': 'fashion',
                'image_url': prod_img,
                'stock' : random.randint(100,200),
            }
            products_list.append(product_info)


df = pd.DataFrame(products_list)
df['price'] = df['price'].str.replace('₫', '', regex=False).str.replace('.', '', regex=False).astype(int)


food_categories = ['fresh food', 'frozen food','department store']

# create random exp_date for food products
randome_date = []
number_of_food_products = df['category'].isin(food_categories).sum()
for i in range(number_of_food_products):
    randome_date.append(pd.to_datetime(1760745600000000000+random.randint(-4060800000000000,5*4060800000000000)).date())
df.loc[df['category'].isin(food_categories), 'exp_date']= randome_date

#exprt to csv
df.to_csv('products.csv', index=False, encoding='utf-8-sig')


