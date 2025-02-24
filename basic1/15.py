'''
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
'''

print("enter a number")
inputnumber = int(input())

if inputnumber > 17:
    if inputnumber-17 >= 17:
        print((inputnumber-17)*2)
    else:
        print("the number is not greater than 17")
else:
    print(17-inputnumber)
    print("nothing to print")

