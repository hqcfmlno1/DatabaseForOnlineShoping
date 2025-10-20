from data_crawler import dataCrawler
dataCrawlerForHealthAndBeauty = dataCrawler('https://aeoneshop.com/products/category/160/suc-khoe-va-sac-dep/pages/1-5', 'health_and_beauty.txt', 20)
dataCrawlerForHealthAndBeauty.crawl_data()