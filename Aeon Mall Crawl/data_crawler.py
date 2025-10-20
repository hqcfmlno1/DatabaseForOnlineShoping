import time
import undetected_chromedriver as uc
class dataCrawler:
    def __init__(self,url,filename,sleep_time):
        self.url = url
        self.filename = filename
        self.sleep_time = sleep_time
    def crawl_data(self):
        self.driver = uc.Chrome()
        self.driver.get(self.url)
        time.sleep(self.sleep_time)
        page_source = self.driver.page_source
        self.driver.quit()
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(page_source)

