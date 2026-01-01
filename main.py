number = int(input("Enter your number:"))

digits = len(str(number))

resultnumber =0

temp = number
while temp>0:
    digit = temp%10
    resultnumber += digit** digit
    temp//= 10

if number == resultnumber:
    print( number, " is an armstrng number")

else:
    print(number, "is armstrong number")    
