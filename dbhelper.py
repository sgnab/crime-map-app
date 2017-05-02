
import pymysql
import dbconfig

class DBhelper:
    def connect(self,database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection=self.connect()

        try:
            query="SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.excute(query)
            return cursor.fetchall()
        finally:
            connection.close()



    def addinput(self):
        connection = self.connect()

        try:
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.excute(query)
                connection.commit()
        finally:
            connection.close()



    def clearinput(self):
        connection = self.connect()

        try:
            query ="DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.excute(query)
                connection.commit()
        finally:
            connection.close()

