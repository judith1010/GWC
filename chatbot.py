import random

# --- Define your functions below! ---
def greet():
    print("---------------------------------------")
    greetings = ["Howdy!", "Hey, there!", "Hello!", "Hey man.", "What's poppin' Jimbo?"]
    print(random.choice(greetings))
    name = input("What's your name?")

    print("Hello %s! My name is Sally!" %name)

def feeling():
    feelings = ["happy!", "tired.", "just peachy!", "hungry!!!!!!", "quite fine"]
    compfeels = random.choice(feelings)
    stories = ["When the coder who coded this was walking to Morgan Stanley the other day, she totally got Regina Georged.", "WHAT IF I TOLD YOU I STOLE A CARDBOARD CUTOUT OF DANNY DEVITO?", "Once upon a time  group of adevnturers went on an adventure to the fridge, they returned with cookies and milk. The end."]
    randomstories = random.choice(stories)
    feel = input("How are you feeling this fine afternoon?")
    if feel.lower() == "good":
        print("So glad to hear that! I'm feeling", compfeels)
    elif feel.lower() == "bad":
        story = input("I'm so sorry to hear that! Would you like for me to tell you a story to make you feel better? y/n: ")
        if story.lower() == "y" or story.lower() == "yes":
            print(randomstories)
        elif story.lower() == "n" or story.lower() == "no":
            print("Okay, I hope you feel better soon.")
        else:
            print("SALLY DOES NOT UNDERSTAND SALLY GOES HOME NOW.")

    else:
        print("Yeah, me too.")
def talk():
    randomfoods = ["Good choice! My favorite food is mac and cheese!", "I hate mayonnaise", "Soda makes my keys sticky", "Water makes me short circuit"]
    foodopinion = random.choice(randomfoods)
    topic = input("What do you want to talk about? ")
    topic = topic.lower()
    if topic == "food":
        print(foodopinion)
    elif topic == "colors":
        color =input("What's your favorite color? ")
        if color.lower() == "blue":
            print("I also love blue! Especially the blue sky")
        else:
            print("Nice!")
    elif topic == 'music':
        genre = input("What music do you like? ")
        genre = genre.lower()
        if genre == "pop":
            print("Same! I like Billie Eilish and Ed Sheeran!")
        elif genre == "alternative":
            print("Cool! I like Panic! At the Disco and the 1975!")
        else:
            ("Me too!")
    else:
        print("Sounds cool!")

# --- Put your main program below! ---
def main():
    greet()
    feeling()
    while True:
        talk()



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
