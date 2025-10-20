from data_crawler import dataCrawler
dataCrawlerForFrozenFood = dataCrawler('https://aeoneshop.com/products/category/205/thuc-pham-dong-lanh%252Fmat/pages/1-5', 'frozen_food.txt', 20)
dataCrawlerForFrozenFood.crawl_data()