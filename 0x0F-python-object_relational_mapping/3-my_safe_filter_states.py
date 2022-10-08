#!/usr/bin/python3
""" Module safe from SQL injection which takes in an argument
    and display query with all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
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
            cur.execute(""" SELECT * FROM states
                            WHERE name = %s
                            ORDER BY id ASC
                        """, (MY_STATE,))
            row = cur.fetchall()
            for col in row:
                print("{0}".format(col))
        except Exception as e:
            raise
