#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:59:12 2025

@author: oh

Melon_Crwaling -> Excel 파일로 저장
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 접속할 URL
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

# 웹페이지 html 다운로드
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
#----------------------------------------------
# 반복문을 이용해 곡과 가수명을 song_data에 저장

song_data = []

rank = 1 # 순위

songs = soup.select('table > tbody > tr')
len(songs) # 100

for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > span > a')[0].text

    song_data.append(['Melon', rank, title, singer])
    
    rank = rank + 1
    
song_data[0]
# ['Melon', 1, 'REBEL HEART', 'IVE (아이브)']

columns = ['서비스', '순위', '타이틀', '가수']

pd_data = pd.DataFrame(song_data, columns = columns)

pd_data.head()
'''
     서비스  순위                             타이틀         가수
0  Melon   1                     REBEL HEART  IVE (아이브)
1  Melon   2  HOME SWEET HOME (feat. 태양, 대성)   G-DRAGON
2  Melon   3                          나는 반딧불        황가람
3  Melon   4                        Whiplash      aespa
4  Melon   5                            APT.  로제 (ROSÉ)
'''
pd_data.tail()
'''
      서비스   순위              타이틀           가수
95  Melon   96       earthquake   지수 (JISOO)
96  Melon   97            Storm   김보경 (NEON)
97  Melon   98         Dynamite        방탄소년단
98  Melon   99       Bubble Gum     NewJeans
99  Melon  100  Congratulations  DAY6 (데이식스)
'''

# 크롤링 결과를 액셀 파일로 저장
pd_data.to_excel("./files/melon.xlsx", index = False)

#-----------------------------------------------------------






























