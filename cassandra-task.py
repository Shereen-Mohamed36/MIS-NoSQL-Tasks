from gevent import monkey
monkey.patch_all()

from cassandra.cluster import Cluster

#  Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

print("Connected to Cassandra")

#  Create Keyspace
session.execute("""
CREATE KEYSPACE IF NOT EXISTS university
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

session.set_keyspace('university')

#  Create Table (Composite Primary Key)
session.execute("""
CREATE TABLE IF NOT EXISTS students (
    department TEXT,
    student_id INT,
    name TEXT,
    age INT,
    grade FLOAT,
    PRIMARY KEY (department, student_id)
)
""")

print("Table created")

#  Insert Data (8 rows)
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('CS', 1, 'Ali', 21, 3.2)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('CS', 2, 'Sara', 22, 3.8)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IT', 3, 'Mona', 20, 3.5)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IT', 4, 'Omar', 23, 2.9)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('AI', 5, 'Youssef', 21, 3.7)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IS', 6, 'Ahmed', 21, 3.8)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IS', 7, 'Ola', 20, 3.3)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IS', 8, 'Eman', 21, 2.5)")

print("Data inserted")

#  Update a value
session.execute("""
UPDATE students SET grade = 4.0
WHERE department = 'CS' AND student_id = 1
""")

print("Data updated")

#  Delete a row
session.execute("""
DELETE FROM students
WHERE department = 'IT' AND student_id = 2
""")

print("Row deleted")

#  Show data
rows = session.execute("SELECT * FROM students")
for row in rows:
    print(row)

session.shutdown()
print("Connection closed")