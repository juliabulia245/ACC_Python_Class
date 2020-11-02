#Class 1 Home Practice
'''
changes/features to add:
- allow the user to change the parameters of Waveee through input prompts
- use while loops instead, and maybe add an option where the user can type "exit" at any time during any function to quit the program
'''

import time

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

#Present options
def options():
    print("Here are your options:")
    print("1. Math Muncher: a simple addition program")
    print("2. Waveee: an aesthetic experience")
    print("3. RudeBot: an unfriendly companion")
    print()

#Choose function
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
        elif choice == "list":
            print()
            options()
            choose()
        else:
            print(choice,"wasn't an option! Let's try again...")
            print()
            choose()
    
#Math Muncher function
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

#Waveee function
def waveee():
    time.sleep(1)
    print()
    print("------ Waveee version 1.0 ------")
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

#RudeBot function
def rudebot():
    print()
    print("------ RudeBot version 1.0 ------")
    time.sleep(.5)
    print("Hi, I'm RudeBot. Say something to me, and I'll talk back!")
    time.sleep(1)
    saysomething = input("What do you want to say?")
    time.sleep(1)
    print("Actually, you know what? I don't really want to talk to you right now.")
    end()

#say hi
print("Hi there! I wrote some little functions for class.")
print()
options()

#present choices and collect user input
choose()
                
                  
