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
    ip_port = '127.0.0.1:7897'
    chrome_options.add_argument(f"--proxy-server={ip_port}")
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
def buying(driver,href:str,sol_amount,slide_point= r'15',youxian= r'0.008',huilu= r'0.012'):
    driver.get(href)

    time.sleep(5)

    inputPlace = driver.find_element(By.XPATH,r'/html/body/div[7]/div[9]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/input')
    inputPlace.send_keys(sol_amount)

    time.sleep(2)

    inputs = driver.find_elements(
        By.XPATH,
        r'/html/body/div[7]/div[9]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]//input'
        )

    target_div = driver.find_element(By.XPATH,r'/html/body/div[7]/div[9]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[4]/div[1]/div[1]')
    target_div.click()
    time.sleep(0.5) # 点div一下，不用反应很久

    if slide_point != '15':
        inputs[0].send_keys(slide_point)
        time.sleep(1)
    if youxian !='0.008':
        inputs[4].send_keys(youxian)
        time.sleep(1)
    if huilu != '0.012': 
        inputs[5].send_keys(huilu)
        time.sleep(1)
    
    button = driver.find_element(By.XPATH, r"(//button[@data-type='now'])[1]")
    button.click()
 
if __name__ == "__main__":

    # 先打开一个debug浏览器，运行命令：
    # chrome.exe --remote-debugging-port=9222
    # subprocess.Popen(['chrome.exe', '--remote-debugging-port=9222'])

    driver = get_opened_chrome_driver()
    
    # 获得币交易地址
    # addr = get_memeaddr_from_tele()
    # href = get_buying_url(driver,addr)
    href = r'https://photon-sol.tinyastro.io/zh/lp/8RBFUoA6CKQY5JVza9NDhkakY3t78w2sdQpaoYCdJXZX?handle=1186999ac63da1362553b6'


    buying(driver, href=href, sol_amount=r'0.00000000001', youxian=r'0.00000000001', huilu=r'0.00000000001')

# .//input[contains(@class,'class1') and contains(@class,'class2') and contains(@class,'class3')]
