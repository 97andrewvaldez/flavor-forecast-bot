def generate_select_query(table_name, columns = "*", filters = None):
    where_clause = ""
    if(columns != "*"):
        columns = ", ".join(columns)

    if(filters):
        #filters is a dict with key values as column names and values as values
        where_clause = " WHERE " + " AND ".join([f"\"{key}\" = '{value}'" for key, value in filters.items()])

    return f"SELECT {columns} FROM {table_name} {where_clause}"

def generate_insert_query(table_name, data):
    #data is a dict with key values as column names and values as values
    columns = ", ".join(data.keys())
    values = ", ".join([f"'{value}'" for value in data.values()])

    return f"INSERT INTO {table_name} ({columns}) VALUES ({values}) RETURNING id"

