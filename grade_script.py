last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], 
["architecture", 65]]

# Your code below: 

#List of subjects I am taking
subjects = ["physics", "calculus", "poetry", "history"]

#List of test scores
grades = [98, 97, 85, 88]

#Combine subjects and grades
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], 
[subjects[2], grades[2]], [subjects[3], grades[3]]]

print("Initial Current Grade Book")
print(gradebook)

#Add a new score
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#Add 5 to visual arts
gradebook[-1][-1] += 5

#Remove the score for poetry class
gradebook[2].remove(85)

#Append Pass to the poetry class
gradebook[2].append("Pass")

#Create a list to hold the previous and current semester
full_gradebook = last_semester_gradebook + gradebook

print("Grade book for both previous and current semester")
print(full_gradebook)


