# 🚀 NoSQL Database Tasks (MongoDB, Cassandra, Neo4j)

This repository contains the implementation for three NoSQL database tasks. It covers connecting via Python drivers, performing CRUD operations, and executing specific Shell/CMD commands.

---

## 🛠️ Prerequisites (What to install?)

* **Python 3.x**
* **MongoDB Community Server & Compass** (Local installation).
* **Docker Desktop** (Specifically for running Cassandra).
* **Neo4j Desktop**.

### Required Python Libraries:
```bash
pip install pymongo cassandra-driver neo4j

1️⃣ MongoDB Task (Local Installation)
Setup & Run:
Make sure your MongoDB Service is running locally (default port 27017).

Run Python Script:

Bash
python mongodb_task.py
💻 Shell Commands (Part 2):
To show the One-to-Many relationship using Aggregation in CMD:

Open your terminal and run:

Bash
mongosh
Execute the following commands:

JavaScript
use gaming_task;
db.players.aggregate([
  {
    $lookup: {
      from: "games",
      localField: "games",
      foreignField: "_id",
      as: "player_games_details"
    }
  }
]).pretty();
2️⃣ Cassandra Task (Docker)
Setup & Run:
Run Cassandra via Docker:

Bash
docker run --name my-cassandra -p 9042:9042 -d cassandra:3.11
Wait about 60 seconds for the container to start.

Run Python Script:

Bash
python cassandra_task.py
💻 Shell Commands (Part 2):
To test Ordering and Materialized Views:

Enter the Cassandra shell:

Bash
docker exec -it my-cassandra cqlsh
Run these queries:

SQL
USE university;

-- Ordering Descending
SELECT * FROM students WHERE department = 'CS' ORDER BY student_id DESC;

-- Create Materialized View
CREATE MATERIALIZED VIEW students_by_grade AS
SELECT * FROM students
WHERE grade IS NOT NULL AND department IS NOT NULL AND student_id IS NOT NULL
PRIMARY KEY (grade, department, student_id);

-- Test the View
SELECT * FROM students_by_grade WHERE grade > 3.0 ALLOW FILTERING;
3️⃣ Neo4j Task
Setup & Run:
Open Neo4j Desktop, create a Local DBMS, and click Start.

Run Python Script:

Bash
python neo4j_task.py
💻 Verification (Visualization):
Open Neo4j Browser.

Run:

Cypher
MATCH (n) RETURN n
📝 Important Notes:
Cassandra: Version 3.11 is used for Materialized View compatibility.
