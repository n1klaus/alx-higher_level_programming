#!/usr/bin/python3
""" Module to take in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa.
"""


from sys import argv
import MySQLdb


MY_HOST = "localhost"
MY_PORT = 3306
MY_USER = ""
MY_PASSWORD = ""
MY_DB = ""

if __name__ == "__main__":
    if len(argv) == 5:
        MY_USER = str(argv[1])
        MY_PASSWORD = str(argv[2])
        MY_DB = str(argv[3])
        MY_STATE = str(argv[4])
        try:
            db = MySQLdb.connect(
                                 host=MY_HOST,
                                 port=MY_PORT,
                                 user=MY_USER,
                                 passwd=MY_PASSWORD,
                                 db=MY_DB)
            cur = db.cursor()
            cur.execute(""" SELECT name
                            FROM cities
                            WHERE state_id =
                                (SELECT id
                                 FROM states
                                 WHERE name = %s)
                            ORDER BY id ASC
                        """, (MY_STATE,))
            row = cur.fetchall()
            for col in range(len(row)):
                print("{0}".format(row[col][0]), end="")
                if col < len(row) - 1:
                    print(", ", end="")
            print()
        except Exception as e:
            raise
