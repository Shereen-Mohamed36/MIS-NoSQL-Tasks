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
```
1️⃣ 𝙈𝙤𝙣𝙜𝙤𝘿𝘽 𝙏𝙖𝙨𝙠 (𝙇𝙤𝙘𝙖𝙡 𝙄𝙣𝙨𝙩𝙖𝙡𝙡𝙖𝙩𝙞𝙤𝙣)

Setup & Run:
Make sure your MongoDB Service is running locally (default port 27017).

Run Python Script:

```Bash
python mongodb_task.py
```
💻 Shell Commands (Part 2):
To show the One-to-Many relationship using Aggregation in CMD:

Open your terminal and run:
```Bash
mongosh
```
Execute the following commands:

```JavaScript
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
```
2️⃣ 𝑪𝒂𝒔𝒔𝒂𝒏𝒅𝒓𝒂 𝑻𝒂𝒔𝒌

Setup & Run:
Run Cassandra via Docker:

```Bash
docker run --name my-cassandra -p 9042:9042 -d cassandra:3.11
```
Wait about 60 seconds for the container to start.

Run Python Script:

```Bash
python cassandra_task.py
```
💻 Shell Commands (Part 2):
To test Ordering and Materialized Views:

Enter the Cassandra shell:

```Bash
docker exec -it my-cassandra cqlsh
Run these queries:
```
```SQL
USE university;
```
-- Ordering Descending
```
SELECT * FROM students WHERE department = 'CS' ORDER BY student_id DESC;
```
-- Create Materialized View
```
CREATE MATERIALIZED VIEW students_by_grade AS
SELECT * FROM students
WHERE grade IS NOT NULL AND department IS NOT NULL AND student_id IS NOT NULL
PRIMARY KEY (grade, department, student_id);
```
-- Test the View
```
SELECT * FROM students_by_grade WHERE grade > 3.0 ALLOW FILTERING;
```
3️⃣ 𝑵𝒆𝒐4𝒋 𝑻𝒂𝒔𝒌

🔹 Setup & Run
Create a Local DBMS in Neo4j Desktop and click Start.

Run the script:

```Bash
python neo4j_task.py
```
💻 Visualization
Open Neo4j Browser and run:

```Cypher
MATCH (n) RETURN n
```
