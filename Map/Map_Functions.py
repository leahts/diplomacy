import mysql.connector

def create_sql_db(username, password):
    sql_db = mysql.connector.connect(
    user = username,
    password = password,
    database = "diplomacy_map_data"
    )
    return sql_db