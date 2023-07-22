from selenium import webdriver
import csv
import time
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

url = "https://y.qq.com/"
browser = webdriver.Chrome()
browser.get(url)
page_height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script(f"window.scrollTo(0, {page_height});")
time.sleep(1)  # 等待一秒让页面加载

# 获取模拟滚动后的页面源代码
page_source = browser.page_source
browser.quit()
bs = BeautifulSoup(page_source, "html5lib")
divMV = bs.find("div", attrs={"class": "mod_mv"})
div = divMV.find("div", attrs={"class": "slide__list"})
ulList = div.find_all("ul")[:-1]
# print(ulList)
for ul in ulList:
    liList = ul.find_all("li")

    # print(liList)
    for li in liList:
        name = li.find("h3").text
        # print(name)
        author = li.find("p").text
        # print(author)
        number = li.find("span").text
        if "万" in number:
            number = number.replace("万", "")
        else:
            number = str(float(number) / 10000)
        # print(number)
        with open("QQ音乐MV播放量.csv", "a", encoding="utf-8-sig", newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow([name, author, number])
