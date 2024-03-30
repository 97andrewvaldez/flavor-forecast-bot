import psycopg2
import data.helpers as helpers
class Database:

    def __init__(self):
        env_vars = helpers.get_env_variables()
        print(env_vars)
        self.dbname = env_vars['DB_NAME']
        self.user = env_vars['USER']
        self.password = env_vars['PASSWORD']
        self.host = env_vars['HOST']
        self.port = env_vars['PORT']
        self.options = env_vars['OPTIONS']
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            "postgresql://postgres:beast1997@localhost:5432/FlavorForecast?options=-csearch_path%3Ddbo,public"
        )
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()
        

with Database() as cursor:
    cursor.execute("SELECT * FROM \"Flavor\"")
    rows = cursor.fetchall()
    for row in rows:
        print(row)