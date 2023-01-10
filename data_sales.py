import pandas as pd
import pymysql

#데이터 정제 및 적재 함수
def get_sales(df):
    for row in df.iterrows():
        year=row[1]['기준_년_코드(STDR_YY_CODE_SE)']
        quarter=row[1]['기준_분기_코드(STDR_QU_CODE_SE)']
        service=int(row[1]['서비스업종코드(SVC_INDUTY_CODE_SE)'][-1])
        total_take=row[1]['분기_매출금액(THSMON_SELNG_AMOUNT_AM)']
        weekday_take=row[1]['주중_매출금액(MDWK_SELNG_AMT)']
        weekend_take=row[1]['주말_매출금액(WKEND_SELNG_AMT)']
        total_sales=row[1]['분기_매출건수(THSMON_SELNG_CO)']
        weekday_sales=row[1]['주중_매출건수(MDWK_SELNG_CO)']
        weekend_sales=row[1]['주말_매출건수(WKEND_SELNG_CO)']
        stores=row[1]['점포수(STOR_CO)']

        cur.execute("INSERT IGNORE INTO sales(year,quarter,service,total_take,weekday_take,weekend_take,total_sales,weekday_sales,weekend_sales,stores) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
        (year,quarter,service,total_take,weekday_take,weekend_take,total_sales,weekday_sales,weekend_sales,stores))
        conn.commit()

###csv파일 불러오기###
df=pd.read_csv('sales_csv/블록별 추정매출액.csv',encoding='CP949')

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

cur=conn.cursor()

###데이터 수집###
get_sales(df)

conn.close()