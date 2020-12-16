#!/usr/bin/python3
"""takes in the name of a state
    as an argument and lists all cities of that state
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states, cities
                WHERE states.id = cities.state_id and
                states.name = %s ORDER BY cities.id ASC""", (argv[4], ))
    content = cur.fetchall()
    sep = ""
    for row in content:
        for col in row:
            print('{}{}'.format(sep, col), end='')
            sep = ", "
    print()
    cur.close()
    db.close()
