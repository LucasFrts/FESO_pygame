import sqlite3

def get_connection():
    return sqlite3.connect("./database/game.db")

def insert_ranking(levels, score, finished):
    cursor  = get_connection()
    statement = f"""
        INSERT INTO ranking('levels', 'score', 'finished') values({levels}, {score}, {finished})
    """
    cursor.execute(statement)
    cursor.commit()
    cursor.close()

def get_ranking():
    cursor  = get_connection()
    res = cursor.execute("SELECT * FROM ranking")
    data = res.fetchall()  
    cursor.close()
    return data