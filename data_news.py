import requests
from bs4 import BeautifulSoup
import pymysql

#뉴스 데이터 수집 함수
def get_news(url,category):
    response=requests.get(url)

    soup=BeautifulSoup(response.text,'html')
    news_list=soup.find('ul',attrs={'class':'type2'})
    
    for news in news_list.find_all('li'):
        a=news.find_all('a')
        em=news.find_all('em')

        link=a[0].attrs['href']
        try:
            image=a[0].find('img').attrs['src']
            title=a[1].text
            leadline=a[2].text[:120]
        except:
            image=""
            title=a[0].text
            leadline=a[1].text[:120]
        reporter=em[1].text
        date=em[2].text.split()[0]
        time=em[2].text.split()[1]

        cur.execute("INSERT IGNORE INTO news(url,image,title,leadline,category,reporter,date,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",(link,image,title,leadline,category,reporter,date,time))
        conn.commit()

#뉴스 카테고리별 요청 URL
url_list=['http://www.foodnews.co.kr/news/articleList.html?sc_sub_section_code=S2N1&view_type=sm',
'http://www.foodnews.co.kr/news/articleList.html?sc_sub_section_code=S2N4&view_type=sm',
'http://www.foodnews.co.kr/news/articleList.html?sc_sub_section_code=S2N5&view_type=sm',
'http://www.foodnews.co.kr/news/articleList.html?sc_sub_section_code=S2N10&view_type=sm',
'http://www.foodnews.co.kr/news/articleList.html?sc_sub_section_code=S2N9&view_type=sm']

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

cur=conn.cursor()

###데이터 수집###
for i in range(len(url_list)):
    get_news(url_list[i],i)

conn.close()