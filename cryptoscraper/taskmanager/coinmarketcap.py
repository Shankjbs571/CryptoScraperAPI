import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Job

class CoinMarketCap:
    def __init__(self, coin):
        self.coin = coin
        self.base_url = f"https://coinmarketcap.com/currencies/{coin.lower()}/"

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        return self.driver
    
    def scrape_data(self):
        driver = self.get_driver()
        try:
            # Using driver to fetch data
            driver.get(self.base_url)
            
            # Using time.sleep to wait for page to load
            time.sleep(3)
            
            # Explicit wait to ensure the web content is fully loaded
            wait = WebDriverWait(driver, 10)

            #price
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')))
            price = price_element.text

            #price_change
            price_change_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-overview"]/div[2]/div/div/p')))
            data_change = price_change_element.get_attribute('data-change')
            s = price_change_element.text
            price_change = s.replace('% (1d)', '')
            if data_change == 'down':
                price_change = "-"+price_change

            #market cap
            market_cap_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[1]/div[1]/dd')))
            market_cap = market_cap_element.text

            #market_cap_rank
            market_cap_rank_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[1]/div[2]/div/span')))
            market_cap_rank = market_cap_rank_element.text

            #volume
            volume_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd')))
            volume = volume_element.text

            #volume_rank
            volume_rank_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[2]/div[2]/div/span')))
            volume_rank = volume_rank_element.text

            #volumne_change
            volume_change_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[3]/div/dd')))
            s = volume_change_element.text
            volumne_change = s.replace('%', '')

            #circulating supply
            circulating_supply_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[4]/div/dd')))
            circulating_supply = circulating_supply_element.text

            #total_supply
            total_supply_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[5]/div/dd')))
            total_supply = total_supply_element.text

            #diluted_market_cap
            diluted_market_cap_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[7]/div/dd')))
            diluted_market_cap = diluted_market_cap_element.text



            print(price)

            return {
                "price" : price,
                "price_change" : price_change,
                "market_cap" : market_cap,
                "market_cap_rank" : market_cap_rank,
                "volume" : volume,
                "volume_rank" : volume_rank,
                "volumne_change" : volumne_change,
                "circulating_supply" : circulating_supply,
                "total_supply" : total_supply,
                "diluted_market_cap" : diluted_market_cap,


                }

            
        except Exception as e:
            print(f"An error occurred: {e}")
            return "error"
        finally:
            # Closing the driver
            if self.driver:
                    self.driver.quit()
                    print("driver quited")


        
            
    def parse_html(self, html_content):
        # Parse the HTML content and extract data
        # Avoid using XPATH, prefer CSS selectors or other methods
        pass
