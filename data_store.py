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
        try:
            open=int(row[1]['인허가일자'])
        except:
            open=0
        if row[1]['영업상태구분코드']==3:
            try:
                close=int(row[1]['폐업일자'])
            except:
                close=0
        else:
            close=0
        if na['좌표정보(x)']:
            x=0
        else:
            x=row[1]['좌표정보(x)']
        if na['좌표정보(y)']:
            y=0
        else:
            y=row[1]['좌표정보(y)']

        cur.execute("INSERT IGNORE INTO store(service,area,open,close,x,y) VALUES (%s,%s,%s,%s,%s,%s);",
        (service,area,open,close,x,y))
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