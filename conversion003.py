" conversion for ferinhit and celsius "



degree = input("Enter C for celsius and f for Fahreheit :")
temp = int(input("Enter the temperature's value :"))

if degree == "f":
    C = (temp-32)*5/9
    print("The conversion in Celsius is :", round(C))
elif degree == 'c':
    F = temp*9/5+32
    print("The conversion in Fahreheit is :", round(F))

else:
    print("There is not such type of temperature:", degree)