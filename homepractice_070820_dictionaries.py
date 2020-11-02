# homepractice_070820_Julia_Alsarraf.py
# Dictionary Program version 1.0

'''
Directions:
Create your own dictionary with at least 10 items:
Add an item to the dictionary (totaling 11 items)
Remove an item in the dictionary (totaling 9 items)
Change an item in the dictionary
'''

#imports
import time

#create the startup dictionary
d = {
    "coronavirus" : "RNA viruses that cause diseases in mammals and birds",
    "social distancing" : "increasing the physical space between you and other people to avoid spreading an illness",
    "quarantine 15" : "weight gain attributed to staying home during the shutdown",
    "PPE" : "acronym for Personal Protective Equipment",
    "hotspot" : "a place with a high percentage of COVID-19 cases",
    "superspreader" : "a scenario where a small number of carriers infect a disproportionate number of others",
    "livestream" : "dissatisfying substitutes for in-person events",
    "quarantini" : "alcoholic beverages, particularly martinis, consumed during quarantine",
    "toilet paper" : "a rare and precious commodity, particularly in the early days of the shutdown",
    "rona" : "an informal shortening of 'coronavirus'",
    }    

#function to format display of definitions across multiple lines
def format(string,longest_key):
    maxlength = 70
    length = maxlength - longest_key
    output = ''
    split_string = string.split(" ")
    for i in split_string:
        if len(i) >= length:
            print("\n" + i + "\n",end="")
        else:
            if (len(output) + len(i) + 1) < length:
                print(i,end=" ")
                output += i
            else:
                print("\n" + (" "*(longest_key+3)) + i, end=" ")
                output = i
    print("\n",end="")

#function to view the items in the dictionary
def view(d):
    print()
    header = "These are the items currently in the dictionary:"
    print(header)
    print('-'*len(header))
    #find the length of the longest key
    longest = 0
    for x in d:
        if len(x) > longest:
            longest = len(x)
    #iterate through the dictionary to display items 
    for x,y in d.items():
        #add spaces by subtracting length of current key from length of longest key
        print(" "*(longest-len(x)) + x + " : ",end="")
        format(y,longest)
    print('-'*len(header))

#function to view the terms in the dictionary
def view_terms(d):
    print()
    header = "The terms in this dictionary are: "
    print(header)
    print("-"*len(header))
    #iterate through the dictioanry
    for x in d:
            print(x)
    print("-"*len(header))
    print()

#function to check whether a key (input_key) is in the dictionary (d), and if it is, return the key from the original dictionary
def key_in_dict(d,input_key):
    #convert input_key to lowercase
    lower_key = input_key.lower()
    #create lowercase version of dictionary to check against lowercase version of key (input_key.lower())
    d_lower = {k.lower() for k in d.keys()}
    #evaluate whether or not the key is in the dictionary
    if input_key.lower() in d_lower:
        #find the original matching key (there might be a better way to do this)
        for x in d:
            if x.lower() == lower_key:
                return x
    else:
        return False
            
#add an item to the dictionary (calls the update function if the key already exists)
def add(d,input_key=None):
    print()
    #if a key was not passed into the function, ask for one
    if input_key == None:
        input_key = input("Please type a new term, or press Enter to return to the main menu: ")
    while key_in_dict(d,input_key):
        match = key_in_dict(d,input_key)
        #provide the option to update (by calling the update function) or enter a new key
        update_ask = ''
        while update_ask not in {'y','n'}:
            update_ask = input("Sorry, " + match + " is already defined." + "\n" + "Would you like to update it instead? (y/n): ")
            if update_ask == 'y':
                update(d,match)
                return
            elif update_ask == 'n':
                view_terms(d)
                break
            else:
                print("That wasn't an option.")
        input_key = input("Please type another term, or press Enter to return to the main menu: ")

    #go back to main() if the user pressed Enter
    if input_key == "":
        return
    
    #ask the user for the value of the new key, add the item to the dictionary
    input_value = input("Please type the definition for '" + input_key + "': ")
    d[input_key] = input_value
    print()
    print("You've added the following item: ")
    print(input_key + " : " + input_value)
    
    time.sleep(1)
    view(d)

#update an item in the dictionary (passed as an argument if called from another function)
def update(d,input_key=None):
    print()
    #if a key was not passed into the function, ask for one
    if input_key == None:
        input_key = input("Please type the term you would like to update, or press Enter to return to the main menu: ")
    while not key_in_dict(d,input_key):
        if input_key == "":
            return
        print("Sorry, " + input_key + " is not in the dictionary.")
        add_ask = ''
        while add_ask not in {'y','n'}:
            add_ask = input("Would you like to add " + input_key + " as a new term instead? (y/n): ")
            if add_ask == 'y':
                add(d,input_key)
                return
            elif add_ask == 'n':
                view_terms(d)
                break
            else:
                 print("That wasn't an option.")
        input_key = input("Please type a valid term, or press Enter to return to the main menu: ")

    #ask the user for the new value of the existing key, update the dictionary
    match = key_in_dict(d,input_key)
    input_value = input("Please type the new definition for " + match + ": ")
    d[match] = input_value
    print()
    print("You've updated the definition of '" + match + "' to: " + input_value)
    time.sleep(1)
    view(d)
    
#remove an item from the dictionary
def remove(d):
    print()
    input_key = input("Please type the term you'd like to remove, or press Enter to return to the main menu: ")
    while not key_in_dict(d,input_key):
        if input_key == "":
            return
        print("Sorry, " + input_key + " is not in the dictionary.")
        view_terms(d)
        input_key = input("Please type a valid term, or press Enter to return to the main menu: ")
    match = key_in_dict(d,input_key)
    del d[match]
    print("You've removed the following term: " + match)
    time.sleep(1)
    view(d)

#main function        
def main():
    #display title, introduce the program, and display the dictionary once before asking for user input
    title = "*** Dictionary Program *** version 1.0 (Julia Alsarraf)"
    print('-'*len(title))
    print(title)
    print('-'*len(title))
    print()
    time.sleep(.5)
    print("Welcome to my dictionary program!")
    print("This dictionary contains terms about the COVID-19 pandemic.")
    print("You can view, add, update, or remove items from the dictionary.")
    time.sleep(1)
    
    running = True
    
    while running:
        print()
        choice = input("Please type a command ('view','add','update','remove', or 'exit'): ")
        if choice == 'view':
            view(d)
        elif choice == 'add':
            add(d)
        elif choice == 'update':
            update(d)
        elif choice == 'remove':
            remove(d)
        elif choice == 'exit':
            print("The program will now exit.")
            time.sleep(1)
            running = False
        else:
            print()
            print("That wasn't an option.")

main()
