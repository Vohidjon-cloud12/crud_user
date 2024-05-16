import psycopg2

dbname = 'n47'
dbpassword = '123'
dbuser = 'postgres'
host = 'localhost'


# ------------

def connect():
    """ python faylimizni n47 nomli database bilan boglovchi funksiya"""
    try:
        connection = psycopg2.connect(
            database=dbname,
            user=dbuser,
            password=dbpassword,
            host=host,
            port='5432')
        return connection
    except (Exception, psycopg2.Error) as e:
        print(e)
        return None
