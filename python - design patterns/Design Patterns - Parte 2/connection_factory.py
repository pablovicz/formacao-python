#conceitual code
import MySQLdb


#parecido com o Builder, porém aqui a gente nao tem controle na criacao do objeto
class ConnectionFactory(object):

    def get_connection():
        connection = MySQLdb.connect(
            host="localhost",
            user='root',
            password='',
            db='alura'
        )

        return connection


