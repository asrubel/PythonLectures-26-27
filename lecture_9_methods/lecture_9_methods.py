class Ship:
    num = 0

    def __new__(cls, *args, **kwargs):
        if cls.num >= 2:
            raise Exception(f"Ship number {cls.num} already used")
        else:
            cls.num += 1
        print("New ship")
        return object.__new__(cls)

    def __init__(self, name, capacity):
        print("Ship initialized")
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

    def __str__(self):
        # return ("Ship: " + self.name +
        #         " with capacity: " + str(self.capacity) +
        #         ", cargo: " + str(self.cargo) +
        #         ", captain: " + str(self.captain))
        return f"""
                Ship: {self.name}
                Captain: {self.captain}
                Capacity: {self.capacity} tons
                Cargo: {self.cargo} tons"""

    def show_declaration(self):
        print(self)

    def name_captain(self, captain):
        self.captain = captain
        print(f"New captain assigned to this ship: {self.captain}")

    def sail(self):
        print(f"{self.name} is sailing...")

    def load_cargo(self, weight):
        status = f"Loading {weight} tons..."
        if self.cargo + weight > self.capacity:
            print(f"{status} Cannot do that!")
        else:
            self.cargo += weight
            print(f"{status} Done!")

    def unload_cargo(self, weight):
        status = f"Unloading {weight} tons..."
        if self.cargo - weight < 0:
            print(f"{status} Cannot do that!")
        else:
            self.cargo -= weight
            print(f"{status} Done!")

    def __add__(self, other):
        self.load_cargo(other)
        return self

    def __sub__(self, other):
        self.unload_cargo(other)
        return self


ship = Ship("Black Pearl", 100)
ship.name_captain("Jack Sparrow")
ship.show_declaration()
ship.sail()
Ship.sail(ship)

print(ship.capacity)
print(ship.cargo)
ship.load_cargo(90)
ship.show_declaration()
ship.unload_cargo(100)
ship.load_cargo(20)
ship.unload_cargo(60)
ship.show_declaration()

ship = ship + 10
ship.show_declaration()
ship = ship - 5
ship.show_declaration()
ship += 18
ship.show_declaration()
ship -= 1
ship.show_declaration()

ship_2 = Ship("Victory", 200)
ship_2.sail()
print(ship_2)

ship_3 = Ship("Flying Dutch", 150)
ship_3.sail()
print(ship_3)

print(Ship.num)
