#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:01:54 2025

@author: oh
Bugs_Crawling
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 접속할 URL
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

# 웹페이지 html 다운로드
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
#----------------------------------------------
# 반복문을 이용해 곡과 가수명을 song_data에 저장
songs = soup.select('tr')
len(songs) # 101
'''
<tr>
<th class="check" scope="col"></th>
<th class="ranking" scope="col"><span>순위</span></th>
<th class="albumArt" scope="col"></th>
<th class="trackInfo" scope="col"></th>
<th class="title" scope="col"><span>곡</span></th>
<th class="artist" scope="col"><span>아티스트</span></th>
<th class="album" scope="col"><span>앨범</span></th>
<th class="action play" scope="col"><span>듣기</span></th>
<th class="action add01" scope="col"><span>재생목록</span></th>
<th class="action add02" scope="col"><span>내앨범</span></th>
<th class="action download" scope="col"><span>다운</span></th>
<th class="action mv" scope="col"><span>영상</span></th>
<th class="action etc" scope="col"><span>기타</span></th>
</tr>
'''
songs[0]
#----------------------------------------------
song_data = []

rank = 1 # 순위

songs = soup.select('table.byChart > tbody > tr')
len(songs) # 100

for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text

    song_data.append(['Bugs', rank, title, singer])
    
    rank = rank + 1
    
song_data[0]
# ['Bugs', 1, 'REBEL HEART', 'IVE (아이브)']

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
pd_data.to_excel("./files/bugs.xlsx", index = False)
