import sqlite3

con = sqlite3.connect("sample.db")

cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE films
    (released text, title text, budget real)
"""
)

con.commit()
con.close()

