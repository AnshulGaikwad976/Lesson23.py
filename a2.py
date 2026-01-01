def print_factor(number):
    print("the factors of the given number", number, "are")
    for i in range (1, number+1):
        if number % i ==0:

          print(i)

number = int(input("Enter your number to findthe factors"))

print_factor(number)