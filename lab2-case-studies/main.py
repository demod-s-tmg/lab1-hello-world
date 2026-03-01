def get_user_query(cursor,search,term): 
    query = f"SELECT * FROM {search} WHERE {term} LIKE ?"
    cursor.execute(query, ('%' + term + '%',))
    results = cursor.fetchall()
    return results