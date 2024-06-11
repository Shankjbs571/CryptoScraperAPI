import time
# import pyperclip
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
        self.driver = webdriver.Chrome(options=chrome_options)
        return self.driver
    
    def scrape_data(self):
        driver = self.get_driver()
        try:
            driver.get(self.base_url)
            time.sleep(3)
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
            market_cap_rank_s = market_cap_rank_element.text
            market_cap_rank = market_cap_rank_s.replace('#', '')

            #volume
            volume_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd')))
            volume = volume_element.text

            #volume_rank
            volume_rank_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]/div/dl/div[2]/div[2]/div/span')))
            volume_rank_s = volume_rank_element.text
            volume_rank = volume_rank_s.replace('#', '')


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

            #contracts
            # contracts_name_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/span[1]')))
            # contracts_name = contracts_name_element.text
            
            # copy_address_button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div')))
            # copy_address_button.click()
            # time.sleep(1)
            # address = pyperclip.paste()
            # contract = [
            #     {
            #         "name" : contracts_name,
            #         "address" : address,
            #      }
            # ]
            # print(contract)

            #official_links
            
            # official_links_div = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[3]/section[2]/div/div[2]/div[2]/div[2]/div/div/a')))
            # link = official_links_div.get_attribute('href')
            # name = official_links_div.text
            # official_links = [
            #     {
            #         "name" : name,
            #         "link" : link,
            #     }
            # ]

            # official_links_parent_div = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[3]/section[2]/div/div[2]/div[2]/div[2]/div')))
            # print("all good 1")
            # official_links_child_divs = official_links_parent_div.find_elements(By.TAG_NAME, 'div')
            # print("all good 2")

            # official_links = []
            # for child in official_links_child_divs:
            #     print("its child ")
            #     a_tag = child.find_element(By.TAG_NAME, 'a')
            #     url = a_tag.get_attribute('href')
            #     name = a_tag.text
            #     this_link = {
            #         "name" : name,
            #         "link" : url
            #     }
            #     official_links.append(this_link)
            #     print("appended",name)

            #social_links
            
            # social_links_parent_div = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[3]/section[2]/div/div[2]/div[3]/div[2]/div')))
            # social_links_child_divs = social_links_parent_div.find_elements(By.TAG_NAME, 'div')
            # social_links = []
            # for child in social_links_child_divs:
            #     a_tag = child.find_element(By.TAG_NAME, 'a')
            #     url = a_tag.get_attribute('href')
            #     name = a_tag.text
            #     this_link = {
            #         "name" : name,
            #         "url" : url
            #     }
            #     social_links.append(this_link)

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
                # "contract" : contract,
                # "official_links" : official_links,
                # "socials" : social_links,
                }

            
        except Exception as e:
            print(f"An error occurred: {e}")
            return "error"
        finally:
            # Closing the driver
            if self.driver:
                    self.driver.quit()
                    print("driver quited")


