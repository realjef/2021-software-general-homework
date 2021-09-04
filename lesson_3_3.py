print("Welcome to the dictionary program!")
fortnite = "bad"
mydict = {}
key = ""
translation = ""
keylist = []
while fortnite == "bad":
#Input OG Word
    key = input("Enter a word or hit enter to end:")
    if key == "":
        break
    if key in keylist:
        print("Duplicate Key")
        break
    keylist.append(key)
    if " " in key:
        print("Error")
        break
#Input Translation
    translation = input("Enter the Translation: ")
    mydict[key] = translation
sentence = input("Enter a sentence: ")
sentence1 = sentence.split(" ")
for i in range(0, len(sentence1)):
    replacement = sentence1[i]
    if replacement in mydict:
        sentence1[i] = mydict[replacement]
translatedsentence = " ".join(sentence1)
print(translatedsentence)
print(mydict)