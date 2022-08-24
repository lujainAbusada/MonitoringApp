import mysql.connector as mysql
import wrapper

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def CheckTableSize(cursor,table,limit):

    cursor.execute("SELECT COUNT(*) FROM " + table)
    count = cursor.fetchone()
    if (int(count[0]) > limit):
       query=("DELETE FROM `" + table + "`ORDER BY time LIMIT 1")
       cursor.execute(query)

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def StoreUsage(db,values,query,table,limit):

    cursor = db.cursor()
    CheckTableSize(cursor,table,limit)
    cursor.execute(query, values)
    db.commit()

