from data.database import Database

class Columns:
    def __init__(self):
        self.id = "\"id\""
        self.city = "\"city\""
        self.state = "\"state\""
        self.zip = "\"zip\""

    def __getattr__(self, attr):
        return getattr(self, attr)
    
class RegionDb(Database):
    def __init__(self):
        self.table_name = "\"Region\""
        self.columns = Columns()
        super().__init__(table_name=self.table_name, columns=self.columns)

