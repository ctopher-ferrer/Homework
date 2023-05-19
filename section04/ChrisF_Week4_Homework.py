# 1. Use the DateTime module to get Current Date and Time, and save it to a variable.
# Then extract just the Full month name form that variable. 
import datetime as dt
today = dt.datetime.now()
print("The date today is.....",today)
print("\nIt's....", today.strftime("%B"))

#----------------------------------------------------------------------

# 2. Write a simple function that takes 2 parameters 
# -- a first name and a day name.

# Set a dafualt value fore the name of Sunday
# Have the function print out a greeting -- using the parameters 
def greeting(fname, day_name = 'Sunday'):
    print("\nWhat is up, " + fname + "! Happy "+ day_name + "!!")

# Invoke function with 2 variables
greeting("Chris","Friday")
# Invoke function with 1 variable
greeting("Chris")


#------------------------------------------------------------------
# 3. Write a block of code to handle one of the most common Python exception 
# errors. Select one of the common errors from the curriculum section on 
# Python Exception handling. Have your code example uses the 
# try,except, else, and finally components.

fav_number = input("\nWhat is your favorite number (in digit format)? ")
try:
    print("\nYour favorite number divided by 2 is...",int(fav_number)/2)
except ValueError:
    print("\nHey!!!! You didn't give a valid digit number....")
else:
    print("\nThank you for putting a valid number!!")
finally:
    print("\nI hope I did a good job on my homework assignment....")