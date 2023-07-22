from bs4 import BeautifulSoup
import requests
import csv

'''
network里面获取真实链接
'''
url = "https://music.163.com/discover/playlist"
headers = {
    # 浏览器信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
# print(response.status_code)
bs = BeautifulSoup(response.content, "html5lib")
# print(bs)
ul = bs.find("ul", attrs={"id": "m-pl-container"})
# print(ul)
liList = ul.find_all("li")
# print(liList)
for li in liList:
    title = li.find("a", attrs={"class": "s-fc0"}).text.strip()
    # print(title)
    number = li.find("span", attrs={"class": "nb"}).text.strip()
    if "万" in number:
        number = number.replace("万", "")
    else:
        number = str(float(number) / 10000)
    # print(number)
    with open("网易云歌单播放量爬取.csv", "a", encoding="utf-8-sig", newline="") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow([title, number])

# text:网页源代码
# content:想获取媒体文件的时候
# json():获取json数据时
