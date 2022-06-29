class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getprice(self):
        return self.price

    def __str__(self):
        return self.name + ' --> ' + str(self.getprice())


# Defining a function for building a Menu
# which generates list of Food
def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu


# items
names = ["Veg Briyani","Chicken Briyani","Mutton Briyani","Fish Briyani","Prawn Briyani","Beef Briyani","65 Briyani"]

# prices
costs = [80, 150, 180,200,220,190,240]

# building food menu
Foods = buildmenu(names, costs)

n = 1
for el in Foods:
    print(n, '. ', el)
    n = n + 1