# assignment: programming assignment 3
# author: Peter Wang Zhao
# date: 10/25/2021
# file: calculator.py is a program that adds, subtracts, multiplies, and divides two numbers.
# input: (write the input description)
# output: (write the output description)

def format(num, precision=2):
    if num == int(num):
        num = int(num)
    else:
        num = round(num, precision)
    return str(num)


def add(num1, num2):
    add = num1+num2
    print(format(num1) + " + " + format(num2) + " = " + format(add))


def subtract(num1, num2):
    subtract = num1-num2
    print(format(num1) + " - " + format(num2) + " = " + format(subtract))


def multiply(num1, num2):
    multiply = num1 * num2
    print(format(num1) + " x " + format(num2) + " = " + format(multiply))

def divide(num1, num2):
    division = num1 / num2
    if num2 == 0:
        print("The division by zero is prohibited!\n")
    else:
        print(format(num1) + " / " + format(num2) + " = " + format(division))

def read_num(num):
    if num - round(num) > 0:
        return 1
    else:
        return 0

def isfloat(token):
    if token == '':
        return False
    dot = False
    minus = False
    for char in token:
        if char.isdigit():  # allow many digits in a string
            continue
        elif char == ".":  # allow only one dot in a string
            if not dot:
                dot = True
            else:
                return False
        elif char == "-" and token[0] == "-":  # allow one minus in front
            if not minus:
                minus = True
            else:
                return False
        else:  # do not allow any other characters in a string
            return False
    return True


# main program

# the main while loop starts here)
# it should be removed when you start to write your loop!!!
##    (print the menu)

##    (get the user choice)

##    (acknowledge the user choice)

##    (start the first inner loop to get the first number)

##    (quit the first inner loop if the input is correct)

##    (start the second inner loop to get the second number)

##    (quit the second inner loop if the input is correct)

##    (call the function depending on the user choice)

##    (get the user choice for the prompt 'Do you want to continue? [Y/N]:')

##    (quit the program if the choice is not 'Y' or 'y')
print("Welcome to Calculator Program!\n")
done = False
while not done:
    t = 'Y'
    while t == 'Y':
        print("Please choose one of the following operations:\n")
        print("Addition - A\n")
        print("Subtraction - S\n")
        print("Multiplication - M\n")
        print("Division - D\n >")
        ch = input().upper()
        if ch not in "ASMD":
            print("You did not choose correctly.\n")
        else:
            if ch == 'A':
                print("You chose addition.\n")
            elif ch == 'S':
                print("You chose subtraction.\n")
            elif ch == 'M':
                print("You chose multiplication.\n")
            elif ch == 'D':
                print("You chose division.\n")
            while True:
                num1 = input("Please enter the first number: \n")
                if isfloat(num1):
                    num1 = float(num1)
                    print(f'The first number is {format(num1)}.\n')
                    break
                else:
                    print("You did not choose a number.\n")
                    continue
            while True:
                num2 = input("Please enter the second number: \n")
                if isfloat(num2):
                    num2 = float(num2)
                    print(f'The second number is {format(num2)}.')
                    break
                else:
                    print("You did not choose a number.\n")
                    continue
            if ch == 'A':
                add(num1, num2)
            elif ch == 'S':
                subtract(num1, num2)
            elif ch == 'M':
                multiply(num1, num2)
            elif ch == 'D':
                if num2 == 0:
                    print("The division by zero is prohibited!\n")
                else:
                    divide(num1, num2)
            ans = input("Do you want to continue? [Y/N] :\n")
            if ans.upper() != 'Y' or ans.lower() != 'y':
                done = True
                break
            elif ans.upper() == 'Y' or ans.lower() == 'y':
                continue
    print("Goodbye!\n")
    pass




