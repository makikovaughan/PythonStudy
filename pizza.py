# Your code below:
#Topping list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", 
"anchovies", "mushrooms"]

#Price list
prices = [2, 6, 1, 3, 2, 7, 2]

#Count $2 slices
num_two_dollar_slices = prices.count(2)
print("Number of Two Dollor Slices: ", num_two_dollar_slices)

#Length of toppings
num_pizzas = len(toppings)

#Render
print("We sell " + str(num_pizzas) + " differnt kinds of pizza!, where " + 
str(num_pizzas) + " represents the value of our vairable num_pizzas")

#List containing prices and toppings
pizza_and_prices = [[prices[0], toppings[0]], [prices[1], toppings[1]], 
[prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], 
toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]]]
print("Pizza Prices and Toppings: ", pizza_and_prices)

#Sort pizza_and_prices by price(ascending)
pizza_and_prices.sort()

#Cheapest pizza
cheapest_pizza = pizza_and_prices[0]

#Most expensive pizza
priciest_pizza = pizza_and_prices[-1]

#Remove anchovies(most expensive)
pizza_and_prices.pop()

#Add peppers
pizza_and_prices.insert(4, [2.5, "peppers"])

#Get the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]

print("The three cheapest pizzas: " + str(three_cheapest))
