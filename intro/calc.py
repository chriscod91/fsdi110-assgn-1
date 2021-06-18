#description
"""
pycalc: simple calculator
author: Chris codina
date: June,15 2021
functionality:
-simple mathematical operations(sum, sub, multiply, divide ) 
"""

#import

#globals

#function
def print_menu():
    print("---------------")
    print("Welcome to PyCalc")
    print("---------------")

    print("1 - Sum")
    print("2 - Subtract")
    print("3 - multiplication")
    print("4 - divide")
    print("5 - is it odd?")
    print("6 - print a message n times")

    print("q - quit")
    print("-------------")

def clear():
    print("\n\n")    
#instructions
selected_option = ""
while(selected_option != "q"):
    clear()
    print_menu()

    selected_option = input("select an option: ")
    if(selected_option == 'q'):
         break
    
    if(selected_option == "6"):
        text = input("enter you message:")

        times = int(input('amount of times:'))
        print(text * times)
        break

    if(selected_option == "5"):    
        num = int(input("enter a number: "))
        if(num <  0): 
          print("is odd")
        
        elif(num >= 0):    
          print("is not odd")
        break         
    
    num1 = float(input("provide num1: "))
    num2 = float(input("provide num2: "))

    if(selected_option == "1"):
        res = num1 + num2
        print("\n")
        print(f"Your result is: {res}") 
       
    elif(selected_option == "2"):
        res = num1 - num2
        print("\n")
        print(f"Your result is: {res}")

    elif(selected_option == "3"):
        res = num1 * num2
        print("\n")
        print(f"Your result is: {res}")

    elif(selected_option == "4"):
        if(num2 == 0):
            print("ERROR: division by zero is not allowed")
        else:    
            res = num1 / num2
            print("\n")
            print(f"Your result is: {res}")
            

           

        input("\npress enter to continue...")    

print("goodbyte!!")
            
 

        
