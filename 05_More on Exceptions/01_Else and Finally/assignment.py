#Continue with code from 3.3

number1 = 0
number2 = 0
answer = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
    answer = number1 / number2
except ValueError:
    print("An input was not correct")
except ZeroDivisionError:
    print("YOU TRIED TO DIVIDE BY ZERO")
else:
    print("No value error detected")
finally:
    print("Values taken care of")


