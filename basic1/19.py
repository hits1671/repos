
def func(text,count):
    for i in range(count):
        print(text, end='')

def main():
    print("enter the string")
    iStr = str(input())
    print("enter the number you want to copy the string")
    iNum = int(input())
    func(iStr,iNum)

main()