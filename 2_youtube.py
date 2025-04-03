#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:02:52 2025

@author: oh
https://youtube-rank.com/borad/bbs/board.php?bo_table=youtube
youtube-rank : root => board => bbs => board.php? (파일과 파라미터 구분)
                                   board.php?bo_table = youtube
                                   bo_table= (파라미터 이름)
                                   
    youtube_rank.xlsx  파일 이용한 시각화
"""

import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'  # macOS 기본 한글 폰트
# plt.rcParams['font.family'] = 'NanumGothic'  # 나눔고딕 사용 시

# youtube_rank.xlsx
df = pd.read_excel('./files/youtube_rank.xlsx')

# 데이터
df.head()
'''
         title     category subscriber       view   video
0    BLACKPINK   [음악/댄스/가수]      9590만  378억7825만    604개
1    김프로KIMPRO  [BJ/인물/연예인]      8690만  547억3689만  2,979개
2    BANGTANTV   [음악/댄스/가수]      7980만  244억0527만  2,699개
3  HYBE LABELS   [음악/댄스/가수]      7650만  380억8129만  2,294개
4   Mark Rober        [미분류]      6430만  102억4266만    196개
'''
df.tail()
'''
                         title     category subscriber     view   video
995                     재훍 영상툰        [미분류]        93만  5억3717만    352개
996          ColorMonsters Toy     [취미/라이프]        93만  5억4939만  1,040개
997                    TAEYONG        [미분류]        92만    1663만     27개
998  영자씨의 부엌Young-Ja's Kitchen  [음식/요리/레시피]        92만  3억1863만  2,217개
999                       배꼽빌라      [TV/방송]        92만  4억5363만    745개
'''

# 구독자수 tn : 0부터 10개만..
df['subscriber'][0:10]
'''
0    9590만
1    8690만
2    7980만
3    7650만
4    6430만
5    6070만
6    4510만
7    3290만
8    3030만
9    3000만
Name: subscriber, dtype: object
'''
# 만 => 0000
df['subscriber'].str.replace('만', '0000')
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.head()

df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 6 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   title                1000 non-null   object
 1   category             1000 non-null   object
 2   subscriber           1000 non-null   object
 3   view                 1000 non-null   object
 4   video                1000 non-null   object
 5   replaced_subscriber  1000 non-null   object
dtypes: object(6)
memory usage: 47.0+ KB
'''
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')

#### 구독자 수 => 파이차트 => 채널 ###
# category => 카테고리 갯수
# replaced_subscriber => 카테고리별로 더하기
# 구독자 수, 채널 수 피봇 테이블 생성
# 데이터프레임.pivot_table()
# index = 'category'
# values = 'replaced_subscriber'
# aggfunc = ['sum', 'count']
pivot_df = df.pivot_table(index = 'category',
                          values = 'replaced_subscriber',
                          aggfunc = ['sum', 'count'])

pivot_df.head()
'''
                            sum                          count
            replaced_subscriber             replaced_subscriber
category                                           
[BJ/인물/연예인]           238590000                  57
[IT/기술/컴퓨터]            11070000                   6
[TV/방송]               285970000                 108
[게임]                   76830000                  45
[교육/강의]                31090000                  18
'''
# 데이터프레임의 칼럼명 변경
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()

# 데이터프레임의 인덱스 초기화
pivot_df = pivot_df.reset_index()

# 데이터프레임을 내림차순 정렬
pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)

plt.figure(figsize = (30,10))

# 카테고리별 구독자수 시각화
plt.pie(pivot_df['subscriber_sum'],
        labels=pivot_df['category'],
        autopct='%1.1f%%')
plt.show()


# 카테고리별 채널 수 시각화
pivot_df = pivot_df.sort_values(by='category_count', ascending=False)
                                
plt.pie(pivot_df['category_count'],
        labels=pivot_df['category'],
        autopct='%1.1f%%')
plt.show()





















