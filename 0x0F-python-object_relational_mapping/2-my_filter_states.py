#!/usr/bin/python3
"""takes in an argument and displays all values"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    "Lists tatates from the db"

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    exe = cur.execute("""SELECT * FROM
                      states WHERE name LIKE BINARY
                      "{}" ORDER BY states.id ASC""".format(argv[4]))
    content = cur.fetchall()
    for b in content:
        print(b)
    cur.close()
    db.close()
