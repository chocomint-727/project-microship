import psycopg2

import psqlConfig as config

class DataSource:
    def __init__(self):
        '''Constructor that initiates connection to database '''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def get_all_anime(self):
        ''' Outputs the entire dataset - currently only includes two columns: title and score '''
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM anime_table")
        records = cursor.fetchall()
        print(records)
        
    def get_score_from_title(self, type):
        ''' Gets score of Anime title input by user '''
        try:
            cursor = self.connection.cursor()
            query = "SELECT score FROM anime_table WHERE anime_title = %s;"
            cursor.execute(query, (type,))
            print(cursor.fetchall())

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
    def get_title_from_score(self, type):
        ''' Gets titles that  match with score input by user. Returns a list of titles '''
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM anime_table WHERE score = %s;"
            cursor.execute(query, (type,))
            print(cursor.fetchall())

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
    def filter(self, g):
        cursor = self.connection.cursor()
        
        if type(g) == list:
            query = f"select * from anime_table where lower(genres) like '%{g[0]}%'"
            for gen in g[1:]:
                query += f"and lower(genres) like '%{gen}%'"
            query += ";"
        elif g is None:
            query = "select * from anime_table;"
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        return results
