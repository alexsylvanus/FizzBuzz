# File: FizzBuzz.py
# Author: Alex Sylvanus
''' Description: Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz  
    instead of the number and for the multiples of five print Buzz. For numbers which are multiples 
    of both three and five print FizzBuzz. '''

# FizzBuzz1 Function
def fizzBuzz1():
    # Iterate through numbers 1-100 
    for i in range(1, 101):
        # Check conditions 
        if (i%15 == 0): print("FizzBuzz")
        elif (i%3 == 0): print("Fizz")
        elif (i%5 == 0): print("Buzz")
        else: print(i)
    print("\nDone!")

# FizzBuzz2 function
def fizzBuzz2():
    # Iterate through the numbers 1-100
    for i in range(1, 201):
        # Assign value to string
        s = "Fizz" if i%3==0 else ""
        s += "Buzz" if i%5==0 else ""
        print(s if s!="" else i)

    print("\nDone!")

# One line solution!
def fizzBuzz3():
    # Iterate through numbers 1-100
    for i in range(1, 101): print((i%3==0)*"Fizz"+(i%5==0)*"Buzz" if (i%3==0 or i%5==0) else i)

# Print the options for the user
def printOptions():
    print("1: Standard Solution")
    print("2: Compose string Solution")
    print("3: One line Solution")
    print("4: Exit program")

# Valid option conditional
def isValidOption(opt):
    # Declare return variable
    ret = False
    # Check if string is a single digit int
    if len(opt)==1:
        c = opt[0]
        # Check if char is digit between 1-4
        if ord(c)>=ord('1') and ord(c)<=ord('4'):
            ret = True

    # Return statement
    return ret

# Main function
def main():
    # Initialize input variable
    c = '0'

    # Print Options
    printOptions()
    while (c != '4'):
        # Prompt User
        s = input("Pick an option: ")
        
        # Check input validity
        if (isValidOption(s)):
            c = s[0]
            if (c=='1'): fizzBuzz1()
            elif(c=='2'): fizzBuzz2()
            elif(c=='3'): fizzBuzz3()
            else: print("Exiting program")
        else:
            print("Invalid Option - Try again")
            c = '0'
            printOptions()

    # End Program
    print("Finished!")

# Main condition
if __name__ == '__main__':
    main()