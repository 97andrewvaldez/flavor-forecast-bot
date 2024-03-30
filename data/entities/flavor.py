from data.database import Database

meta = {
    'table_name' : '\"Flavor\"',
    'columns' : {
        'id': "\"id\"",
        'name': "\"name\"",
        'description': "\"description\"",
        'date_added': "\"dateAdded\"",
        'restaurant_id': "\"restaurantId\"",
    }
}
class Columns:

    def __init__(self):
        self.id = "\"id\""
        self.name = "\"name\""
        self.description = "\"description\""
        self.date_added = "\"dateAdded\""
        self.restaurant_id = "\"restaurantId\""
    
    def __getattr__(self, attr):
        return getattr(self, attr)
    

class FlavorDb(Database):
    def __init__(self):
        self.table_name = "\"Flavor\""
        self.columns = Columns()
        super().__init__(table_name=self.table_name, columns=self.columns)
