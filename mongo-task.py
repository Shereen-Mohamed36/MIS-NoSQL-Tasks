from pymongo import MongoClient
import pprint

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gaming_task']

print("Started MongoDB Task - Part 1")

# 1. Create two collections
player_coll = db.players
game_coll = db.games

# Insert 3 players
player_coll.insert_many([
    {"_id": 1, "name": "Omar Ahmed", "age": 22, "level": "Pro"},
    {"_id": 2, "name": "Ahmed Khaled", "age": 25, "level": "Intermediate"},
    {"_id": 3, "name": "Mariam Hassan", "age": 20, "level": "Beginner"}
])

# Insert 3 games
game_coll.insert_many([
    {"_id": 101, "title": "Valorant", "genre": "FPS", "rating": 9},
    {"_id": 102, "title": "GTA V", "genre": "Open World", "rating": 10},
    {"_id": 103, "title": "Minecraft", "genre": "Sandbox", "rating": 8}
])

print("Created collections and inserted documents")

# 2. Delete one document from each collection
player_coll.delete_one({"_id": 3})
game_coll.delete_one({"_id": 103})
print(" Deleted one document from each collection")

# 3. Add score array to both collections
player_coll.update_many({}, {"$set": {"score": [15, 22, 18]}})
game_coll.update_many({}, {"$set": {"score": [10, 25, 12]}})
print("Added score array")

# 4. Update based on _id condition
for doc in player_coll.find():
    if doc["_id"] == 1:
        player_coll.update_one({"_id": 1}, {"$set": {"score.2": 5}})
        print("Updated player with _id = 1")
    else:
        player_coll.update_one({"_id": doc["_id"]}, {"$set": {"score.3": 6}})

for doc in game_coll.find():
    if doc["_id"] == 101:
        game_coll.update_one({"_id": 101}, {"$set": {"score.2": 5}})
    else:
        game_coll.update_one({"_id": doc["_id"]}, {"$set": {"score.3": 6}})

print("Finished special update based on _id")

# 5. Multiply each element in score array by 20
player_coll.update_many({}, {"$mul": {"score.$[]": 20}})
game_coll.update_many({}, {"$mul": {"score.$[]": 20}})
print("Multiplied all score elements by 20")

print("\n=== Part 2: One-to-Many + Aggregation ===")

# One-to-Many relationship
player_coll.update_one({"_id": 1}, {"$set": {"games": [101, 102]}})
player_coll.update_one({"_id": 2}, {"$set": {"games": [101]}})

# Aggregation to show player with his games
pipeline = [
    {"$lookup": {
        "from": "games",
        "localField": "games",
        "foreignField": "_id",
        "as": "player_games"
    }},
    {"$match": {"_id": 1}}
]

result = list(player_coll.aggregate(pipeline))
pprint.pprint(result[0])

print("\n Task Completed Successfully!")