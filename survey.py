import json
answers = []
survey = ["What's your name? ", "When is your birthday? (MM/DD/YYYY) ", "How old are you? ", "Where do you live? (City, State, Country) ", "What's your favorite food? ", "What's your favorite color? "]
while True: #can also do for i in range() or while input(continue?) == 'yes'
    print('NEW SURVEY')
    answer = {}
    for q in survey: #Can also put this for loop (including the answer dictionary declaration) into a function(give questions and answers in the parameters)
        answer[q] = input(q)
    #print(answer)
    answers.append(answer)
    print(answers)
    check = input("Would you like to continue collecting data? ")
    if check.lower() == "no":
        break
