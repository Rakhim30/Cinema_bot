import sqlite3


def create_read():
    connection = None
    try:
        connection = sqlite3.connect('base.db')
        cursor = connection.cursor()

        table = '''SELECT * FROM SECOND'''
        cursor.execute(table)
        records = cursor.fetchall()
        return records

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return []

    finally:
        if connection:
            connection.close()

def create_ad(kino,name,desc):
    connection=sqlite3.connect('base.db')

    cursor=connection.cursor()

    table='''INSERT INTO FIRST(CINEMA_ID,NAME,DESCRIP) VALUES (?,?,?)'''
    cursor.execute(table,(kino,name,desc))

    connection.commit()
    cursor.close()
    connection.close()

def create_add(kino,name,desc):
    connection=sqlite3.connect('base.db')

    cursor=connection.cursor()

    table='''INSERT INTO SECOND(CINEMA_ID,NAME,DESCRIP) VALUES (?,?,?)'''
    cursor.execute(table,(kino,name,desc))

    connection.commit()
    cursor.close()
    connection.close()



# def create():
#     try:
#         connection=sqlite3.connect('base.db')

#         cursor=connection.cursor()

#         table='''CREATE TABLE SECOND(
#             CINEMA_ID BIGINT NOT NULL,
#             NAME VARCHAR(50) NOT NULL,
#             DESCRIP VARCHAR(50) NOT NULL
#         );'''
#         cursor.execute(table)

#         connection.commit()
#         cursor.close()
#     except (Exception,sqlite3.Error) as eror:
#         print(eror)
#     finally:
#         if connection:
#             connection.close()


def delete(NAME):
    try:
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        add = '''
            DELETE FROM SECOND WHERE NAME = ?
        '''
        cur.execute(add, (NAME,))
        con.commit()
        print('ishladi')
    except (Exception,sqlite3.Error) as er:
        print(er)
    finally:
        if con:
            cur.close()
            con.close()
            print('ilindi')