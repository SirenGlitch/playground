password = "wh@t!nTh£$hi78a1ls"  # input("Enter a password")

lettersInPassword = []

crackedPassword = []

possibleChars = [""]
possibleChars.extend("asdfghjklqwertyuiopzxcvbnm")  # Lower case
possibleChars.extend("ASDFGHJKLQWERTYUIOPZXCVBNM")  # Upper case
possibleChars.extend("1234567890")  # Numbers
possibleChars.extend("!$£%^&*@#?.()-")  # Specials
# print(possibleChars)

for letter in range(0, len(password)):
    savedLetter = password[letter : letter + 1]
    lettersInPassword.append(savedLetter)

for letter in lettersInPassword:
    for char in possibleChars:
        if char == letter:
            crackedPassword.append(char)
            break
        if char != letter:
            continue

print(
    *crackedPassword
)  # Can't be asked to fix the spaces between them, just deal with it
