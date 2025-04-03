#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:02:42 2025

@author: oh
"""

# 크롤링 결과가 담긴 멜론, 벅스, 지니 크롤링 엑셀 파일 통합
import pandas as pd

excel_names = ["./files/bugs.xlsx",
               "./files/melon.xlsx",
               "./files/genie.xlsx"]


appended_data = pd.DataFrame()

for name in excel_names:
    pd_data = pd.read_excel(name)
    
    appended_data = pd.concat([appended_data , pd_data],
                              ignore_index=True)
    
appended_data.info

appended_data.to_excel('./files/total.xlsx', index=True)




























