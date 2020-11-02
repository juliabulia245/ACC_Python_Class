# WEDNESDAY, JUL 1 2020

#For your reference:
    #TEST YOUR MEMORY:
    #How do you write a piece of code simply asking the user for their name, and then saying "Hi, name" ?
'''
#long way
print("Good evening. What is your name?")
variable = input('Enter your name: ') 
print("Hello, " + variable)

#shorthand
name = input('What is your name?\n')
print ('Hi, %s.' % name)
'''
####################################
#Homework:
    #Why the extra punctuation?
    #What does it mean?
    #What if you replace 's' with another letter?
'''
Julia's Answer:
    % is an operator you can use to format variables.
    %s means the variable will be formatted as a string.
    The second % precedes the name of the variable that will be formatted.
      e.g., the following line of code formats the variable 'name' as a string
      print ('Hi, %s.' % name)
    If you replace s with another letter in this specific example, you will likely get an error, because many of the other formats require numbers, not strings
    There are other letters that allow you to format variables as integers (d), floating point numbers (f), etc.
'''    
####################################


#For your reference:
    #while loop: execute a set of statements as long as a condition is true
    #Print i as long as i is less than 6
'''
i = 1
while i < 6:
  print(i)
  i += 1
''' 
#increment i, or loop will continue forever (not good)

####################################
#Homework:
    #Why the letter 'i'?
    #Why the '+-'?
    #What does it mean?
    #What happens if you replace 'i' with another letter?
'''
Julia's Answer:
    Rumor has it, this stands for "iteration," but a brief Internet search also yielded the following:
      - it relates back to conventions used in the days of Fortran, where integer variables had to begin with letters i - n.
      - the above may have possibly come from the mathematical use of i for matrix indexes
      - the above may have possibly come from Rene Descartes, who also purportedly popularized the use of a, b, and c for known variables and x, y, and z for unknowns
    The += in the code above increments i by 1.
    += is an addition assignment operator, which sets the value of whatever is to the left of the operator equal to its value plus the value of whatever is to the right of the operator.
    In other words, x += y is equivalent to x = x + y. In the specific example above, it sets i equal to i + 1, more easily understood in this context as incrementing by 1.
    You can replace i with whatever letter or valid variable name you'd like, as long as it's consistent everywhere it appears in the code (in this case, four times).
''' 
####################################

'''
#For your reference:
    #math.ceil()
        #rounds a num up to nearest int
    #math.floor()
        #rounds a num down to nearest int

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) #returns 2
print(y) #returns 1
'''

######################################
#Homework:
    #What happens if you don't enter a decimal? i.e. 10?
    #What happens if I enter a number typed out? i.e. ten?
'''
Julia's Answer:
    If you enter an integer, e.g. 10, you will get that integer as the result
      Why? Because math.ceil() and math.floor() round to the nearest whole number, and integers by definition are already whole numbers.
    If you enter a number typed out, e.g., ten, you will get a TypeError, because the program interprets "ten" as a string, and math.ceil() and math.floor() require numbers, not strings.
''' 
######################################


#For your reference:
    #RegEx in Python
        #Example: Search the string to see if it starts with "The" and ends with "Spain"
        #Check if the string starts with "The" and ends with "Spain":
'''
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES, We have a match!")
else:
  print("No match")
'''

##########################################
'''
HOME PRACTICE:
https://www.w3schools.com/python/python_regex.asp

Write a regex for finding a piece of info in a large body of text.
'''

#Julia's regex code

## package imports (necessary for the program to function properly) ##
import random
import re
import time

#set the reader speed (adjusts the length of the pause when time.sleep() is called)
r = .5

#assign a category
category = "animals"

#create a list of items in the assigned category
items = ["cat","dog","mouse","squirrel","raccoon","koala","kangaroo","bear","tiger","lion","sheep","mouse","elephant","python"]

## function to assign the secret word randomly ##
def assign_secret_word():    
    #assign the secret word randomly
    global secretword
    secretword = random.choice(items)

## function to assign the computer's guesses randomly ##
def set_guess():
  #reset full item list, if necessary
  currentlist = items[:]
  #create an empty string to store the computer's guess
  computerguess = ''
  #set a variable equal to the starting length of the list of items
  length = len(currentlist)
  #set a counter equal to zero
  i = 0
  while i < length:
    currentitem = random.choice(currentlist)
    computerguess += currentitem + " "
    currentlist.remove(currentitem)
    #iterate by 2 instead of 1 to add less items to the list and decrease likelihood of the computer guessing correctly
    i += 2
  return computerguess

## gameplay function ##
def game():
    #say hello
    print("I'm thinking of a secret word... I'd like for you to try to guess it!")
    time.sleep(r)
    
    #ask the user for guesses
    txt = input("Type as many words as you'd like, or type 'no' and I'll guess for you:\n")

    #if user types no, set txt equal to the hard-coded list and display it
    if txt == "no":
        txt = set_guess()
        print()
        print("I guessed this for you: \n"+txt)
        
    #search the user input for the secretword
    x = re.search(r'\b'+secretword+r'\b', txt.lower())
    time.sleep(r)
    print()
    #if the user guessed correctly, congratulate them and tell them what the word was
    if x:
        print("Congratulations, you guessed it! The secret word was "+secretword+".")
    else:
    #if the user guessed incorrectly, ask if they want to try again
        print("Nope, that wasn't it!")
        restart = input("Would you like to try again? 'y' for yes, 'n' for no, or 'answer' to give up:\n")
        #accept yes or no, even though it asks for y or n
        if restart == "y" or restart == "yes":
            print()
            time.sleep(r)
            print("I'll give you a hint... it's in this category: "+category)
            time.sleep(r)
            game()
        elif restart == "n" or restart == "no":
            print()
            time.sleep(r)
            print("Ok, maybe you didn't enjoy this round.")
        elif restart == "answer":
            print()
            print("The secret word was: "+secretword)
        #optimistically interpret erroneous input as a yes
        else:
            print("That wasn't an option... I'll assume you want to make another guess!")
            game()

def play_again():
    restart = input("Would you like to play another round? y for yes, n for no: ")
    if restart == "y" or restart == "yes":
        assign_secret_word()
        return True
    elif restart == "n" or restart == "no":
        print("Ok, see you later!")
        return False
    #optimistically interpret erroneous input as a yes
    else:
        print("That wasn't an option... I'll take it as a yes!")
        return True

#introduce the program
print("----- Guessing Game version 1.0, by Julia Alsarraf ------")
print()
time.sleep(r)
print("Hello, and welcome to my guessing game program!")
print()
time.sleep(r)

#assign the secret word for the first time
assign_secret_word()

playing = True
while playing:
    #run the guessing game
    game()  
    #ask if the user wants to play again
    playing = play_again()

##########################################
