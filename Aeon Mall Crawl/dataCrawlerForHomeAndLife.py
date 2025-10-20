from data_crawler import dataCrawler
dataCrawlerForHomeAndLife = dataCrawler('https://aeoneshop.com/products/category/120/nha-cua-va-doi-song/pages/1-5', 'home_and_life.txt', 20)
dataCrawlerForHomeAndLife.crawl_data()