# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/15
"""

import MySQLdb as sql


def read_image():
    fin = open("woman.PNG")
    img = fin.read()

    return img


def writeImage(data):
    fout = open('woman2.PNG', 'wb')

    with fout:
        fout.write(data)

conn = sql.Connect(host='localhost', user='root', passwd='root', db='mytest', port=3306)
with conn:
    cur = conn.cursor()
    # cur.execute("DROP TABLE IF EXISTS Writers")
    # cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(25))")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

    # cur.execute("SELECT * FROM Writers")

    # rows = cur.fetchall()
    # for row in rows:
    #     print row

    # for i in range(cur.rowcount):
    #     row = cur.fetchone()
    #     print row[0], row[1]

    # rows = cur.fetchall()
    # desc = cur.description
    # print desc[0][0],'--',desc[1][0]



    # cur.execute("CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB)")
    data = read_image()
    cur.execute("INSERT INTO Images VALUES(1, %s)", (data,))

    # cur.execute("SELECT Data FROM Images WHERE Id=1")
    # data = cur.fetchone()[0]
    # writeImage(data)