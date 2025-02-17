'''
기본 내장 모듈 : built_in module (math / time / ramdom)

외부 모듈 : external module
터미널에서 모듈 설치해야함 : pip install 모듈이름

pip install Flask - 웹서버 생성
pip install beautifulsoup4 - 데이터 불러와서 분석 (웹크롤링) - 크롤링 : 데이터를 가져온다
pip install tensorflow - 간단한 인공지능

1. 책 구매해서 어떤 모듈 사용하는지 보기
    파이썬 웹 - Django / Flask
    머신러닝 - scikit-learn / tensorflow
    웹크롤링 - requests / beautifulsoup4
    영상분석 - cv2 / pillow
    파이썬 알고리즘 / 파이썬 인공지능 / 파이썬 가상환경 / 파이썬 웹크롤링 / 파이썬 머신러닝  등등

2. 구글링 ***
    음악 - python midi

웹크롤링 주의사항
법적 제약이 따른다.
정보통신망 제 48 조 정보통신망 침해 행위 금지

1. 데이터 수집 목적 : 개인적인 학습이나 연구 목적으로 사용하고 상업적인 목적으로는 이용 X
2. 데이터 사용 : 수집한 데이터는 허용된 범위 내에서만 사용해야합니다. 악용 X
3. 웹사이트 서버에 과부하를 주지 않도록 많은 사람들이 사용하는 사이트는 반복적으로 스크롤링 X
'''

# 크롤링
from urllib import request
from bs4 import BeautifulSoup
news_url = "https://www.korea.kr/rss/policy.xml"

response = request.urlopen(news_url)
xml = response.read()
soup = BeautifulSoup(xml,"xml")


# data = request.urlopen(news_url)
# with request.urlopen(news_url) as response:
#         soup = BeautifulSoup(response,"xml")

items = soup.select("item") # 특정한 이름을 가진 테크를 모두 찾아줌
title = soup.select_one("title").text # 특정 이름을 가진 테그를 하나만 찾아줌

print(items)
print(title)












