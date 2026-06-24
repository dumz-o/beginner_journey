#Temperature Converter: Write a program that converts temperature from Celsius Kelvin or Fahrenheit to each othe
temp1 = str(input("Please enter temperature to convert: (Celsius, Fahrenheit, Kelvin)"))
#Only allowing Celsius Fahrenheit or Kelvin
try :
    temp1 == str("Celsius, Fahrenheit, Kelvin")
except :
    print ("Please enter: Celsius, Fahrenheit or Kelvin ")
#Prompting for number to be selected
x = int(input("Please enter temperature value: "))
# Only numbers to be selected 
try :
    x == int()
except ValueError:
    print("Please enter numbers only!!!")
#Only allowing temperature to be selected again
temp2 = input("Please enter second temperature to convert: (Celsius, Fahrenheit, Kelvin) ")
try :
    temp2 == str("Celsius, Fahrenheit, Kelvin")
except :
    print ("Please enter: Celsius, Fahrenheit or Kelvin ")
# Conditions if Celsius is selected and its calculations
if temp1 == "Celsius" + temp2 == "Fahrenheit" :
    y = (x - 32)/5 * 9
    print(y, "F")
elif temp1 == "Celsius" + temp2 == "Kelvin" :
    y = x + 273
    print(y, "K")
else :
    print("Please select  Fahrenheit or Kelvin")
# Conditions if Fahrenheit is selected and its calculations
if temp1 == "Fahrenheit" + temp2 == "Celsius" :
    y = (x * 9/5) + 32
    print(y, "C")
elif temp1 == "Fahrenheit" + temp2 == "Kelvin" :
    y = (x - 32) * 5/9 + 273
    print(y, "K")
else :
    print("Please select other Celsius or Kelvin")
# Conditions if Kelvin is selected and its calculations
if temp1 == "Kelvin" + temp2 == "Fahrenheit" :
    y = (x - 273) * 9/5 + 32
    print(y, "F")
elif temp1 == "Kelvin" + "Celsius" :
    y = x - 273
    print(y, "C")
else :
    print("Please select Fahrenheit or Celsius")