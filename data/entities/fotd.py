from data.database import Database
class Columns:
    def __init__(self):
        self.id = "\"id\""
        self.flavor_id = "\"flavorId\""
        self.date = "\"date\""

    def __getattr__(self, attr):
        return getattr(self, attr)


class FlavorOfTheDayDb(Database):
    def __init__(self):
        self.table_name = "\"FlavorsOfTheDay\""
        self.columns = Columns()
        super().__init__(table_name=self.table_name, columns=self.columns)

