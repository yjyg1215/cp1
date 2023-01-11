from flask import Flask,render_template
import pandas as pd
import pymysql
import dash 
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output 
import plotly.express as px 

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

cur=conn.cursor()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'),200

@app.route('/news')
def news():
    cur.execute("""
    SELECT n.url,n.image ,n.title ,n.leadline ,c.name,n.reporter ,n.`date` ,n.`time`
    FROM news as n, news_category as c
    WHERE n.category = c.code ;
    """)
    news_list=cur.fetchall()
    news_df=pd.DataFrame(news_list,columns=['url','image','title','leadline','category','reporter','date','time'])

    return render_template('news.html',news=news_df),200

@app.route('/policy')
def policy():
    def get_policy(code):
        cur.execute("""
        SELECT p.title ,p.url ,p.`year` ,c.name ,a.name 
        FROM policy as p, policy_area as a, policy_category as c
        WHERE p.area =a.code and p.category =c.code and p.category=
        """+code+" ORDER BY p.`year` DESC,p.area;")
        policy_list=cur.fetchall()
        policy_df=pd.DataFrame(policy_list,columns=['title','url','year','category','area'])

        return policy_df

    p0=get_policy('0')
    p1=get_policy('1')
    p2=get_policy('2')
    p3=get_policy('3')
    p4=get_policy('4')
    p5=get_policy('5')

    return render_template('policy.html',p0=p0,p1=p1,p2=p2,p3=p3,p4=p4,p5=p5),200

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html'),200

dash_app=dash.Dash(
    __name__,
    server=app,
    url_base_pathname='/dashboard/'
)

dash_app.title="외식 산업 창업 Helper"

cur.execute("""SELECT ss.name ,s.area ,s.open_y ,s.open_m ,s.close_y ,s.close_m 
FROM store s, store_service ss
WHERE s.service =ss.code ;""")
df=cur.fetchall()
df=pd.DataFrame(df,columns=['service','area','open_y','open_m','close_y','close_m'])

open_y=df.groupby('open_y').count().sort_index(ascending=False)[:20]
open_y=open_y['area']
close_y=df.groupby('close_y').count().sort_index(ascending=False)[1:21]
close_y=close_y['service']
fig1_df=pd.concat([open_y,close_y],axis=1)
fig1_df.rename(columns={'area':'신규','service':'폐점'},inplace=True)
fig1=px.line(fig1_df,x=fig1_df.index,y=['신규','폐점'],title='신규 및 폐점 추이')

open_ser=df.groupby(['service','open_y']).count().sort_index(ascending=False).reset_index()
open_ser=open_ser[open_ser['open_y']==2022][['service','close_y']]
close_ser=df.groupby(['service','close_y']).count().sort_index(ascending=False).reset_index()
close_ser=close_ser[close_ser['close_y']==2022][['service','area']]
fig2_df=pd.merge(open_ser,close_ser,how='inner')
fig2_df.rename(columns={'close_y':'신규','area':'폐점'},inplace=True)
fig2=px.bar(fig2_df,x='service',y=['신규','폐점'],barmode='stack',title='2022 업종별 신규 및 폐점 수')

open_a=df.groupby(['area','open_y']).count().sort_index(ascending=False).reset_index()
open_a=open_a[open_a['open_y']==2022][['area','close_y']]
close_a=df.groupby(['area','close_y']).count().sort_index(ascending=False).reset_index()
close_a=close_a[close_a['close_y']==2022][['area','open_y']]
fig3_df=pd.merge(open_a,close_a,how='inner')
fig3_df.rename(columns={'close_y':'신규','open_y':'폐점'},inplace=True)
fig3=px.bar(fig3_df,x='area',y=['신규','폐점'],barmode='stack',title='2022 지역별 신규 및 폐점 수')


cur.execute("""SELECT s.`year` ,s.quarter ,ss.name ,s.total_take ,s.total_sales
FROM sales s,sales_service ss 
WHERE s.service =ss.code ;""")
df2=cur.fetchall()
df2=pd.DataFrame(df2,columns=['year','quarter','service','total_take','total_sales'])

df2_mean=df2.groupby('service')['total_take','total_sales'].mean()
fig4=px.bar(df2_mean,x=df2_mean.index,y='total_take',title='업종별 평균 매출액(분기 단위)')

fig5=px.bar(df2_mean,x=df2_mean.index,y='total_sales',title='업종별 평균 매출 건수(분기 단위)')

dash_app.layout=html.Div([
    html.H1('분석 대시보드',style={"text-align": "center"}),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),

])

if __name__=='__main__':
    app.run()