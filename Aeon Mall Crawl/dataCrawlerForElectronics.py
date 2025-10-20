from data_crawler import dataCrawler
dataCrawlerForElectronics = dataCrawler('https://aeoneshop.com/products/category/91/dien-may---dien-tu/pages/1-5', 'electronics.txt', 20)
dataCrawlerForElectronics.crawl_data()