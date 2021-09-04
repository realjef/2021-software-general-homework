print("Welcome to the dictionary program!")
mydict = {}

while mydict == {}:
    key = input("Please enter a word, or press enter to end: ")
    if key == "":
        break
    translation = input("Please enter the word's translation: " )
    mydict[key] = translation
while mydict != {}:
    key = input("Please enter a word, or press enter to end: ")
    if key == "":
        break
    translation = input("Please enter the word's translation: " )
    mydict[key] = translation
    
if mydict != {}:
    print("Your dictionary: ")
    print(mydict)