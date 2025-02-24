def oddEvenChk(iNum):
    if iNum==0:
        print("please enter a valid number")
    elif iNum % 2 ==0:
        print("given number is even")
    else:
        print("given number is odd")
def main():
    print("enter a number to check that is odd or even")
    num = int(input())
    oddEvenChk(num)

