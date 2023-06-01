# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#f_to_c takes Fahrenheit as a parameter and return the Celcius conversion
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5 / 9)
  return c_temp

#Calculate the conversion from 100F to celcius
f100_in_celsius = f_to_c(100)
print("100 Fahrenheit: ", f100_in_celsius)

#c_to_f takes Celcius as a parameter and return the Fahrenheit conversion
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5)) + 32
  return f_temp

#Calculate the conversion from 0 C to Fahrenheit
c0_in_fahrenheit = c_to_f(0)
print("0 Celcius: ", c0_in_fahrenheit)

#get_force takes in mass and acceleration and returns mass * acceleration
def get_force(mass, acceleration):
  return mass * acceleration

#Test the get_force function
train_force = get_force(train_mass, train_acceleration)
print("Force: ", train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Calculate energy: get_energy should return mass multiplied by c squared.
#c's default is 3*10**8
def get_energy(mass, c=3*10**8):
  return mass * (c**2)

#Test get_energy
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) +  " Joules")

#Calculate work defined as force multiplied by distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#Test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + 
str(train_distance) + " meters.")

