from data.database import Database
class Columns:
    def __init__(self): 
        self.id = "\"id\""
        self.name = "\"name\""
        self.description = "\"date\""
        self.url = "\"url\""
        self.fotd_url = "\"flavorOfDayUrl\""
        self.region_id = "\"regionId\""
        self.date_added = "\"dateAdded\""

    def __getattr__(self, attr):
        return getattr(self, attr)
    

class RestaurantDb(Database):
    def __init__(self):
        self.table_name = "\"Restaurant\""
        self.columns = Columns()
        super().__init__(table_name=self.table_name, columns=self.columns)

