import csv
import psycopg2

conn = psycopg2.connect(dsn='postgres://aspaxqsxuivosj:d2f1cb0ed93f85059fe391019101a9904934907825fb19cc06fdc8261acddf6e@ec2-52-0-155-79.compute-1.amazonaws.com:5432/dfsgi85ac0e0ld')
#カーソルを作成
cursor = conn.cursor()
#もしテーブルが存在しない場合は作成
cursor.execute("CREATE TABLE IF NOT EXISTS temper(a TEXT,b TEXT,c TEXT,d TEXT,e TEXT,f TEXT,g TEXT,h TEXT,i TEXT,j TEXT,k TEXT,l TEXT,m TEXT,n TEXT,o TEXT,p TEXT,q TEXT,r TEXT,s TEXT,t TEXT,u TEXT,v TEXT,w TEXT,x TEXT,y TEXT,z TEXT)")
lastrow = sum(1 for i in open("TEMPerGold/1.csv", "r",encoding="utf-8_sig"))
n=0
with open("TEMPerGold/1.csv", "r",encoding="utf-8_sig") as file:
    rows = csv.reader(file)
    for row in rows:
        n += 1
#最初の行は取り除く
#データの挿入
        if lastrow==n:
            cursor.execute('INSERT INTO temper (a,b) VALUES (%s,%s)', row)
#変更を反映させる
conn.commit()
#中身を確認する
cursor.execute('select * from temper')
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()