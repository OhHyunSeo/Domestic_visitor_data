#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:02:24 2025

@author: oh
Genie_Crawling
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 접속할 URL
url = 'https://genie.co.kr/chart/top200'
driver.get(url)

# 웹페이지 html 다운로드
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
#----------------------------------------------
# 반복문을 이용해 곡과 가수명을 song_data에 저장
songs = soup.select('tr')
len(songs)
songs[0] # 51
#----------------------------------------------
song_data = []

rank = 1 # 순위

# 1~50 까지
songs = soup.select('table > tbody > tr')
len(songs) # 50

for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text.strip()

    song_data.append(['Genie', rank, title, singer])
    
    rank = rank + 1
    
song_data[0]
# ['Genie', 1, 'REBEL HEART', 'IVE (아이브)']

# 51~100

driver = webdriver.Chrome()
url = 'https://genie.co.kr/chart/top200?ditc=D&ymd=20250218&hh=12&rtm=Y&pg=2'
driver.get(url)

# 웹페이지 html 다운로드
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
# 1~50 까지
songs = soup.select('tbody > tr')
len(songs) # 50

for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text.strip()

    song_data.append(['Genie', rank, title, singer])
    
    rank = rank + 1

song_data[49]



columns = ['서비스', '순위', '타이틀', '가수']

pd_data = pd.DataFrame(song_data, columns = columns)

pd_data.head()
'''
    서비스  순위                 타이틀         가수
0  Bugs   1         REBEL HEART  IVE (아이브)
1  Bugs   2            ATTITUDE  IVE (아이브)
2  Bugs   3              나는 반딧불        황가람
3  Bugs   4            Whiplash      aespa
4  Bugs   5  toxic till the end   로제(ROSÉ)
'''
pd_data.tail()
'''
     서비스   순위       타이틀           가수
95  Bugs   96    살기 위해서          순순희
96  Bugs   97   그녀가 웃었다  DAY6 (데이식스)
97  Bugs   98  아직 거기 살아  DAY6 (데이식스)
98  Bugs   99      MEOW  MEOVV (미야오)
99  Bugs  100   Gravity  FIFTY FIFTY
'''

# 크롤링 결과를 액셀 파일로 저장
pd_data.to_excel("./files/genie.xlsx", index = False)
