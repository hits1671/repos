def findNumberWithinRange(num):
    if num > 100 and num <1000:
        print("number is within range of 100 and 1000")
    elif num > 1000 and num < 2000:
        print("number is not within range of 1000 and 2000")
    else:
        print("number is not within range of 100 and 2000")

def main():
    print("enter a number")
    num = int(input())
    findNumberWithinRange(num)
main()