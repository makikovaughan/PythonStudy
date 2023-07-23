import json
import csv

# A list of users whose passwords have been compromised
compromised_users = []

# Open up the file itself. Store it in a file object called password_file.
with open("passwords.csv") as password_file:
    # Pass the password_file object holder to our CSV reader for parsing and save it to password_csv
    password_csv = csv.DictReader(password_file)

    # Add the compromised users to the list
    for password_row in password_csv:
        # print(password_row["Username"])
        compromised_users.append(password_row["Username"])

# Write the compromised users to compromised_users.txt
with open("compromised_users.txt", "w") as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)


boss_message = {"recipient": "The Boss", "message": "Mission Success"}

# Open a new JSON file to write data
with open("boss_message.json", "w") as boss_message_dict:
    json.dump(boss_message, boss_message_dict)

# Create a new password file
with open("new_passwords.csv", "w") as new_passwords_obj:

    # Save the signature
    slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

    # Write slash_null_sig to the new password file
    new_passwords_obj.write(slash_null_sig)
