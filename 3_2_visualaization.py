#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:03:47 2025

@author: oh
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic' 

### 중국인 관광객 시계열
# 1. 중국 국적 데이터 필터링
df = pd.read_excel("./files/kto_total.xlsx")

condition = (df['국적'] == "중국")
df_filter = df[condition]

# 2. 시계열 : plot(x, y)
plt.plot(df_filter['기준년월'], df_filter['관광'])
plt.show()

# 3. 시계열 : 그래프 크기 조절 / 타이틀, x축, y축 이름,  / x 축 눈금값
# 그래프 크기 조절
plt.figure(figsize=(15,5))

# 그래프의 데이터 설정
plt.plot(df_filter['기준년월'], df_filter['관광'])

# 타이틀 : title()
plt.title("중국인 관광객 추이")

# x축 이름 : xlabel()
plt.xlabel("년도")

# y축 이름 : ylabel()
plt.ylabel("관광객수")

# x축 눈금 : xticks() => [ , , ]
plt.xticks(['2010-01',
            '2011-01',
            '2012-01',
            '2013-01',
            '2014-01',
            '2015-01',
            '2016-01',
            '2017-01',
            '2018-01',
            '2019-01',
            '2020-01',
            ])

plt.show()


# 국내 외국인 관광객 중 상위 5개 국각를 각각 시계열
## (중국, 일본, 대만, 미국, 홍콩)

# condition_c = (df['국적'] == "중국")
# df_filter_c = df[condition_c]

condition_j = (df['국적'] == "일본")
df_filter_j = df[condition_j]

# 그래프 크기 조절
plt.figure(figsize=(15,5))

# 그래프의 데이터 설정
plt.plot(df_filter_j['기준년월'], df_filter_j['관광'])

# 타이틀 : title()
plt.title("일본인 관광객 추이")

# x축 이름 : xlabel()
plt.xlabel("년도")

# y축 이름 : ylabel()
plt.ylabel("관광객수")

# x축 눈금 : xticks() => [ , , ]
plt.xticks(['2010-01',
            '2011-01',
            '2012-01',
            '2013-01',
            '2014-01',
            '2015-01',
            '2016-01',
            '2017-01',
            '2018-01',
            '2019-01',
            '2020-01',
            ])

plt.show()
#----------------------------------------------

condition_t = (df['국적'] == "대만")
df_filter_t = df[condition_t]

# 그래프 크기 조절
plt.figure(figsize=(15,5))

# 그래프의 데이터 설정
plt.plot(df_filter_t['기준년월'], df_filter_t['관광'])

# 타이틀 : title()
plt.title("대만인 관광객 추이")

# x축 이름 : xlabel()
plt.xlabel("년도")

# y축 이름 : ylabel()
plt.ylabel("관광객수")

# x축 눈금 : xticks() => [ , , ]
plt.xticks(['2010-01',
            '2011-01',
            '2012-01',
            '2013-01',
            '2014-01',
            '2015-01',
            '2016-01',
            '2017-01',
            '2018-01',
            '2019-01',
            '2020-01',
            ])

plt.show()
#----------------------------------------------

condition_u = (df['국적'] == "미국")
df_filter_u = df[condition_u]

# 그래프 크기 조절
plt.figure(figsize=(15,5))

# 그래프의 데이터 설정
plt.plot(df_filter_u['기준년월'], df_filter_u['관광'])

# 타이틀 : title()
plt.title("미국인 관광객 추이")

# x축 이름 : xlabel()
plt.xlabel("년도")

# y축 이름 : ylabel()
plt.ylabel("관광객수")

# x축 눈금 : xticks() => [ , , ]
plt.xticks(['2010-01',
            '2011-01',
            '2012-01',
            '2013-01',
            '2014-01',
            '2015-01',
            '2016-01',
            '2017-01',
            '2018-01',
            '2019-01',
            '2020-01',
            ])

plt.show()
#----------------------------------------------

condition = (df['국적'] == "홍콩")
df_filter_h = df[condition]

# 그래프 크기 조절
plt.figure(figsize=(15,5))

# 그래프의 데이터 설정
plt.plot(df_filter_h['기준년월'], df_filter_h['관광'])

# 타이틀 : title()
plt.title("홍콩인 관광객 추이")

# x축 이름 : xlabel()
plt.xlabel("년도")

# y축 이름 : ylabel()
plt.ylabel("관광객수")

# x축 눈금 : xticks() => [ , , ]
plt.xticks(['2010-01',
            '2011-01',
            '2012-01',
            '2013-01',
            '2014-01',
            '2015-01',
            '2016-01',
            '2017-01',
            '2018-01',
            '2019-01',
            '2020-01',
            ])

plt.show()
#----------------------------------------------

# 다른 방법
cntry_list = ['중국', '일본', '대만', '미국', '홍콩']

# 시각화 코드를 매번사용할건지 / 아니면 반복문을 통해 사용할것인지 / 아니면 함수처리 할건지
# -> 반복처리가 가장 효율적임

for cntry in cntry_list:
    condition = (df['국적'] == cntry)
    df_filter = df[condition]

    plt.figure(figsize=(15,5))
    plt.plot(df_filter['기준년월'], df_filter['관광'])
    plt.title("{}인 관광객 추이".format(cntry))
    plt.xlabel("년도")
    plt.ylabel("관광객수")
    plt.xticks(['2010-01',
                '2011-01',
                '2012-01',
                '2013-01',
                '2014-01',
                '2015-01',
                '2016-01',
                '2017-01',
                '2018-01',
                '2019-01',
                '2020-01',
                ])

    plt.show()

# 함수처리 : 관광 / 유학 / 기타



def plot_test(cntry, t):
    condition = (df['국적'] == cntry)
    df_filter = df[condition]

    plt.figure(figsize=(15,5))
    plt.plot(df_filter['기준년월'], df_filter['관광'])
    plt.title("{}인 관광객 추이".format(cntry))
    plt.xlabel("년도")
    plt.ylabel("관광객수")
    plt.xticks(['2010-01',
                '2011-01',
                '2012-01',
                '2013-01',
                '2014-01',
                '2015-01',
                '2016-01',
                '2017-01',
                '2018-01',
                '2019-01',
                '2020-01',
                ])
    plt.show()

# plot_test('cntry' t_list)

# 히트맵
'''
매트릭스 형태에 값을 컬러로 표현하는 데이터 시각화 방법
장점 : 전체 데이터를 한눈에 파악할 수 있다.

x축, y축에 어떤 변수들을 사용할 지를 고민해야한다.
'''
# x축 : 월, y 축 : 연
# 데이터 : 관광객수
# => 연도와 월로 구분된 변수를 생성 : 2010-01 str.slice(sIdx, eIdx)
df['년도'] = df['기준년월'].str.slice(0,4)
df['월'] = df['기준년월'].str.slice(5,7)

# 원하는 국적 데이터만 추출 : df_filter
condition = (df['국적'] == '미국')
df_filter = df[condition]

# df_filter 데이터를 매트릭스 형태로 변환 : pivot_table()
# index = '년도'
# columns = '월'
# values = '관광'

df_pivot = df_filter.pivot_table(index = '년도',
                                 columns = '월',
                                 values = '관광')

import seaborn as sns

plt.figure(figsize=(16,10))

sns.heatmap(df_pivot,
            annot = True,
            fmt = '.0f',
            cmap = 'rocket_r')
plt.title("미국 관광객 히트맵")






















