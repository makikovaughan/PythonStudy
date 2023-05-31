hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", 
"mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Total price of haircuts. Initialize to 0
total_price = 0

#Add all prices in prices list
for price in prices :
  total_price += price

#Calculate the average price
average_price = total_price / len(prices)

#Render the average price
print("Average Haircut Price: ", format(average_price, ".2f"))

#Create a new price list deducted by 5 dollars
new_prices = [price - 5 for price in prices]

#Render the new price list
print("New Price List: ", new_prices)

#Create a total revenue variable and initialize to 0
total_revenue = 0

#Calculate total revenue
for i in range(len(hairstyles)) :
  total_revenue += prices[i] * last_week[i]

#Render the total revenue
print("Total Revenue: " + str(total_revenue))

#Calculate the daily average revenue
average_daily_revenue = total_revenue / 7

#Create a list under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if 
new_prices[i] < 30]

#Render a list under 30 dollors
print("Hairstyles under 30 dollars: ", cuts_under_30)
