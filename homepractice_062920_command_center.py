#Class 2 Home Practice
#Command Center v1.0
'''
changes/features to add:
- add an option where the user can type "exit" at any time during any function to quit the program (use while loop?)
'''

'''
Printing commands - range, character count, etc
Variable type - print(type(x))
Converting numbers - i.e. str, int, float
True/False statements - i.e. 10 > 9, 10 ==9, 10 < 9
Formatting input to printing text - i.e. "My favorite colors are {}, {}, and {}!!!"
'''

#imports
import time
import random

#end - close the program
def end():
    time.sleep(1)
    print()
    whatnext = input("Want to try another function? (Type y for yes, n for no)")
    if whatnext == "y":
        print()
        choose()
    elif whatnext == "n":
        time.sleep(.5)
        print("Alright... see you next time!")
    else:
        print("I didn't quite catch that... try again!")
        end()

#options - display available options
def options():
    print("Here are the mini-programs available to you:")
    print("1. Math Muncher: a simple addition program (no changes since last upload)")
    print("2. Waveee: an aesthetic experience (no changes since last upload)")
    print("3. RudeBot: an unfriendly companion *UPDATED*")
    print("4. Anna Graham: an anagram scrambler with no internal vocabulary *NEW!*")
    print()

#choose
def choose():
    #collect user input to choose a function to run
        choice = input("Type the number of the function you'd like to run,\nor type 'list' to see the list of options again: ")
        if choice == "1":
            print("You chose Math Muncher! Get ready to crush some simple math!")
            mathmuncher()
        elif choice == "2":
            print("You chose Waveee! Get ready for a wild ride!")
            waveee()
        elif choice == "3":
            print("You chose RudeBot! This should be interesting...")
            rudebot()
        elif choice == "4":
            print("You chose Anna Graham - things are about to get scrambly!")
            anagram()
        elif choice == "list":
            print()
            options()
            choose()
        else:
            print(choice,"wasn't an option! Let's try again...")
            print()
            choose()
    
#Math Muncher v1.0
#to do: add error handling for non-numeric input values
def mathmuncher():
    print()
    print("------ Math Muncher version 1.0 ------")
    time.sleep(.5)
    print("I'm going to ask you to enter a couple of numbers to add together magically.")
    time.sleep(.5)
    
    #Get first number from the user
    num1 = input("Enter 1st number: ")
    
    #Convert text entered to a floating point number
    num1 = float(num1)

    #Get second number from the user
    num2 = input("Enter 2nd number: ")

    #Convert text entered to a floating point number
    num2 = float(num2)

    #Add and display the numbers
    result = num1+num2
    time.sleep(.5)
    print("Hmm...")
    time.sleep(1)
    print("Let me think about that...")
    time.sleep(1.5)
    print("...")
    time.sleep(.75)
    print("Oh! I've got it!")
    time.sleep(1)
    print("That was easy! The answer is",result)
    end()

'''
to do: allow the user to change the parameters of Waveee through input prompts
'''
#Waveee v1.0
def waveee():
    print()
    print("------ Waveee version 1.0 ------")
    time.sleep(.5)
    i = 0
    speed = 6.5
    size = 32
    slope = 1
    repetitions = 1
    while i < repetitions:
        n = 1
        while n < size:
            print("." * n)
            time.sleep(1/(n*speed))
            n += slope
        while n > 0:
            print("." * n)
            time.sleep(1/(n*speed))
            n -= slope
        i += 1
    print()
    time.sleep(1)
    print("Wow, that was fun!")
    time.sleep(1)
    print("I'm getting a little dizzy...")
    end()

'''
- expand RudeBot's capabilities
        - many similar concepts to the UBI/SNAP game, so maybe not
        - topics to choose from: colors, animals, technology, politics, etc. (search the input string for any of these, maybe in order of RudeBot's preferences? whichever is found first gets discussed)
        - RudeBot is randomly assigned preferences on the above and will criticize you if yours don't match. If they do match, he's still rude and says something condescending like, "wow, I'm surprised someone like you likes cats."
        - secret easter egg command to see behind the scenes (nerd reference like "Do a barrel roll!" or "I am your father" or something) and view RudeBot's preferences. Make it uncomfortable for the bot. ARGGHHH!
'''

#RudeBot v1.1
def rudebot():
    topics = ["animals","politics","food","music"]
    #create topics and fill them with example items
    animals = ["rhinocerous","flamingo","cardinal","cat","dog","elephant","hamster"]
    politics = ["Joe Biden","Bernie Sanders","Donald Trump"]
    food = ["pizza","ice cream","tacos","pasta","potato chips"]
    music = ["Radiohead","Coldplay","Taylor Swift","Drake","Cardi B","Eminem","The Lumineers","Shawn Mendes"]
    topics = ", ".join(topics)
    print()
    print("------ RudeBot version 1.1 (2020-06-28) ------")
    time.sleep(.5)
    print("Hi, I'm RudeBot. Say something to me, and I'll talk back!")
    time.sleep(.5)
    print("I only know how to talk about a few things right now.")
    time.sleep(.5)
    print("Here's what I can talk about:",topics)
    selection = input("What do you want to talk about? ")
    time.sleep(.5)
    #listed in order of RudeBot's hard-coded preference to talk about them
    if selection in topics:
        print("Yes, let's talk about "+selection+".")
        if selection == "animals":
            userfavorite = input("What is your favorite animal? ")
        elif selection == "politics":
            userfavorite = input("Who do you want to win the 2020 election? ")
        elif selection == "food":
            userfavorite = input("What is your favorite food? ")
        elif selection == "music":
            userfavorite = input("Who is your favorite musician? ")
        #assign RudeBot's preference randomly
        botfavorite = random.choice(selection) #this is currently choosing from the word selection lol
        if userfavorite == botfavorite:
            print("I like",botfavorite,"too!")
        else:
            print("Are you serious?",botfavorite,"is the best.")
    else:
        print("I already told you, I don't know how to talk about "+selection+".")
        time.sleep(1)
        print("Please go away.")
    end()

#Anna Graham
'''
Note: storing the letters perhaps removes some of the true randomness because list.remove() removes the first instance of a letter, as opposed to removing it at its chosen position
To do: make it re-run the anagram loops if result == source... needs an exception if the string is only one character!
'''

def anagram():
    print()
    print("------ Anna Graham version 1.0 (2020-06-28) ------")
    time.sleep(.5)
    print("Hi, my name is Anna Graham, and I'm here to scramble your name!")
    print()
    time.sleep(.5)
    source = input("Type your first/given name (or someone else's name): ")
    time.sleep(.5)
    #convert to string
    source = str(source)
    #remove extra spaces 
    source = source.strip()
    #convert to lowercase
    source = source.lower()
    length = len(source)
    #set a counter & an empty list of available positions
    i = 0
    positions = []
    #place each position in a list
    while i < length:
        positions.append(source[i])
        i += 1
    #fill the result one character at a time with random selections from the source characters
    result = []
    i = 0
    while i < length:
        current = random.choice(positions)
        result.append(current)
        positions.remove(current)
        i += 1
    result = "".join(result)
    time.sleep(.5)
    print("Hmmm...")
    time.sleep(1)
    print("Are you sure your name isn't",result[0].upper()+result[1:]+"?")
    end()    

#welcome message
print("------ Command Center version 1.0 ------")
print("Hello, and welcome to the Command Center!")
print()
options()

#display choices and collect user input
choose()
                
                  
