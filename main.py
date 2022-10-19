word = str(input("Please enter a word: "))

if (len(word) >= 3) & ("ing" not in word):
    print(word + "ing")

if (len(word) >= 3) & ("ing" in word):
    print(word + "ly")

else:
    print(word)