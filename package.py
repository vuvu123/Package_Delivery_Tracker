# Package class holds information about the package
# __str__ and __repr__ classes were set up to easily display data on the lookup functions
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes=None, truck=None,
                 status="AT_THE_HUB", time_delivered=None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = truck
        self.status = status
        self.time_delivered = time_delivered

    def __str__(self):
        description = f'Package ID: {self.package_id} | Address: {self.address}, {self.city}, {self.state}, ' \
               f'{self.zip_code} | Deadline: {self.deadline} | Weight: {self.weight} | Note: {self.notes} | ' \
               f'Assigned Truck: {self.truck} | Status: {self.status}'
        if self.time_delivered is not None:
            description += self.time_delivered.strftime('%H:%M:%S')
        return description

    def __repr__(self):
        return f'Package({self.package_id}, {self.address}, {self.city}, {self.state}, ' \
               f'{self.zip_code}, {self.deadline}, {self.weight}, {self.notes}, {self.truck})'
