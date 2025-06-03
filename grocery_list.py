# setup_db.py

import sqlite3

groceries = sorted([
    "apples", "bananas", "clemintines", "dill", "eggs", "flour", "granola", "honey",
    "ice cream", "juice", "ketchup", "lemon", "margarine", "onion", "potatoes",
    "rosmary", "salt", "thyme", "vinegar", "watermelon", "pears", "cucumbers",
    "garlic", "carrots", "pastries", "eggplants", "milk", "coffee", "tea", "rice",
    "noodles", "lentils", "sweet potatoes", "strawberries", "cranberries", "mangos",
    "pappers", "zuccinis", "lime", "broth", "mushrooms", "chicken", "beef", "pork",
    "fish", "cream", "paprika", "tumeric", "cinamon", "pumpkin", "basil", "tomatoes",
    "bread", "cake", "chocolate", "gum", "pinapple", "oranges", "lettuce", "cheese", "cilantro"
])

def setup_database(db_path="grocery_list.db"):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS groceries")
    cursor.execute("CREATE TABLE groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

    for item in groceries:
        cursor.execute("INSERT INTO groceries (name) VALUES (?)", [item])

    connection.commit()
    connection.close()
    print(f"✅ Database '{db_path}' initialized with {len(groceries)} items.")

if __name__ == "__main__":
    setup_database()
