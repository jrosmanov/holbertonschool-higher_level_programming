#!/usr/bin/python3
"""type"""
import MySQLdb
import sys


if __name__ == "__main__":

    usrnm = sys.argv[1]
    psswrd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=usrnm,
        password=psswrd,
        database=db_name)

    cursor = db.cursor()

    sql = ("SELECT cities.id, cities.name, states.name FROM cities "
           "JOIN states ON states.id = cities.state_id "
           "ORDER BY cities.id ASC;")

    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
