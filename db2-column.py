import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'permanent_comments'")

data = []
while True:
    temp = cursor.fetchone()
    if temp:
        data.append(temp)
    else:
        break
print(data)