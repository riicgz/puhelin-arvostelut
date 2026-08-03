import db

def add_item(title, description, verdict, user_id):
    sql = """INSERT INTO items (title, description, verdict, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, verdict, user_id])