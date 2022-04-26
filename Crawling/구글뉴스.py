from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import chromedriver_autoinstaller
import time
import os
import openpyxl
import datetime

keyword = input("키워드를 입력하세요 >>")
chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)

page_num = 0
page = 1
rank = 1
while True:
    browser.get("https://www.google.co.kr/search?q={}&tbs=qdr:w&tbm=nws&sxsrf=ALeKk01Z5HjBrqCbE2DFrKpJjO_waCcANQ:1615095474813&ei=smZEYN2GMci9hwONto7QDQ&start={}&sa=N&ved=0ahUKEwjdp7fAu53vAhXI3mEKHQ2bA9oQ8tMDCIQB&biw=1604&bih=940&dpr=1".format(keyword,page_num))
    time.sleep(3)

    browser.find_element_by_css_selector("html").send_keys(Keys.END)
    time.sleep(3)

    title = browser.find_elements_by_css_selector("div.hI5pFf div.JheGif.nDgy9d")
    news_company = browser.find_elements_by_css_selector("div.XTjFC.WF4CUc")


    print("--------최신 업데이트 : {} 페이지 --------".format(page))
    if len(title) == 0:
        break
    for i in range(len(title)):
        print("{}번 {} : {}".format(rank,news_company[i].text,title[i].text))
        rank += 1

    page_num += 10
    page += 1

    if page_num == 30:
        browser.close()
        break