import requests
import pymysql

#정책 데이터 수집 함수
def get_policy(url,category):
    response=requests.get(url).json()

    for items in response['item']:
        for item in items['items']:
            if item['title'][1]!='[':
                title=item['title'][1:]
                area=0
            else:
                title=item['title'][6:]
                area=area_code[item['title'][2:4]]
            link=item['url']
            year=int(item['year'][:-1])

            cur.execute("INSERT IGNORE INTO policy(title,url,year,category,area) VALUES (%s,%s,%s,%s,%s);",(title,link,year,category,area))
            conn.commit()

#정책 카테고리별 요청 URL
url_list=["https://www.sbiz.or.kr/sup/policy/json/policyfound.do"
,"https://www.sbiz.or.kr/sup/policy/json/policygrow.do"
,"https://www.sbiz.or.kr/sup/policy/json/policycomeback.do"
,"https://www.sbiz.or.kr/sup/policy/json/policystartup.do"
,"https://www.sbiz.or.kr/sup/policy/json/policymarket.do"
,"https://www.sbiz.or.kr/sup/policy/json/policygrnty.do"]

#지역 코드
area_code={'전국':0,'서울':1,'강원':2,'인천':3,'경기':4,'대전':5,'세종':6,'충청':7,'충북':7,'충남':7,'대구':8,'경북':8,'부산':10,'울산':11,'경남':12,'광주':13,'전라':14,'전북':14,'전남':14,'제주':15}

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

###데이터 수집###
cur=conn.cursor()

for i in range(len(url_list)):
    get_policy(url_list[i],i)

conn.close()