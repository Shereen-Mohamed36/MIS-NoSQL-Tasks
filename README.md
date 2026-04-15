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
