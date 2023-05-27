#Create tuples
my_info = ("Mike", 24, "Programmer")

#Print out
print(my_info)
print(my_info[0])
print(my_info[-1])

#Do not do this. Causes a type error
# my_info[0] = "Michael"

#List of dog owners
owners = ["Jenny", "Alexus", "Sam", "Grace"]

#List of dog names
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

#Combine owners and dog_names
names_and_dogs_names = zip(owners, dogs_names)

#Print out(Tuples)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
