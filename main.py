# 主要流程


import subprocess
import time  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



# 获取已打开的chrome浏览器
def get_opened_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options = chrome_options)
    return driver


# 从tele获得币地址
def get_memeaddr_from_tele():
    addr = r'6g7Jywh8Mx6gohbdibV1SNf9KEkPDHn27tCUMobLpump'


# 获取photon币对应的购买页面
def get_buying_url(driver,addr:str):
    driver.get(r'https://photon-sol.tinyastro.io/zh/discover')
    # print(driver.title)
    time.sleep(1)
    inputPlace = driver.find_element(By.CSS_SELECTOR, r'input.c-autocomplete__input.js-autocomplete.js-intro') #用css_selector寻找有多个类的input元素

    inputPlace.send_keys(addr) # 装入币地址。装入之后等1s，等它反应一下。
    time.sleep(1)

    # 写入bi地址之后再获取id为 autoComplete_result_0 的子a元素
    target_div = driver.find_element(By.ID,r'autoComplete_result_0')
    a_element = target_div.find_element(By.TAG_NAME, 'a')
    href = a_element.get_attribute('href')
    return href


# 在href所指的币页面，购入币
def buying(driver,href:str):
    driver.get(href)

    time.sleep(5)

    inputs = driver.find_elements(
        By.XPATH,
        r'/html/body/div[7]/div[9]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]//input'
        )

    
    print(inputs[0].get_attribute(r'type'))
    print(inputs[0].get_attribute(r'value'))
 
if __name__ == "__main__":

    driver = get_opened_chrome_driver()
    
    href = r'https://photon-sol.tinyastro.io/zh/lp/8RBFUoA6CKQY5JVza9NDhkakY3t78w2sdQpaoYCdJXZX?handle=1186999ac63da1362553b6'

    buying(driver, href)