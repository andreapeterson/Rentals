from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#--- HOUSING DATA---#
### SET- UP
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get("https://www.apartments.com/max-1-bedrooms-under-2500/?bb=ski89x5_yHs0kn_R", headers=HEADERS)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")
### CODE
prices = [price.text for price in soup.find_all(name="p", class_="property-pricing")]
print(prices)
addresses = [address.text for address in soup.find_all(name="div", class_="property-address")]
print(addresses)
links = [link.get("href") for link in soup.find_all(name="a", class_="property-link")]
print(links)

#--- GOOGLE DOCS ---#
### SET-UP
# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

### CODE
for item in range(len(prices)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdW88mLa0xe94kH8lsv_p5Bicg87hM5ju_4jVRiQjcN79CY5g/viewform?usp=sf_link")
    address_fill_in = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_fill_in = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_fill_in = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    time.sleep(2)

    address_fill_in.send_keys(addresses[item])
    price_fill_in.send_keys(prices[item])
    link_fill_in.send_keys(links[item])
    submit_button.click()

driver.close()
