#!/usr/bin/python3
from sys import argv
import MySQLdb
"""takes in the name of a state
    as an argument and lists all cities of that state"""


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states, cities
                WHERE states.id = cities.state_id and
                states.name = %s ORDER BY cities.id ASC""", (argv[4], ))
    content = cur.fetchall()
    i = 1
    size = len(content)
    for a in content:
        if i != size:
            print('{}, '.format(a[0]), end='')
        else:
            print(a[0])
        i += 1

    print()
    cur.close()
    db.close()
