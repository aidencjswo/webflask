import datetime
import time
import mysql.connector



date = time.localtime()
str = str(date.tm_year)+"/"+str(date.tm_mon)+"/"+str(date.tm_mday)
print(str)
config = {
'user':'aidencjswo',
'password':'1234',
'host':'121.131.135.84',
'port':'3306',
'database':'sample'
}

def select_db_get_achive_fruits():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "select f_name from sample.fruits;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

obj = select_db_get_achive_fruits()

print(obj)