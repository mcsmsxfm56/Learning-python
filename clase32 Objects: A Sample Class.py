class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):#constructor
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print(dir(an))#dir prints the methods of the class

#FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and 
#more

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)