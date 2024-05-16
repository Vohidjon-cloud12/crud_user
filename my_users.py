from connect import *

def insertdata():
    connection = connect()
    dbcurser = connection.cursor()
    if connection:
        print("connection already connected insert data") 
        username = input("Enter your username :) ")
        email = input("Enter your email :) ")
        password = input("Enter your password :) ")
        phone = input("Enter your phone :) ")

        query_insert = "insert into crudtable (username, email,password,phone)values(%s,%s,%s,%s)"
        query_value = (username, email, password, phone)

        dbcurser.execute(query_insert, query_value)
        connection.commit()
        print("data inserted succesfully :: ")

        dbcurser.close()
        connection.close()

# ----------------------------------------------------------------

def viewdata():
    connection = connect()
    dbcurser = connection.cursor()
    if connection:
        print("connection successful")
        view = """select * from crudtable;"""
        dbcurser.execute(view)
        row = dbcurser.fetchall()
        for n in row:
            print(n)
        connection.commit()
        dbcurser.close()
        connection.close()


# ----------------------------------------------------------------


def deletedata():
    connection = connect()
    dbcurser = connection.cursor()
    if connection:
        print("connection successful")
        deletedid = input("Deleted data from database at id :) ")
        delete = """delete  from crudtable where id = %s;"""
        query_deleted = (deletedid)
        dbcurser.execute(delete, query_deleted)
        connection.commit()
        print("data deleted succesfully :: ")
        dbcurser.close()
        connection.close()



#----------------------------------------------------------------


def updatedata():
    connection = connect()
    dbcurser = connection.cursor()
    if connection:
        print("connection already connected update data")
        userid = input("user id you want to update :) ")
        username = input("Enter your username :) ")
        email = input("Enter your email :) ")
        password = input("Enter your password :) ")
        phone = input("Enter your phone :) ")
        update = """UPDATE crudtable SET username = %s, email = %s, password = %s, phone = %s WHERE id = %s"""
        query_Newvalue = (username, email, password, phone, userid)

        dbcurser.execute(update, query_Newvalue)
        connection.commit()
        print("data updated succesfully :: ")
        dbcurser.close()
        connection.close()





# ----------------------------------------------------------------
