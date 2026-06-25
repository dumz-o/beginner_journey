# Character input to calculate when someone will turn 100
fname = input("Please enter your first name:")
sname = input("Please enter your surname:")

try:
    float(fname)
    float(sname)
    print("Please enter letters only")
except:
    try:
        age = float(input("Please enter your age:"))
        if age < 0 :
            print("You arent negative years old")
        else :
            hund = 100 - age
        
        # Cleaned up and streamlined conditionals
        if hund >= 80:    
            print(sname + " " + fname, "you still have", hund, "years left till hundred youngling")
        elif hund >= 70:  
            print(sname + " " + fname, "you still have", hund, "years left till hundred. About to retire just a few more years!!!")
        elif hund >= 60:  
            print(sname + " " + fname, "you still have", hund, "years left till hundred. Are you enjoying being a wage slave?")
        elif hund >= 50:  
            print(sname + " " + fname, "you still have", hund, "years left till hundred. About to hit unc status huh?")
        elif hund >= 35:  
            print(sname + " " + fname, "you still have", hund, "years left till hundred. Experiencing the vicissitudes of life. How is that?")
        elif hund >= 20:  
            print(sname + " " + fname, "you still have", hund, "years left till hundred. At least you've retired you can enjoy your peace.")
        elif hund >= 0:   
            print(sname + " " + fname, "you still have", hund, "years left till hundred. How are you even still alive....")
        else:             
            print("No way you legit lived past a hundred. You deserve a medal.")
            
    except ValueError:
        print("Please enter numbers only")
