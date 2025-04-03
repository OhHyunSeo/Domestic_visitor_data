# 🧭 Domestic Visitor Data Analysis

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

## 🔍 소개

**Domestic Visitor Data Analysis** 프로젝트는 국내 관광 데이터 및 미디어 순위 데이터를 수집, 병합, 전처리하고  
시각화를 통해 방문자 수 및 트렌드를 분석하는 데이터 기반 프로젝트입니다.

---

## 🛠️ 주요 기능

- 🎵 Melon, Bugs, Genie 크롤링 및 통합
- 📹 YouTube 데이터 수집 및 비교 분석
- 📊 엑셀 기반 데이터 전처리 및 병합
- 📈 시각화 결과 도출 (막대그래프, 라인플롯 등)

---

## 📁 프로젝트 구조

```
📁 Domestic_visitor_data-master/
│
├── 📄 1_0_bs_selenium.py               # Selenium 및 BeautifulSoup 기반 기본 크롤링
├── 📄 1_1_Melon_Crawling.py           # Melon 사이트 데이터 수집
├── 📄 1_2_Bugs_Crawling.py            # Bugs 사이트 데이터 수집
├── 📄 1_3_Genie_Crawling.py           # Genie 사이트 데이터 수집
├── 📄 1_4_Excel_Merge.py              # 수집한 데이터를 엑셀 파일로 병합
├── 📄 2_youtube.py                    # 유튜브 관련 데이터 수집 및 처리
├── 📄 2_youtube_vs.py                 # 유튜브 VS 경쟁 분석 혹은 비교 시각화
├── 📄 3_1_data_preprocessing_multi_xls.py  # 엑셀 여러 파일 전처리
└── 📄 3_2_visualaization.py           # 시각화 및 그래프 출력
```

---

## 🚀 실행 방법

### 1. 가상환경 설정 및 패키지 설치

```bash
python -m venv venv
source venv/bin/activate  # 윈도우: venv\Scripts\activate
pip install -r requirements.txt  # 필요시 생성
```

### 2. 스크립트 실행 순서

1. `1_0_bs_selenium.py` → 웹 크롤링 셋업
2. `1_1~1_3_*.py` → Melon, Bugs, Genie 크롤링
3. `1_4_Excel_Merge.py` → 데이터 통합
4. `3_1_data_preprocessing_multi_xls.py` → 전처리
5. `3_2_visualaization.py` → 시각화 결과 생성

---

## 🧑‍💻 기여 방법

1. 이 레포지토리를 포크하세요.
2. 새로운 브랜치를 생성하세요: `git checkout -b feature/기능명`
3. 변경사항을 커밋하세요: `git commit -m "Add 기능"`
4. 브랜치에 푸시하세요: `git push origin feature/기능명`
5. Pull Request를 생성하세요.

