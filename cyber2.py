import hashlib

passwordFileName = "password.txt"
saltFileName = "salt.txt"
UIDFileName = "UID.txt"

hash_dictionary = {}
passwordArray = []
saltArray = []
UIDArray = []
passSaltArray = []


def convertFiletoArray(fileName):
    resultArray = []
    i = 0
    fileObject = open(fileName, "r")
    for fileLine in fileObject:
        # print(i)
        fileLine = fileLine.strip()
        resultArray.append(fileLine)
        i = i + 1
    fileObject.close()
    return resultArray


def getMD5Hash(strA):
    m = hashlib.md5()
    m.update(strA.encode("utf-8"))
    return m.hexdigest()
