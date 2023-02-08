# 🥩*외식 산업 예비 창업자를 위한 데이터 시각화 및 분석 프로그래밍*🥩

## ✔️*개요*

### 기능

1. 오늘의 뉴스 - 오늘 올라온 외식 산업 관련 뉴스를 한 페이지에 모아서 제공
2. 정책 - 현재 시행되고 있는 정책들을 제공
3. 분석 대시보드 - 신규 및 폐점, 업종별 매출

## ✔️*개발 파이프라인*

<img width="500" alt="스크린샷 2023-02-09 오전 1 47 39" src="https://user-images.githubusercontent.com/62207156/217596195-4aa83a27-51b4-4506-bc8c-6c5a5ba3e950.png">

## ✔️*데이터 스키마*

<img width="580" alt="스크린샷 2023-02-09 오전 1 56 00" src="https://user-images.githubusercontent.com/62207156/217598453-3dadcf32-4120-411d-a938-1ee9ff9f6058.png">

## ✔️*데이터 수집*

1. 뉴스 데이터 수집(웹 크롤링)

<img width="500" alt="스크린샷 2023-02-09 오전 1 53 52" src="https://user-images.githubusercontent.com/62207156/217597881-2fe2def3-62d1-4f67-b400-5c447ed7369c.png">

- 식품저널 사이트의 뉴스 목록을 크롤링
- 예외처리: 대표 이미지가 없는 뉴스가 존재할 수 있으므로 이미지 수집 시 에러가 발생하면 none을 저장하도록 함
- MySQL 연동 후 당일 뉴스만 선별하여 로컬 데이터베이스에 적재
- crontab을 이용하여 매일 9, 12, 15, 18, 21시에 수집을 하도록 스케줄링
<img width="966" alt="image" src="https://user-images.githubusercontent.com/62207156/217597561-910fd5c5-1b80-466a-9755-ac98f6e24534.png">

2. 정책 (Open API)

<img width="335" alt="스크린샷 2023-02-09 오전 1 57 28" src="https://user-images.githubusercontent.com/62207156/217598860-8719fba0-5b0b-4b51-9168-e093eb2d4221.png">

- MySQL 연동 후 현재 시행중인 정책의 정보를 추출해 로컬 데이터베이스에 적재

3. 신규 및 폐점 데이터 (csv파일)
- MySQL 연동 후 신규 및 폐점 정보를 로컬 데이터베이스에 적재
- 약 266만 row의 데이터

4. 업종별 매출 데이터 (csv파일)
- MySQL 연동 후 업종별 매출 정보를 로컬 데이터베이스에 적재

## ✔️*서비스 시연*

### 메인 페이지

<img width="381" alt="스크린샷 2023-02-09 오전 2 01 08" src="https://user-images.githubusercontent.com/62207156/217599869-e49f1eac-7170-4660-92cb-2e0d86fa2a87.png">

→ 세 가지 메뉴를 클릭 할 수 있으며, 각 메뉴를 클릭 할 시 해당 페이지로 이동

### 오늘의 뉴스 페이지

<img width="372" alt="스크린샷 2023-02-09 오전 2 03 06" src="https://user-images.githubusercontent.com/62207156/217600403-e5e24ccb-9ffe-4e4f-ac3c-b13605b371d7.png">

→ DB의 News 테이블 데이터를 불러옴. 이미지, 제목, 줄거리를 클릭하면 해당 뉴스의 원문 페이지로 이동함.

### 정책 페이지

<img width="321" alt="스크린샷 2023-02-09 오전 2 04 27" src="https://user-images.githubusercontent.com/62207156/217600736-d00f1557-e2fd-4195-955d-407c58d14a90.png">

→ DB의 Policy 테이블 데이터를 불러옴. 토글을 클릭하면 해당하는 카테고리의 정책이 등장함. 정책 목록을 클릭하면 해당 정책 정보 페이지로 이동함.

### 분석 대시보드 페이지

<img width="391" alt="스크린샷 2023-02-09 오전 2 05 57" src="https://user-images.githubusercontent.com/62207156/217601084-21b3bf50-d724-4df8-94d8-fe7cc88e0029.png">

→ DB의 store, sales 테이블 데이터를 불러옴. Plotly dash를 통해서 다음과 같은 분석 결과를 보여줌.
- 신규 및 폐점 추이
- 2022 업종별 신규 및 폐점 수
- 2022 지역별 신규 및 폐점 수
- 업종별 평균 매출액(분기 단위)
- 업종별 평균 매출 건 수(분기 단위)

----------------------------
`Python` `HTML` `VSCode` `MySQL` `Flask` `Crontab` `Selenium` `ETL` `Plotly Dash`
