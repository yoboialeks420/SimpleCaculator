## What do we want to learn today?
# -- Aleksander's answer: We want to learn how to use a calculator. Not how to use! You are serously typing everything i say?!
# We want to learn to build a simple calculator.
# In this we will learn:
# 0 Data types in python
# 1 How to read from the console and how to call functions in python
# 2 How to print stuff out.
# 3 If statements
# 4 Math operations with simple numbers
# 5 Maybe a loop :)

def basicTypesInPython():
    """
    Examples of types in python

    Programing languages have something called a "Type System". Python's is called "duck typeing" Meaning
    This means that type enforcement is weak and is not specified as it is in other languages.
    It is called Duck Typing because of the expression: "If it looks like a duck and quacks like a duck, it is a duck" :)
    'Types' is short for Data Types which means what kind of data or object (we will get to that some other time) is stored in a varable
    A varable is a "named thing" that stands for some data. see examples below

    """

    myFirstVarable = 5  # This is the type "Integer"
    # In python we can reassign things without issue. This is not true in other languages
    myFirstVarable = "Hello"  # now myFirstVarable this is a "String"
    mySecondVarable = myFirstVarable  # now this new variable is also a string
    myFirstVarable = 5  # I've reassigned myFirstVarable back to an int
    # What happened to my second variable!?
    print(mySecondVarable)  # This says "Hello" because the reassignment

def printExample():
    """
    This is a function that shows how printing stuff works in python!
    """
    # Printing is very simple, we just call the print function. In py3 we wrap the call in parentheses.

    print("Your text here!")  # Prints the inside to the console

def readExample():
    """
    This is an example of a function that reads stuff in from the console
    """

    theInput = input("Prompt> ")
    print("You said: " + theInput)

def ifStatementExample():
    """
    This is an example of how if statements work
    # Lets do this with types!
    """
    # First we take an input
    anythingWeWant = 5
    if (anythingWeWant > 5 ):
        print("Wow, big number")
    elif (anythingWeWant < 3):
        print("Small number")
    else:
        print("ok number")

def mathOperationExamples():
    """
    Examples of how to do simple math operations
    """
    myNumber = 5
    print(type(myNumber))
    # Add a number
    myNumber = myNumber + 1
    myNumber += 1  # This statement is equivalent to the above
    # Subtract a number
    myNumber = myNumber - 1
    myNumber -= 1  # This statement is equivalent to the above
    # Multiply a number
    myNumber = myNumber * 2
    myNumber *= 1  # This statement is equivalent to the above
    # Divide a number
    myNumber = myNumber / 2
    myNumber /= 1  # This statement is equivalent to the above
    print(myNumber) # Aleksander thinks this is going to be 5
    # He was right, but it was 5.0. The reason is, when you divide python makes the return type a float!
    # A float is a number that can have a decimal!
    print(type(myNumber))

def main():
    """
    This is where you (Aleksander) will code the calculator!!
    :return: Awesomeness!!
    """
    # When I write a program, I break things up into steps
    # 1. Input two numbers
    #    1a. (Hint: they will come in as strings you have to convert them to a number! Try to google how to do this!)
    # 2. Take in the operation to be done. Use an if statement to figure out which operation
    # 3. Print out the result!
    # firstdigit = int(input("First number: "))
    # print(firstdigit)
    # seconddigit = int(input("second number: "))
    # print(seconddigit)
    # print(firstdigit+seconddigit) # This just combines the two numbers!? why?
    # # Lets check the DataTypes
    # print(type(firstdigit))
    # print(type(seconddigit))

    firstdigit = float(input("First number: "))
    seconddigit = float(input("second number: "))

    operation = input("Operation")

    print(firstdigit + seconddigit)


if __name__ == "__main__":
    main()