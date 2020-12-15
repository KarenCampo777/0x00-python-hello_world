#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name = %s
                ORDER BY states.id ASC""", (argv[4], ))

    content = cur.fetchall()
    for c in content:
        print(c)
    cur.close()
    db.close()
