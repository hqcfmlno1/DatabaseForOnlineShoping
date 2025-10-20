from data_crawler import dataCrawler
dataCrawlerForFashion = dataCrawler('https://aeoneshop.com/products/category/330/thoi-trang-va-phu-kien/pages/1-5', 'fashion.txt', 20)
dataCrawlerForFashion.crawl_data()