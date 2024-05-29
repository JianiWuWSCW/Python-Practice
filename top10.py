#------FUNCTIONS ------

BIGGEST_COUNTRIES_ANSWERS=["russia","canada","china","us","brazil","australia","india"]

def intro():
    print("Welcome to the quiz ")
    print("what's your name?")

def getlives():
    while True:
        lives = input("How many chances do you want?")
        try:
            lives=int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a postive number")
        except:
            print("taht wasn't a number")

#------MAIN CODE ------

intro()
lives=getlives

score=0
while lives>0:
    answer=input("Name one of 10 contries in the world:\n").lower()
