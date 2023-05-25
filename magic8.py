#import
import random

#Name of the person who will be asking the Magic 8 - Ball
name = "Makiko"
#name = ""

#Assign the question
question = "Am I going to find a job?"
#question = ""

#Initialize the answer
answer = ""

#Generate a random number between 1 and 9
random_number = random.randint(1, 11)

#print(random_number)

#Assign the answer based on the random_number
if random_number == 1 :
  answer = "Yes - definitely"
elif random_number == 2 :
  answer = "It is decidedly so"
elif random_number == 3 :
  answer = "Without a doubt"
elif random_number == 4 :
  answer = "Reply hazy, try again"
elif random_number == 5 :
  answer = "Ask again later"
elif random_number == 6 :
  answer = "Better not tell you now"
elif random_number == 7 :
  answer = "My sources say no"
elif random_number == 8 :
  answer = "Outlook not so good"
elif random_number == 9 :
  answer = "Very doubtful"
elif random_number == 10 :
  answer = "It is certain"
elif random_number == 11 :
  answer = "Reply hazy, try again"
else :
  answer = "Error"

#Print the question
if question == "" :
    print("No question is provided")
else : 
  if name == "" :
    print("Question: ", question)
  else :
    print(name, " asks: ", question)
  #Print the answer
  print("Magic 8-Ball's answer: ", answer)

