'''Importing all the python files which includes file handling,
custome transcation and overwriting the txt files.'''
import View
import Rent
import Return
import Exit
import datetime

print("................................................")
print("     Welcome to the Sakun Rental Store!!...")
print("................................................")
print("         Kamalpokhari, Kathmandu                ")
print("                 Since,2003!                    ")
print("")
        
#defining a function main to call the other functions 
def main():
    #providing details to perform a specific task
    while True:
        print("++"*15)
        print("What are you planning to do?")
        print("++"*15)
        print("")
        print("1] View Costume (V)")
        print("2] Rent Costume (R)")
        print("3] Return Costume (RC)")
        print("4] Exit (E)")
        print("")
        print("++"*15)
        #implementating exception
        try:
            #asking the user to select the option
            select=(input("Enter the option in the brackets: "))
            #reading files
            if(select.upper()=="V"):
                View.view_costume()
            elif(select.upper()=="R"):
                Rent.Rent_costume()
            elif(select.upper()=="RC"):
                Return.Return_costume()
            elif(select.upper()=="E"):
                Exit.Exit()
                break
            else:
                print("Please enter the valid input...")
                print("")
        except:
            print("Please provide input as suggested!!")
            #exception is handeled...
            
#calling the function to perform all the actions...
main()
        
