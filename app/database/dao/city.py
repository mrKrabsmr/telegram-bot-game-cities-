from sqlalchemy import insert


class CityDAO:
    def __init__(self, conn, cities):
        self.conn = conn
        self.cities = cities

    def get_all(self):
        return self.conn.execute(self.cities.select())

    def get_one(self, name):
        return self.conn.execute(self.cities.select().where(self.cities.c.name == name))

    def create(self, crname):
        self.conn.execute(insert(self.cities).values(name=crname))
        self.conn.commit()

    def update(self, old_name, new_name):
        self.conn.execute(self.cities.update().where(self.cities.c.name == old_name)).values(name=new_name)
        self.conn.commit()

    def delete(self, name):
        self.conn.execute(self.cities.delete().where(self.cities.c.name == name))
        self.conn.commit()

    def get_by_last_letter(self, letter):
        return self.conn.execute(self.cities.select().where(self.cities.c.name.like(letter+'%')))

