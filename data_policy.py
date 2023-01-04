import requests
import pymysql

#정책 데이터 수집 함수
def get_policy(url,code):
    response=requests.get(url)



#정책 카테고리별 요청 URL
url=["https://www.sbiz.or.kr/sup/policy/json/policyfound.do"
,"https://www.sbiz.or.kr/sup/policy/json/policygrow.do"
,"https://www.sbiz.or.kr/sup/policy/json/policycomeback.do"
,"https://www.sbiz.or.kr/sup/policy/json/policystartup.do"
,"https://www.sbiz.or.kr/sup/policy/json/policymarket.do"
,"https://www.sbiz.or.kr/sup/policy/json/policygrnty.do"]

#데이터 수집
for i in range(len(url)):
    get_policy(url[i],i)