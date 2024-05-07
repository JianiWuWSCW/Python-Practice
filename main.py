# Ask the user their name 
name=input("What's your name?")
# Greet the user and introduce the quiz
print("Welcome to the quiz",name)
print("This quiz is about capital cities about the world")
# Ask the user a question
answer=input(" What is the capital city of New Zealand?")
# Tell the user the answer
if answer == "Wellington":
    print("correct")
elif answer =="":
    print("not sure???")
else:
    print("incorrect")

print("Wellington")
# End the quiz
input("Goodbye!")
