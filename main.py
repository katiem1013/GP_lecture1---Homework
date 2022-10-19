word = str(input("Please enter a word: "))

if (len(word) >= 3) & ("ing" not in word):
    print("your word is: " + word + "ing")

elif (len(word) >= 3) & ("ing" in word):
    print("your word is: " + word + "ly")

else:
    print("your word is: " + word)



print("")
print("Hello..." + word)

choice_1 = str(input("You are in a room with three doors, please enter left, right, or forward to choose your door: "))

if choice_1 in "left":
    choice_2 = str(input("You have entered a bedroom, there is a door to the left and one to the right: "))

    if choice_2 in "right":
        print("This is just a wardrobe, it's full of clothes...")
        exit()

    elif choice_2 in "left":
        print("You have entered a bathroom... What else could it have been?")
        exit()

    else:
        exit()

elif choice_1 in "right":
    choice_3 = str(input("You have entered the back garden, you can go left into the woods or right to the pond: "))

    if choice_3 in "right":
        pet_fish = str(input("It is a lovely pond. There is a fish, would you like to pet it? yes or no: "))

        if pet_fish in "yes":
            print(" _________         .    .")
            print("(..       \_    ,  |\  /|")
            print(" \       O  \  /|  \ \/ /")
            print("  \______    \/ |   \  / ")
            print("     vvvv\    \ |   /  |")
            print("     \^^^^  ==   \_/   |")
            print("      `\_   ===    \.  |")
            print("      / /\_   \ /      |")
            print("      |/   \_  \|      /")
            print("            \_________/")
            print("")
            print("...it was a shark...")
            print("...it bites your hand off...")
            exit()

        elif pet_fish in "no":
            print("Your loss.")
            exit()

        else:
            exit()

    elif choice_3 in "left":
        print("You seem to have gotten lost.")
        exit()

    else:
        exit()

elif choice_1 in "forward":
    choice_4 = str(input("You have entered the kitchen, would you like to enter the fridge or the cupboard?"))

    if choice_4 in "fridge":
        print("The fridge is empty.")
        exit()

    elif choice_4 in "cupboard":
        print("The cupboard is empty, you should go shopping...")
        exit()

    else:
        exit()

else:
    exit()