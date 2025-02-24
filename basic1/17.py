
def oper(iNum1, iNum2, iNum3):
    if iNum1 == iNum2 and iNum1 == iNum3:
        print((iNum1+iNum2+iNum3)*3)
    else:
        print(iNum1+iNum2+iNum3)



def main():
    print("enter three  numbers  ")
    iNum1 = int(input())
    iNum2 = int(input())
    iNum3 = int(input())

    oper( iNum1, iNum2, iNum3)
    # if iNum == iNum2 and iNum1 == iNum3:
    #     print((iNum1+iNum2+iNum3)*3)
    # else:
    #     print(iNum1+iNum2+iNum3)


main()
