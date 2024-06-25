play="yes"

score=0
GOOD_COMMENTS = ["Way to go!","Keep it up!","Fantastic!"]
BAD_COMMENTS = ["Keep trying","Maybe next time","Don't give up"]

# Ask the user their name 
name=input("What's your name?")
# Greet the user and introduce the quiz
print("Welcome to the quiz",name)
print("This quiz is about capital cities about the world")

import random

while True:
    try:

        tries=input("How many tries do you want for the questions? ")
        tries=int(tries) 
        
        break
    except:
        print("That's not a number")
    
    
    
# Ask the user a question
while play == "yes":
    score=0
    answer=input(" What is the capital city of New Zealand?").upper()

    # Tell the user the answer
    if answer == "Wellington".upper():
        print("correct!")
        score= score+10
        print(GOOD_COMMENTS[0])

    elif answer =="":
        print("not sure???")
        print(BAD_COMMENTS[0])
    else:
        print("incorrect")
        print("Wellington")
        print(BAD_COMMENTS[2])


    answer=input("What is the biggest city of New Zealand?").upper()

    if answer == "Auckland".upper():
        print("correct!")
        score=score+10
        print(GOOD_COMMENTS[2])

    elif answer =="":
        print("not sure???")
        print(BAD_COMMENTS[0])
    else:
        print("incorrect")
        print("Auckland")
        print(BAD_COMMENTS[2])


    QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
    question = "What is the capital city of New Zealand?"
    a= "Wellington"
    b= "London"
    c= "Auckland"
    d= "Beijing"
    answer= input(QUESTION_FORMAT.format(question,a,b,c,d)).lower()

    if answer == "a".lower() or answer==a.lower():
        print("correct!")
        score=score+10
        print(GOOD_COMMENTS[2])

    elif answer =="":
        print("not sure???") 
        print("Wellington")
        print(BAD_COMMENTS[0])
    else:
        print("incorrect")
        print("A")
        print(BAD_COMMENTS[1])
    
   

    print("Well done {}.You finished the quiz.You final score is{}".format(name,score))
    play = input("Do you want to do this quiz again?")



# End the quiz

print("Goodbye!") 