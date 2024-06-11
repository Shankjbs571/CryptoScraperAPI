import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoinMarketCap:
    def __init__(self, coin):
        self.coin = coin
        self.base_url = f"https://coinmarketcap.com/currencies/{coin.lower()}/"

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        return driver
    
    def scrape_data(self):
        driver = self.get_driver()
        try:
            # Using driver to fetch data
            driver.get(self.base_url)
            
            # Using time.sleep to wait for page to load
            time.sleep(3)
            
            # Explicit wait to ensure the web content is fully loaded
            wait = WebDriverWait(driver, 10)
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')))
            
            # Extracting the required data
            data = price_element.text
            print(data)
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Closing the driver
            driver.quit()
            print("driver quited")
        
        return data
    
    def parse_html(self, html_content):
        # Parse the HTML content and extract data
        # Avoid using XPATH, prefer CSS selectors or other methods
        pass
