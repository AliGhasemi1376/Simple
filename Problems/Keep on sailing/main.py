class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self, location):
        return "The {} has sailed for {}!".format(self.name, location)


black_pearl = Ship("Black Pearl", 800)
print(black_pearl.sail(input()))
