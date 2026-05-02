from neo4j import GraphDatabase

class Neo4jTask:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def session(self):
        return self.driver.session()


uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "mis_project" 
app = Neo4jTask(uri, user, password)

with app.session() as session:
    # 1. Create Graph (Nodes & Relationships) 
    
    session.run("MATCH (n) DETACH DELETE n") 
    
    session.run("""
  
    CREATE (p1:Person {id: 1, name: 'Tom Hanks', age: 67}),
           (p2:Person {id: 2, name: 'Robert De Niro', age: 80}),
           (p3:Person {id: 3, name: 'Robin Wright', age: 58}),
           (p4:Person {id: 4, name: 'Al Pacino', age: 83}),
           (p5:Person {id: 5, name: 'Meryl Streep', age: 74}),
           (p6:Person {id: 6, name: 'Leonardo DiCaprio', age: 49}),

    
    (m1:Movie {title: 'Forrest Gump', year: 1994, genre: 'Drama'}),
    (m2:Movie {title: 'The Godfather Part II', year: 1974, genre: 'Crime'}),
    (m3:Movie {title: 'Cast Away', year: 2000, genre: 'Adventure'}),
    (m4:Movie {title: 'Inception', year: 2010, genre: 'Sci-Fi'}),
    (m5:Movie {title: 'The Devil Wears Prada', year: 2006, genre: 'Comedy'}),

    
    (p1)-[:ACTED_IN {role: 'Forrest'}]->(m1),
    (p3)-[:ACTED_IN {role: 'Jenny Curran'}]->(m1),
    (p1)-[:ACTED_IN {role: 'Chuck Noland'}]->(m3),
    (p2)-[:ACTED_IN {role: 'Vito Corleone'}]->(m2),
    (p4)-[:ACTED_IN {role: 'Michael Corleone'}]->(m2),
    (p6)-[:ACTED_IN {role: 'Cobb'}]->(m4),
    (p5)-[:ACTED_IN {role: 'Miranda Priestly'}]->(m5),
    
  
    (p1)-[:FRIEND_WITH {since: 1990}]->(p2),
    (p2)-[:FRIEND_WITH {since: 1985}]->(p4),
    (p6)-[:FRIEND_WITH {since: 2010}]->(p1)
    """)
    print("1. Graph Created with 6 Persons, 5 Movies, and multiple Relationships!")

    # 2. Delete (Node, Relationship, Property)
    session.run("""
        MATCH (p1:Person {id: 2})-[r:FRIEND_WITH]->(p2:Person {id: 4}) 
        DELETE r
    """)
    session.run("MATCH (p:Person {id: 2}) REMOVE p.age")
    session.run("MATCH (p:Person {id: 2}) DETACH DELETE p")
    print("2. Deleted Property (age) from Leonardo and Node (Robert)")

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
