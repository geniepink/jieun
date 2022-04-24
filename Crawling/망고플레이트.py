import json
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import requests

keyword = input("지역,식당 또는 음식 >> ")
encoded = par.quote(keyword)

url = req.Request(f"https://www.mangoplate.com/search/{encoded}", headers={"User-Agent": "Mozilla/5.0"})
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")

name = soup.select("div.info h2.title")
score = soup.select("div.info strong")[:20]
region = soup.select("div.info p.etc")[:20]
move = soup.select("figure.restaurant-item > a")[:20]

menulist = []

while True:
    for _ in range(len(name)):
        food = name[_].text.strip().replace("                                    ", "").replace("\n", "").replace(" ","")
        print(f"음식점 : {food}, 평점 : {score[_].text}점, 지역 : {region[_].text}")
        menulist.append(food)

    review = input("====리뷰 확인할 음식점을 고르세요.==== >>")
    for i in range(len(move)):
        if review == menulist[i]:
            review_page_num = 1
            review_url = f"https://stage.mangoplate.com/api/v5/{move[i].attrs['href']}/reviews.json?language=kor&device_uuid=5cNB31650690010319344zF8V&device_type=web&start_index={(review_page_num-1)*5}&request_count=5&sort_by=2"
            data = requests.get(review_url)
            result = json.loads(data.text)
            if len(result) == 0:
                break
            for j in result:
                print(j["comment"]["comment"])
                print("------------------------------------------")
            review_page_num += 1



# 함수화
# 텍스트 마이닝
# 메모장에 입력
# 감정분석