from random import*
aRandomNumber = randint(1, 20)
i = 0
#print(aRandomNumber)
while i < 3:
    guess = input("Guess a number between 1 and 20 ")
    if not guess.isnumeric():
        print("Please choose a positive whole number")
        i -= 1
    else:
        if int(guess) == aRandomNumber:
            print("That's correct!!")
            i = 6
        elif int(guess) > aRandomNumber:
            print("Sorry, that's too high")
        elif int(guess) < aRandomNumber:
            print("Sorry, that's too low")
    i += 1
print("The number is",aRandomNumber)
#
# from random import*
# aRandomNumber = randint(1, 20)
# i = 0
# for i in range(3):
#     guess = input("Guess a number between 1 and 20 ")
#     if not guess.isnumeric():
#         print("Please choose a positive whole number")
#         i -= 1
#     elif int(guess) == aRandomNumber:
#         print("That's correct!!")
#     elif int(guess) > aRandomNumber:
#         print("Sorry, that's too high")
#     else:
#         print("Sorry, that's too low")
# print("The number is",aRandomNumber)
