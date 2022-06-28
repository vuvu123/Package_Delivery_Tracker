class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.start_time = None
        self.current_time = None
        self.finish_time = None
        self.speed = 0.3

    def insert(self, package):
        self.packages.append(package)
        self.route.append(package[1])

    def remove(self, package):
        self.packages.remove(package)
        self.route.remove(package[1])


truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


