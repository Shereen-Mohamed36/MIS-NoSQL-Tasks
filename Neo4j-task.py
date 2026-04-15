from neo4j import GraphDatabase

class Neo4jTask:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.session() as session:
            session.run(query, parameters)

    def session(self):
        return self.driver.session()


uri = "bolt://localhost:7687"
user = "shereen"
password = "12345678" 
app = Neo4jTask(uri, user, password)

with app.session() as session:
    # 1. Create Graph (Nodes & Relationships)
   
    session.run("""
    CREATE (p1:Person {id: 1, name: 'Tom Hanks', age: 67}),
           (p2:Person {id: 2, name: 'Robert De Niro', age: 80}),
           (m1:Movie {title: 'Forrest Gump', year: 1994}),
           (p1)-[:ACTED_IN {role: 'Forrest'}]->(m1)
    """)
    print("1. Graph Created (Nodes & Relationships)")

    # 2. Delete (Node, Relationship, Property)
    session.run("MATCH (p:Person {name: 'Robert De Niro'}) REMOVE p.age")

    session.run("MATCH (p:Person {id: 2}) DETACH DELETE p")
    print("2. Deleted Property (age) and Node (Robert)")

    # 3. Update (Properties)
    
    session.run("MATCH (m:Movie {title: 'Forrest Gump'}) SET m.year = 1995")
    session.run("MATCH (:Person {name: 'Tom Hanks'})-[r:ACTED_IN]->(:Movie) SET r.role = 'Forrest Gump Junior'")
    print("3. Updated Movie year and Relationship role")

    # 4. Find Nodes based on condition
    print("\n4. Finding Nodes (People older than 60):")
    result = session.run("MATCH (p:Person) WHERE p.age > 60 RETURN p.name, p.age")
    for record in result:
        print(f"Name: {record['p.name']}, Age: {record['p.age']}")

    # 5. Find Relationships based on condition
    print("\n5. Finding Relationships (Roles starting with 'Forrest'):")
    result = session.run("MATCH (p)-[r:ACTED_IN]->(m) WHERE r.role STARTS WITH 'Forrest' RETURN p.name, r.role, m.title")
    for record in result:
        print(f"{record['p.name']} played {record['r.role']} in {record['m.title']}")

app.close()