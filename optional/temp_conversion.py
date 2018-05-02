temp = float(input("Please enter the temperature: "))
c_or_f = str(input("Is this Celsius or Fahrenheit? (Please enter C or F): "))

if c_or_f == 'C':
    temp = (temp * 1.8) + 32
    print(f"That is {round(temp,2)} F")
elif c_or_f == 'F' :
    temp = (temp-32)/1.8
    print(f"That is {round(temp,2)} C")
else:
    print("Please try again with either C or F")

