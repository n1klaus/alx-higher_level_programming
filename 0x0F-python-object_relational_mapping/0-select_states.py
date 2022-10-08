#!/usr/bin/python3
""" Module to query states table in hbtn_0e_0_usa and sort by id. """


from sys import argv
import MySQLdb


MY_HOST = "localhost"
MY_PORT = 3306
MY_USER = ""
MY_PASSWORD = ""
MY_DB = ""

if __name__ == "__main__":
    if len(argv) == 4:
        MY_USER = str(argv[1])
        MY_PASSWORD = str(argv[2])
        MY_DB = str(argv[3])
        try:
            db = MySQLdb.connect(
                                 host=MY_HOST,
                                 port=MY_PORT,
                                 user=MY_USER,
                                 passwd=MY_PASSWORD,
                                 db=MY_DB)
            cur = db.cursor()
            cur.execute(""" SELECT * FROM states ORDER BY id ASC """)
            row = cur.fetchall()
            for col in row:
                print("{0}".format(col))
        except Exception as e:
            raise
