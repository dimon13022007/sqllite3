import sqlite3
import requests
from bs4 import BeautifulSoup as Borsch
import datetime





connection = sqlite3.connect('ddd.sl3', 5) #5-timeout
cur = connection.cursor()



url = requests.get('https://ua.sinoptik.ua/погода-київ/')
sup = Borsch(url.content, 'html.parser')

for el in sup.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    print(t_min)
    cur.execute("INSERT INTO third_table (temperature) VALUES (?)", (t_min,))
time = datetime.datetime.now()

cur.execute("CREATE TABLE third_table (date TEXT, temperature TEXT);")
cur.execute("INSERT INTO third_table (date) VALUES ('Nick');")
cur.execute("INSERT INTO third_table (date) VALUES  (?)", (time,))
cur.execute("INSERT INTO third_table (temperature) VALUES ('Nick');")
cur.execute("SELECT rowid, temperature FROM third_table;")
res = cur.fetchall()
print(res)
connection.commit()
# print(connection)
# print(cur)
connection.close()





