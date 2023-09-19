# api de comunicacao com o banco de dados
import sqlite3


# api
def run_sql(instruction, variables=None):
    conn = None
    results = list()
    
    try:
        conn = sqlite3.connect('./database/ssac.db')
        cursor = conn.cursor()
        cursor.execute(instruction)

    except Exception as error:
        print('Execution error')
        print(error)
        print(instruction)
        conn.close()

    else:
        try:
            results = cursor.fetchall()
            conn.commit()
            cursor.close()

        except Exception as error:
            print('Return error')
            print(instruction)
            print(error)

        finally:
            if conn is not None:
                conn.close()

    return results