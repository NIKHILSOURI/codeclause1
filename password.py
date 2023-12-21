import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

passwordLength = int(input("How long would you like your password to be? "))

newPassword = []
for x in range(passwordLength):

    newPassword.append(random.choice(characters))

finalPassword = ''.join(map(str, newPassword))

print("\n This is your new password: ", finalPassword)
