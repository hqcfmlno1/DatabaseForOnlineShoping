from data_crawler import dataCrawler
dataCrawlerForFreshFood = dataCrawler('https://aeoneshop.com/products/category/204/thuc-pham-tuoi-song/pages/1-5', 'fresh_food.txt', 20)
dataCrawlerForFreshFood.crawl_data()
