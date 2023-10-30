'''
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''

def isEven(number):
        if number % 2 == 0:
            return True
        return False

def main():
    n = input("Input a number : " ).strip()
    try:
        number = int(n)
        if isEven(number) and number in range(2, 5):
            print("Not Weird")
        elif isEven(number) and number in range(6, 20):
            print("Weird")
        elif isEven(number) and number > 20:
            print("Not Weird")
        elif not isEven(number):
            print("Weird")
    except ValueError:
        print("Cant convert to integer")



if __name__ == '__main__':
    main()
