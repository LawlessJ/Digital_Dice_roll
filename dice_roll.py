import random
six_sided = [1, 2, 3, 4, 5, 6]
eight_sided = [i for i in range(1,9)]
twelve_sided = [i for i in range(1,13)]
twenty_sided = [i for i in range(1, 21)]
twenty_four_sided = [i for i in range(1,25)]


def roll():
    print("\nWelcome to digital dice roll!")
    valid_answers = ["1","2","3","4","5"]
    while True:
        x = input("\nWhat size dice do you want to roll? Press 1 for 6 sided; press 2 for 8 sided; \npress 3 for 12 sided; press 4 for 20 sided; press 5 for 24 sided.")
        if x not in valid_answers:
            x = input("\nPlease enter a number between 1 and 6.")
        if x == "1":
            dice = six_sided
            break
        if x == "2":
            dice = eight_sided
            break
        if x == "3":
            dice = twelve_sided
            break
        if x == "4":
            dice = twenty_sided
            break
        else:
            dice = twenty_four_sided
            break
        break
        
    value = dice[random.randint(0,dice[-2])]
    print("You rolled a {0}!".format(value))
    while True:
        valid_choices = ["Y", "y", "N", "n"]
        x = input("\nRoll again? Y/N\n")
        if x not in valid_choices:
            x = input("Please enter Y for yes or N for no.\n")
        elif x == "Y" or x == "y":
            value = dice[random.randint(0,dice[-2])]
            print("You rolled a {0}!".format(value))
        else:
            break
    while True:
        answers = ["1", "2"]
        x = input("Would you like to roll another size die or quit? 1:Choose another die 2:Quit")
        if x not in answers:
            print("Please select 1 or 2.")
            continue
        if x == "1":
            roll()
            break
        if x == "2":
            print("See you next time!")
            break
        

roll()

#update code to have options for 6 sided, 8, 12, 20 and 24 sides as an idea
