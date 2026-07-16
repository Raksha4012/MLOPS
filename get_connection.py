from sql_connection import get_connection
def execution(query):
    connection = sql_connection
    if connection is None:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
            result=cursor.fetchall()
        else:
            connection.commit()
            result=cursor.rowcount
        return result
    except Exception as e:
        print("sql error")
        print(e)
        return None
    finally:
        cursor.close()