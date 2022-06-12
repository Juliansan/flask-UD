import psycopg2


conn = psycopg2.connect(dbname='example', user='postgres', password='Juli1984')

cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS table2;
''')

cur.execute('''
CREATE TABLE table2(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False 
);
''')

# There are two types on passing variables to a SQL command

# Passing parameters in a tupple
cur.execute("INSERT INTO table2 (id, completed) VALUES (%s, %s);", (1, True))

# Passing parameters as a dict

SQL = "INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);"

data = {
    'id': 2,
    'completed': False
}

cur.execute(SQL, data)

conn.commit()

cur.execute("SELECT * FROM table2;")

print('fetchmany', cur.fetchmany(1))
print('fetchone', cur.fetchone())

cur.close()
conn.close()
