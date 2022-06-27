class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes=None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self):
        return f'[{self.package_id}, {self.address}, {self.city}, {self.state}, ' \
               f'{self.zip_code}, {self.deadline}, {self.weight}, {self.notes}]'

    def __repr__(self):
        return f'Package({self.package_id}, {self.address}, {self.city}, {self.state}, ' \
               f'{self.zip_code}, {self.deadline}, {self.weight}, {self.notes})'