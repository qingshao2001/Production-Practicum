from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

url = "https://www.kugou.com/"
browser = webdriver.Chrome()
browser.get(url)
page_height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script(f"window.scrollTo(0, {page_height});")
time.sleep(1)  # 等待一秒让页面加载

# 获取页面源代码
page_source = browser.page_source
browser.quit()
# print(page_source)
bs = BeautifulSoup(page_source, "html5lib")
divxiaoshuo = bs.find("div", attrs={"class": "homep_d1_d4"})
divList = divxiaoshuo.find_all("div", attrs={"class": "homep_d1_d1_d4"})
# print(divList)
for div in divList:
    divList2 = div.find_all("div", attrs={"class": "homep_cm_item_st2 _s2"})
    # print(divList2)
    for li in divList2:
        name = li.find("p", attrs={"class": "homep_cm_item_st2_p1"}).text
        # print(name)
        minDiv = li.find("div", attrs={"class": "homep_cm_item_st2_d2"})
        number = minDiv.find("span", attrs={"class": "homep_cm_item_st2_sp4"}).text
        if "万" in number:
            number = number.replace("万", "")
        else:
            number = str(float(number) / 10000)
        # print(number)
        with open("酷狗说书播放数据.csv", "a", encoding="utf-8-sig", newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow([name, number])
