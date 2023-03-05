class CityService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, name):
        if name not in self.get_all():
            raise NameError
        return self.dao.get_one(name)

    def create(self, name):
        return self.dao.create(name)

    def update(self, old_name, new_name):
        if old_name not in self.get_all():
            raise NameError
        return self.dao.update(old_name, new_name)

    def delete(self, name):
        return self.dao.delete(name)

    def get_by_last_letter(self, name):
        return self.dao.get_by_last_letter(name[-1].upper())
