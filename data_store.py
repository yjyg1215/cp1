import pandas as pd
import pymysql

#데이터 정제 및 적재 함수
def get_store(df,service):
    for row in df.iterrows():
        na=row[1].isnull()
        if na['소재지전체주소']:
            continue
        else:
            area=row[1]['소재지전체주소'][:2]
        if na['인허가일자']:
            open_y=0
            open_m=0
        else:
            open_y=row[1]['인허가일자']//10000
            open_m=row[1]['인허가일자']//100-(row[1]['인허가일자']//10000)*100  
        if row[1]['영업상태구분코드']==3:
            if na['폐업일자']:
                close_y=0
                close_m=0
            else:
                close_y=row[1]['폐업일자']//10000
                close_m=row[1]['폐업일자']//100-(row[1]['폐업일자']//10000)*100
        else:
            close_y=0
            close_m=0

        cur.execute("INSERT IGNORE INTO store(service,area,open_y,open_m,close_y,close_m) VALUES (%s,%s,%s,%s,%s,%s);",
        (service,area,open_y,open_m,close_y,close_m))
        conn.commit()

###csv파일 불러오기###
df1=pd.read_csv('store_csv/fulldata_07_22_18_P_제과점영업.csv',encoding='CP949')
df2=pd.read_csv('store_csv/fulldata_07_23_01_P_단란주점영업.csv',encoding='CP949')
df3=pd.read_csv('store_csv/fulldata_07_24_01_P_관광식당.csv',encoding='CP949')
df4=pd.read_csv('store_csv/fulldata_07_24_02_P_관광유흥음식점업.csv',encoding='CP949')
df5=pd.read_csv('store_csv/fulldata_07_24_03_P_외국인전용유흥음식점업.csv',encoding='CP949')
df6=pd.read_csv('store_csv/fulldata_07_24_04_P_일반음식점.csv',encoding='CP949')
df7=pd.read_csv('store_csv/fulldata_07_24_05_P_휴게음식점.csv',encoding='CP949')

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

cur=conn.cursor()

###데이터 적재###
get_store(df1,0)
get_store(df2,1)
get_store(df3,2)
get_store(df4,3)
get_store(df5,4)
get_store(df6,5)
get_store(df7,6)

conn.close()