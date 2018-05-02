check_num = int(input("Please enter a number to check: "))
if check_num % 3 == 0 and check_num % 5 == 0 :
    print("Fizz Buzz")
elif    check_num % 3 == 0 :
    print("Fizz")
elif    check_num % 5 == 0 :
    print("Buzz")
else:
    print("Try agin")