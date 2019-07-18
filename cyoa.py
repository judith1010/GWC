name = input("Welcome to East High School!I heard you're the new student! My name is Candace! What is your name?" )
print("Hi", name)
print( "Here at East High we take pride in our variety of clubs! We have book club, cheerleading, and computer science club!")
club = input("Which of these would you like to participate in?")
print(f"Great choice! I'm signing up for {club} too!")
if club == "book club":
    print(f"Candace: Ohhhh~ Here comes Ben! He's the president of book club! He's so smart and cute >.< uwu. \n*Ben enters* Hey guys! Welcome to book club. *faces you* Haven't seen you around? What's your name? \n*blushes* My name is {name} ")
    print("Ben: We already had our first meeting. If you give me your number, we can work out a time for me to catch you up on what you missed. *winks*")
    answer = input("*thinks* Should I give him my number? Yes or No?")
    while answer != "Yes" and answer != "No":
        print("Idiot. It's a Yes or No question!")
        answer = input("*thinks* Should I give him my number? Yes or No? ")
    if answer == "No":
        print("Ok. I won't give you my number.")
        print("Ben: Oh Ok bye. :( *leaves*")
    else :
        print("Ok sure. Here's my number!")
        print("Ben: Great. See you later! *winks and leaves*")
if club == "cheerleading":
    print(f"Candace: Wow! First day of cheer practice was crazy! Oh snap here are the football players! \n candace: Look! It's Mitch the quarterback! He's coming our way! \n *Mitch enters* How you girls doing? *looks at you* Haven't seen you around? \n I'm {name}. Nice to meet you! \n Mitch: Wanna go out to the movies tonight?")
    answer = input("*thinks* Should I go to the movies with him? Yes or No?")
    while answer != "Yes" and answer != "No":
        print("Idiot. It's a Yes or No question!")
        answer = input("*thinks* Should I go to the movies with him? Yes or No?")
    if answer == "No":
        print("I'll pass *flips hair* but thanks. \n *Candace faints* \n Mitch: damn ok. *ego deflates*")
    else :
        print("Sure why not? \n Mitch: Great. See you later! *winks and leaves*")
if club == "computer science":
    print(f"Candace: Oh look. Here comes Eric. He knows so many coding languages that they made him president when he was a freshman! *fawns* \n *enters Eric* Hi I'm Eric. Welcome to Computer Science club. Nice to meet you {name}. \n You: How do you know my name? \n Eric: I do background checks on everyone who joins my club. I can see we have a lot in common. Went to get some coffee later?")
    answer = input("*thinks* Should I get coffee with him? Yes or No?")
    while answer != "Yes" and answer != "No":
        print("Idiot. It's a Yes or No question!")
        answer = input("*thinks* Should I get coffee with him? Yes or No?")
    if answer == "No":
        print("Um no thanks. You're kinda creepy. *leaves*")
    else :
        print("Oh I'm so flattered. Sure! \n Eric   : Great. See you later! *winks and leaves*")
