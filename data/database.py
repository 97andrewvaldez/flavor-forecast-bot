import psycopg2
import os
from dotenv import load_dotenv
import data.helpers as helpers
class Database:

    def __init__(self, table_name = None, columns = None):
        if(not table_name or not columns):
            self.meta = None
            print("Creating generic db")
        else:
            self.meta = {
                'table_name' : table_name,
                'columns' : columns
            }
            print(f"Creating {self.meta['table_name']} db")

        load_dotenv()
        self.connectionString = os.getenv('DB_CONNECTION')
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            self.connectionString
        )
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()
    
    def __check_cursor(self):
        if not self.cursor:
            raise Exception("Cursor not defined. Unable to use generic method to fetch data.")
    def __check_meta(self, methodName):
        if not self.meta:
            raise Exception(f"Meta not defined. Unable to use generic method {methodName}.")
        
    def __generic_function_checks(self, methodName = ""):
        self.__check_cursor()
        self.__check_meta(methodName)

    def fetch_data(self, filters=None):
        self.__generic_function_checks("fetch_data")
        query = helpers.generate_select_query(self.meta['table_name'], filters=filters)    
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_data(self, table_name, data):
        self.__generic_function_checks("insert_data")
        insert_query = helpers.generate_insert_query(table_name, data)
        try:
            self.cursor.execute(insert_query)
            self.connection.commit()
            return self.cursor.fetchone()[0]

        except Exception as e:
            print(e)
            self.connection.rollback()
    
    def run_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()