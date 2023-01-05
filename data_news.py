import requests
import pymysql

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

