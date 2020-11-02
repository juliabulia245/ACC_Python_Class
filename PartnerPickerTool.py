#PartnerPicker v1.2
import random

#create empty list to store students
availablestudents = []

#ask the user to input student(s)
##to-do: add the option to import a .csv file
newstudent = input("Enter the name of a student, or multiple students separated by commas: ")
while newstudent != "done":
    availablestudents.append(newstudent)
    print("There are currently",len(availablestudents),"students total.")
    newstudent = input("Enter the next student(s), or type 'done' if you are finished: ")

##to-do: capitalize student names (maybe)

##to-do: print the list of students, and give the option to remove or update a student record
    
#let the user know if there are zero students.
if len(availablestudents) == 0:
    print("There are no students! The program will close.")

#pair up the students
while len(availablestudents) > 1:
    currentstudent = random.choice(availablestudents)
    availablestudents.remove(currentstudent)
    partner = random.choice(availablestudents)
    print(currentstudent,"is partnered with",partner+".")
    availablestudents.remove(partner)
if len(availablestudents) == 1:
    print(availablestudents[0],"does not have a partner.")
    print()
else:
    print("Everyone is paired up!")
    print()
