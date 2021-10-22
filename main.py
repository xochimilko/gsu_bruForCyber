import hashlib
from functions import *

passwordFileName = "password.txt"
saltFileName = "salt.txt"
UIDFileName = "UID.txt"

hash_dictionary = {}
passwordArray = []
saltArray = []
UIDArray = []
passSaltArray = []

passwordArray = convertFiletoArray(passwordFileName)
saltArray = convertFiletoArray(saltFileName)
UIDArray = convertFiletoArray(UIDFileName)

# iterates through UIDArray,SaltArray,PasswordArray
# makes dictionary containing UID and its respective saltedpassword
for i in range(len(UIDArray)):
    userID = UIDArray[i]
    currPassword = passwordArray[i]
    currSalt = saltArray[i]
    passSalt = currPassword + currSalt
    passSaltArray.append(passSalt)
    # print(passSalt)
    hash_dictionary[userID] = getMD5Hash(passSalt)


def verify(guessPass, guessSalt):
    guessPassSalt = guessPass + guessSalt
    guessMF5Hash = getMD5Hash(guessPassSalt)
    for i in hash_dictionary.values():
        if guessMF5Hash == i:
            print("This password and salt are in the database")
            return 0
    print("This password and salt are not in the database")
    return 0


def crack(userID):

    for i in range(0, 1001):
        str1 = f"{i:004}"
        for j in range(0, 101):
            str2 = f"{j:003}"
            sumString = str1 + str2
            guess = getMD5Hash(sumString)
            if hash_dictionary[userID] == guess:
                print(f"userID: {userID} password: {str1} salt: {str2} hash: {guess}")
                return 0


answers = ["001", "054", "022", "060", "061", "080", "081", "003", "004", "010"]
for uid in answers:
    crack(uid)
