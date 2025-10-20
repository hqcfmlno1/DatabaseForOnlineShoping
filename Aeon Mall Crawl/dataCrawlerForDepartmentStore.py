from data_crawler import dataCrawler
dataCrawlerForDepartmentStore = dataCrawler('https://aeoneshop.com/products/category/52/bach-hoa/pages/1-5', 'department_store.txt', 20)
dataCrawlerForDepartmentStore.crawl_data()