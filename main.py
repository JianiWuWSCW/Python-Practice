play="yes"

score=0


# Ask the user their name 
name=input("What's your name?")
# Greet the user and introduce the quiz
print("Welcome to the quiz",name)
print("This quiz is about capital cities about the world")

# Ask the user a question
while play == "yes":
score=0
answer=input(" What is the capital city of New Zealand?").upper()

# Tell the user the answer
if answer == "Wellington".upper():
    print("correct!")
    score= score+10

elif answer =="":
    print("not sure???")
else:
    print("incorrect")
    print("Wellington")


answer=input("What is the biggest city of New Zealand?").upper()

if answer == "Auckland".upper():
    print("correct!")
    score=score+10

elif answer =="":
    print("not sure???")
else:
    print("incorrect")
    print("Auckland")

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

elif answer =="":
    print("not sure???") 
    print("Wellington")
else:
    print("incorrect")
    print("A")

run = input("Do you want to go to Wellington?")

while run=="yes":
    print("Let's go!")
    run=input("Do you want to go to Wellington?")


# End the quiz

print("Well done {}.You finished the quiz.You final score is{}".format(name,score))
input("Goodbye!") 
# Replay
play = input("Do you want to play again?")
