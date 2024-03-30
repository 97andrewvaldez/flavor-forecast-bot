import data.entities.region as region
import data.entities.flavor as flavor
import data.entities.fotd as fotd
import data.entities.restaurant as restaurant
import data.database as database

with region.RegionDb() as conn:
    data = conn.fetch_data()
    for row in data:
        print(row)

with flavor.FlavorDb() as conn:
    data = conn.fetch_data()
    for row in data:
        print(row)

with fotd.FlavorOfTheDayDb() as conn:
    data = conn.fetch_data()
    for row in data:
        print(row)

with restaurant.RestaurantDb() as conn:
    data = conn.fetch_data()
    print(data)

with database.Database() as conn:
    data = conn.run_query("SELECT * FROM \"Flavor\"")
    print(data)
