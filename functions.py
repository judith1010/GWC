# --- Define your functions below! ---
def greeting():
    print("Hey there! \nI'm chat bot!")
    name = input("What's your name? ")
    print(f"Hi {name}!\nIt's nice to meet you!")

def addition(num1, num2):
    print("I can add those numbers together!")
    answer = int(num1) + int(num2)
    print(f"{num1} + {num2} = {answer}")

def feelingToday(feeling):
    feeling.lower()
    if feeling == 'good':
        print("Glad to hear! Me too.")
    elif feeling == 'bad':
        help = input("I'm sorry. Is there anything I can do to help?")
        help.lower()
        if help == 'no':
            print("Ok. I hope things get better soon.")
        else:
            print("I was only being polite. I'm a computer. There's not really much I can do ;)")
    else:
        print("Yeah, me too")
def trick():
    see = input("Wanna see a cool trick? ")
    if see.lower() == 'yes':
        num1 = input("Pick a number: ")
        num2 = input("Pick another one: ")
        addition(num1, num2)
    elif see.lower() == 'no':
        print("Ok then. You're missing out.")
    else:
        print("Sorry I didn't catch that")


# --- Put your main program below! ---
def main():
    greeting()
    while True:
    #answer = input("(What will you say?) ")
    #print("That's cool!")
        feeling = input("How are you today? ")
        feelingToday(feeling)
        trick()

# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":
    main()
