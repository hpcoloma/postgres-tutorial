import psycopg2

#connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursos objuect of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute ('SELECT * FROM "Artist"')

# fetch the results (multiplt)
results = cursos.fetchall()

#fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close

#print results
for result in results:
    print(result)