import pymysql
conn=pymysql.connect(host='127.0.0.1', user='root', password='1234', db='soloDB', charset='utf8')
cur=conn.cursor()
cur.execute("create table solodb.usertable_2 (id char(4), userName varchar(15), email char(20), birthYear int);")


cur.execute("insert into usertable values('hong', '홍지훈', 'jihoon@naver.com', '1998');")
cur.execute("insert into usertable values('lee', '이미자', 'jykimpool@naver.com', '1940');")
cur.execute("insert into usertable values('jho', '조용필', 'jykimpool@naver.com', '1950');")
conn.commit()
conn.close()