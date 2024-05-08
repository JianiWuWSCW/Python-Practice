score=0
# Ask the user their name 
name=input("What's your name?")
# Greet the user and introduce the quiz
print("Welcome to the quiz",name)
print("This quiz is about capital cities about the world")
# Ask the user a question
answer=input(" What is the capital city of New Zealand?").upper()
answer=input("What is the biggest city of New Zealand?").upper()
# Tell the user the answer

if answer == "Wellington".upper():
    print("correct!")
    score= score+10
if answer == "Auckland".upper():
    print("correct!")

elif answer =="":
    print("not sure???")
else:
    print("incorrect")
    print("Wellington")

# End the quiz
print("you final score is",score)
input("Goodbye!")
