from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)



driver= webdriver.Chrome(options=options)
driver.get("https://www.google.com")
element=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
element.send_keys('how are you'+Keys.ENTER)
element2=driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div[1]/div[1]/div[2]/a/div')
element2.click()
print(driver.title)
