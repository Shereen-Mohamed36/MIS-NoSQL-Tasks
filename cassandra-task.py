from cassandra.cluster import Cluster

# 🔹 Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

print("Connected to Cassandra")

# 🔹 Create Keyspace
session.execute("""
CREATE KEYSPACE IF NOT EXISTS university
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

session.set_keyspace('university')

# 🔹 Create Table (Composite Primary Key)
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

# 🔹 Insert Data (5 rows)
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('CS', 1, 'Ali', 21, 3.2)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('CS', 2, 'Sara', 22, 3.8)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IT', 1, 'Mona', 20, 3.5)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('IT', 2, 'Omar', 23, 2.9)")
session.execute("INSERT INTO students (department, student_id, name, age, grade) VALUES ('AI', 1, 'Youssef', 21, 3.7)")

print("Data inserted")

# 🔹 Update a value
session.execute("""
UPDATE students SET grade = 4.0
WHERE department = 'CS' AND student_id = 1
""")

print("Data updated")

# 🔹 Delete a row
session.execute("""
DELETE FROM students
WHERE department = 'IT' AND student_id = 2
""")

print("Row deleted")

# 🔹 Show data
rows = session.execute("SELECT * FROM students")
for row in rows:
    print(row)