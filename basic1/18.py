def addis(iString):
    if iString[0:2]=="is":
        print(iString)
    else:
        print("is"+iString)
def main():
    print("enter sentence")
    iStr = str(input())
    addis(iStr)

main()