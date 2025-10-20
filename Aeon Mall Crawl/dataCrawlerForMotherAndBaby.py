from data_crawler import dataCrawler
dataCrawlerForMotherAndBaby = dataCrawler('https://aeoneshop.com/products/category/103/me-va-be/pages/1-5', 'mother_and_baby.txt', 20)
dataCrawlerForMotherAndBaby.crawl_data()