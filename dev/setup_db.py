import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='db', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

DROP_DB_SQL = '''DROP DATABASE IF EXISTS nestjsrealworld;'''
cursor.execute(DROP_DB_SQL)
CREATE_DB_SQL = '''CREATE database nestjsrealworld'''
cursor.execute(CREATE_DB_SQL)
print("Database 'nestjsrealworld' created successfully........")

conn.close()
