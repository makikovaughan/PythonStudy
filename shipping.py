#Set the weight
weight = 41.5

#Ground Shipping & Premium Shipping
print("Ground Shipping")
cost_ground = 0.0
cost_drone = 0
if weight <= 2:
  cost_ground = 1.50 * weight + 20.00
  cost_drone = 4.50 * weight
elif weight <= 6:
  cost_ground = 3.00 * weight + 20.00
  cost_drone = 9.00 * weight
elif weight <= 10:
  cost_ground = 4.00 * weight + 20.00
  cost_drone = 12.00 * weight
else :
  cost_ground = 4.75 * weight + 20.00
  cost_drone = 14.25 * weight
print("Weight: ", weight)
print("Cost: $", format(cost_ground, ".2f"))
#Assign the Ground Shipping Premium
cost_premium_ground = 125.00
print("Ground Shipping Premium Cost: $", format(cost_premium_ground, 
".2f"))
print("Drone Shipping")
print("Cost: $", format(cost_drone, ".2f"))


