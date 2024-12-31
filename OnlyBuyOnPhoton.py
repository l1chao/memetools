import requests
from bs4 import BeautifulSoup

# 目标网页URL
url = r'https://blog.csdn.net/sohoqq/article/details/134348817'

# 发送HTTP请求获取页面内容
response = requests.get(url)
response.encoding = 'utf-8'  # 根据网页编码设置，确保中文等字符正确显示

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 根据div的id或class属性获取特定div的内容
# 假设我们要获取id为"my-div"的div内容
div_content = soup.find('div', id='my-div')

# 打印div内容
if div_content:
    print(div_content.text)  # 获取div的文本内容
    print(div_content.prettify())  # 获取div的完整HTML内容
else:
    print("未找到指定的div")



