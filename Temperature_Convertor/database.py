import sqlite3
from model import TempConv
from typing import List

connection = sqlite3.connect("conversion_log.db")
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS conversions(value REAL, from_unit TEXT, to_unit TEXT, result REAL)")

create_table()

def insert_conversion(conversion: TempConv):
    with connection:
       c.execute("INSERT INTO conversions(value, from_unit, to_unit, result)VALUES(:value, :from_unit, :to_unit, " \
       ":result)",{'value': conversion.value,
                   'from_unit': conversion.from_unit,
                   'to_unit': conversion.to_unit,
                   'result': conversion.result
                   })

def get_all_conversion():
    c.execute("SELECT * FROM conversions")
    result = c.fetchall()
    return [TempConv(*row) for row in result] 