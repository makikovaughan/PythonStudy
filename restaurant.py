from datetime import time

# Crete a menu for brunch, early-bird, dinner, and kids.


class Menu:

    # Constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # Representation
    def __repr__(self):
        return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time.strftime("%-I%p"), end_time=self.end_time.strftime("%-I%p"))

    # Calculate total price based on the purchased items
    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return bill

# Create a franchise class


class Franchise:

    # Constructor
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # String representation
    def __repr__(self):
        return "Address: {}".format(self.address)

    # Method takes in a time parameter and returns a list of the Menu objects that are available at that time.
    def available_menus(self, time):

        available_menu = []

        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

# Business Class


class Business:

    # Constructor
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Brunch items
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# Create a bunch menu
brunch = Menu("brunch", brunch_items, time(11, 0, 0, 0), time(16, 0, 0, 0))

# Early bird dinner items
early_dinner_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

# Creaete a early dinner bird
early_bird = Menu("early-bird Dinner", early_dinner_items,
                  time(15, 0, 0, 0), time(18, 0, 0, 0))

# Dinner items
dinner_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

# Create a dinner menu
dinner = Menu("dinner", dinner_items, time(17, 0, 0, 0), time(23, 0, 0, 0))

# Kid's items
kids_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

# Create a kids menu
kids = Menu("kids", kids_items, time(11, 0, 0, 0), time(21, 0, 0, 0))

# Print out brunch info
print(brunch)

# Print out the total order for brunch
print("Total bill is ${}".format(
    brunch.calculate_bill(["pancakes", "home fries", "coffee"])))

# Print out the total order for early-bird dinner
print("Total bill is ${}".format(early_bird.calculate_bill(
    ["salumeria plate", "mushroom ravioli (vegan)"])))

# Creaete a list of Menu objects
menus = [brunch, early_bird, dinner, kids]

# Create the flagship store
flagship_store = Franchise("1232 West End Road", menus)

# Crete new installment
new_installment = Franchise("12 East Mulberry Street", menus)

# Print out available menus at noon
print(flagship_store.available_menus(time(12, 0, 0, 0)))

# Print out available menus at 5pm
print(new_installment.available_menus(time(17, 0, 0, 0)))


# Create a Business class
first_businee = Business("Basta Fazoolin' with my Heart", [
                         flagship_store, new_installment])

# Arepas Menu
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50,
                'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("arepas", arepas_items, time(
    10, 0, 0, 0), time(20, 0, 0, 0))

# Areoas Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create a new Business
arepa_business = Business("Take a' Arepa", [arepas_place])

# Print arepa info
print("Restaurant name: {}\n{}\n{}".format(arepa_business.name,
      arepa_business.franchises[0], arepa_business.franchises[0].menus))
