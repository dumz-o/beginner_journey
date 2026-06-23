#selecting what you are calculating
choice = input("Please select what you want to calculate: (voltage, current, resistance)")
if choice == "voltage":
    #calculations for voltage
        current = float(input("Enter Current:"))
        resistance = float(input("Enter Resistance:"))
        voltage = current * resistance
        print(voltage, "v")
elif choice == "current":
    #calculations for current
    voltage = float(input("Enter Voltage:"))
    resistance = float(input("Enter Resistance:"))
    current = voltage/resistance
    print(current,"A")
elif choice == "resistance":
      #calculations for resistance 
    voltage = float(input("Enter Voltage:"))
    current = float(input("Enter Current:"))
    resistance = voltage/current
    print(resistance, "ohms")
#if the user is an illiterate
else: 
     print("Please select voltage resistance or current!!!")