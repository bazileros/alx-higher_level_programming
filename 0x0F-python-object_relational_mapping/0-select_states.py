#!/usr/bin/python3
"""
    lists all states from the database hbtn_0e_0_usa in ascending ORDER
    Usage: ./0-select_states.py <username> <password> <database>
"""

import MySQLdb as sql
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        with sql.connect(user=username, passwd=password, db=database) as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
                states = cursor.fetchall()
                for state in states:
                    print(state)
    except sql.Error as e:
        print(f"❌ Error: {e}")
