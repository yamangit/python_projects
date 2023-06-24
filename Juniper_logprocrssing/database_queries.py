import mysql.connector as sql
from mysql.connector import Error
from mysql.connector import pooling

def InsertData(tablename, data, column):
    query = f"CREATE TABLE IF NOT EXISTS `{tablename}`(id INT AUTO_INCREMENT PRIMARY KEY, {', '.join(f'{k} VARCHAR(255)' for k in column)});"
    cnxpool = pooling.MySQLConnectionPool(
    host='localhost',
    user='root',
    password='strong_password',
    database='mydb',
    pool_name='mypool',
    pool_size=32
    )
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    insert_query = f'INSERT INTO `{tablename}`({", ".join(["`"+k+"`" for k in column])} ) VALUES({",".join(["%s" for i in column])});'
    try:
        cursor.executemany(insert_query, [data])
        cnx.commit()
    except Error as e:
        print("Error while inserting data: ", e)
    finally:
        cursor.close()
        cnx.close()