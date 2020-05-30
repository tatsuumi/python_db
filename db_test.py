import psycopg2

# connect postgreSQL
conn = psycopg2.connect(host='ec2-52-0-155-79.compute-1.amazonaws.com', dbname='dfsgi85ac0e0ld', user='aspaxqsxuivosj', password='d2f1cb0ed93f85059fe391019101a9904934907825fb19cc06fdc8261acddf6e', port='5432')
# もしくは
conn = psycopg2.connect(dsn='postgres://aspaxqsxuivosj:d2f1cb0ed93f85059fe391019101a9904934907825fb19cc06fdc8261acddf6e@ec2-52-0-155-79.compute-1.amazonaws.com:5432/dfsgi85ac0e0ld')
# excexute sql
cur = conn.cursor()
cur.execute('SELECT * FROM people;')
results = cur.fetchall()

#output result
print(results)

cur.close()
conn.close()