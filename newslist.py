import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com/')#html ssourse를 받아옴
soup = BeautifulSoup(res.text,'html.parser')
news= soup.select('.thumb_box._NM_NEWSSTAND_THUMB._NM_NEWSSTAND_THUMB_press_valid')
#클래스명으로 파싱을 진행할 때는 클래스명들 사이에 점을 찍어야해용
news[0].select('a.btn_popup')[2].get('href')#a태그에 atn_popup클래스 안에 href속성에 있는 url을 가져옴.
news_list = []
for line in news:
    url = line.select('a.btn_popup')[2].get('href')
    news_list.append(url)
print(news_list)