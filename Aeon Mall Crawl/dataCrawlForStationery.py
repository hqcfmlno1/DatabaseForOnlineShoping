from data_crawler import dataCrawler
dataCrawlForStationery = dataCrawler('https://aeoneshop.com/products/category/271/van-phong-pham/pages/1-5', 'stationery.txt', 20)
dataCrawlForStationery.crawl_data()