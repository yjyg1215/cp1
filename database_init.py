import pymysql

###MySQL 연동###
conn=pymysql.connect(
    user="root",
    passwd="",
    host="localhost",
    db="cp1"
)

###데이터베이스 테이블 생성###
cur=conn.cursor()

cur.execute("""CREATE TABLE news_category (
    code INT NOT NULL,
    name VARCHAR(9),

    PRIMARY KEY (code)
);""")

cur.execute("""CREATE TABLE news (
    id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(200),
    image VARCHAR(200),
    title VARCHAR(50),
    leadline VARCHAR(150),
    category INT,
    reporter VARCHAR(10),
    date VARCHAR(10),
    time VARCHAR(5),

    PRIMARY KEY (id),
    FOREIGN KEY (category) REFERENCES news_category(code)
);""")

cur.execute("""CREATE TABLE policy_category (
    code INT NOT NULL,
    name VARCHAR(7),

    PRIMARY KEY (code)
);""")

cur.execute("""CREATE TABLE policy_area (
    code INT NOT NULL,
    name VARCHAR(2),

    PRIMARY KEY (code)
);""")

cur.execute("""CREATE TABLE policy (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    url VARCHAR(200),
    year INT,
    category INT,
    area INT,

    PRIMARY KEY (id),
    FOREIGN KEY (category) REFERENCES policy_category(code),
    FOREIGN KEY (area) REFERENCES policy_area(code)
);""")

cur.execute("""CREATE TABLE store_service (
    code INT NOT NULL,
    name VARCHAR(11),

    PRIMARY KEY (code)
);""")

cur.execute("""CREATE TABLE store (
    id INT NOT NULL AUTO_INCREMENT,
    service INT,
    area VARCHAR(10),
    open INT,
    state INT,
    close INT,
    x FLOAT,
    y FLOAT,

    PRIMARY KEY (id),
    FOREIGN KEY (service) REFERENCES store_service(code)
);""")

cur.execute("""CREATE TABLE sales_service (
    code int NOT NULL,
    name VARCHAR(7),

    PRIMARY KEY (code)
);""")

cur.execute("""CREATE TABLE sales (
    id INT NOT NULL AUTO_INCREMENT,
    year INT,
    quarter INT,
    service INT,
    total_take INT,
    weekday_take INT,
    weekend_take INT,
    total_sales INT,
    weekday_sales INT,
    weekend_sales INT,
    stores INT,

    PRIMARY KEY (id),
    FOREIGN KEY (service) REFERENCES sales_service(code)
);""")

###코드번호를 담을 테이블에 데이터 추가###
cur.execute("""INSERT INTO news_category VALUES (0,'정책');""")
cur.execute("""INSERT INTO news_category VALUES (1,'외식산업');""")
cur.execute("""INSERT INTO news_category VALUES (2,'농수축산');""")
cur.execute("""INSERT INTO news_category VALUES (3,'기획/핫이슈');""")
cur.execute("""INSERT INTO news_category VALUES (4,'Food&Life');""")

cur.execute("""INSERT INTO policy_category VALUES (0,'정책자금');""")
cur.execute("""INSERT INTO policy_category VALUES (1,'성장지원');""")
cur.execute("""INSERT INTO policy_category VALUES (2,'재기지원');""")
cur.execute("""INSERT INTO policy_category VALUES (3,'창업지원');""")
cur.execute("""INSERT INTO policy_category VALUES (4,'전통시장활성화');""")
cur.execute("""INSERT INTO policy_category VALUES (5,'보증지원');""")

cur.execute("""INSERT INTO policy_area VALUES (0,'전국');""")
cur.execute("""INSERT INTO policy_area VALUES (1,'서울');""")
cur.execute("""INSERT INTO policy_area VALUES (2,'강원');""")
cur.execute("""INSERT INTO policy_area VALUES (3,'인천');""")
cur.execute("""INSERT INTO policy_area VALUES (4,'경기');""")
cur.execute("""INSERT INTO policy_area VALUES (5,'대전');""")
cur.execute("""INSERT INTO policy_area VALUES (6,'세종');""")
cur.execute("""INSERT INTO policy_area VALUES (7,'충청');""")
cur.execute("""INSERT INTO policy_area VALUES (8,'대구');""")
cur.execute("""INSERT INTO policy_area VALUES (9,'경북');""")
cur.execute("""INSERT INTO policy_area VALUES (10,'부산');""")
cur.execute("""INSERT INTO policy_area VALUES (11,'울산');""")
cur.execute("""INSERT INTO policy_area VALUES (12,'경남');""")
cur.execute("""INSERT INTO policy_area VALUES (13,'광주');""")
cur.execute("""INSERT INTO policy_area VALUES (14,'전라');""")
cur.execute("""INSERT INTO policy_area VALUES (15,'제주');""")

cur.execute("""INSERT INTO store_service VALUES (0,'제과점영업');""")
cur.execute("""INSERT INTO store_service VALUES (1,'단란주점영업');""")
cur.execute("""INSERT INTO store_service VALUES (2,'관광식당');""")
cur.execute("""INSERT INTO store_service VALUES (3,'관광유흥음식점업');""")
cur.execute("""INSERT INTO store_service VALUES (4,'외국인전용유흥음식점업');""")
cur.execute("""INSERT INTO store_service VALUES (5,'일반음식점');""")
cur.execute("""INSERT INTO store_service VALUES (6,'휴게음식점');""")

cur.execute("""INSERT INTO sales_service VALUES (0,'호프/간이주점');""")
cur.execute("""INSERT INTO sales_service VALUES (1,'한식음식점');""")
cur.execute("""INSERT INTO sales_service VALUES (2,'중식음식점');""")
cur.execute("""INSERT INTO sales_service VALUES (3,'일식음식점');""")
cur.execute("""INSERT INTO sales_service VALUES (4,'양식음식점');""")
cur.execute("""INSERT INTO sales_service VALUES (5,'분식전문점');""")
cur.execute("""INSERT INTO sales_service VALUES (6,'패스트푸드점');""")
cur.execute("""INSERT INTO sales_service VALUES (7,'치킨전문점');""")
cur.execute("""INSERT INTO sales_service VALUES (8,'제과점');""")
cur.execute("""INSERT INTO sales_service VALUES (9,'커피/음료');""")

conn.commit()

conn.close()