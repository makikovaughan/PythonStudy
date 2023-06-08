letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Combine to a list of letters and points
letter_to_points = {key:value for key, value in zip(letters, points)}

#Add the key, " " and value, 0
letter_to_points[" "] = 0

#score_word will take in a word and return how many points that word is worth.
def score_word(word):
  total_point = 0
  for letter in word:
    total_point += letter_to_points.get(letter.upper(), 0)
  return total_point

brownie_points = score_word("BROWNIE")
print("brownie_points : ", brownie_points)

# player_to_words maps players to a list of the words they have played.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


#Use for loop to get the total score of each player
#Return the result
def update_point_totals(): 
  #Add the total points of each player
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    #Use another for loop to get a total score of words
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

#Prints the player and its words
def render_player_to_words():
    for player, words in player_to_words.items():
        print("********************************************************************")
        print("Player: {player} \n Words: {words}".format(player=player, words=words))


#Prints the player and its points
def render_player_to_points():
    for player, point in player_to_points.items():
        print("********************************************************************")
        print("Player: {player} \n Points: {point}".format(player=player, point=point))



player_to_points = update_point_totals()
render_player_to_points()

# a function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
  if player in player_to_points:
    player_to_words[player].append(word)
  else:
    print("{} does not exist. Please try again".format(player))

#Add more word
play_word("player1", "hahaha")
render_player_to_words()

#Update the total points
player_to_points = update_point_totals()
render_player_to_points()

