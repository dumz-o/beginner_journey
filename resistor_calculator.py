#Resistance calculator

try : #error checking for correct input 
    select = int(input("Please select how many resistors do you want to calculate(2, 3 or 4):")) #prompting user for how many resistors
    if select == 2 : #conditions and calculations if user wants to select 2 resistors
        try : #error checking for only numbers
            r1 = float(input("Enter resistor 1: ")) #prompting user for resistors to calculate for 2
            r2 = float(input("Enter resistor 2: "))
            x = r1 + r2 #Calculations for series
            rp1 = 1/r1
            rp2 = 1/r2
            inverse_sum = rp1 + rp2 #Calculations for parallel
            y = 1/inverse_sum
            calculation_type = str(input("Choose enter calculation type:(series or parallel)")) #Asking the user for calculation of series or parallel
            if calculation_type == "series":
                print("The sum is:", x) #Output if series
            elif calculation_type == "parallel" :
                print("The sum is:", y)#Output if parallel
            else :
                print("Please enter 'parallel' or 'sum' only") #Only allowing series or parallel to be typed
        except ValueError :
            print("Please enter numbers only")
    elif select == 3 :  #conditions and calculations if user wants to select 3 resistors
        try :  #error checking for only numbers
            r1 = float(input("Enter resistor 1: ")) #prompting user for resistors to calculate for 3
            r2 = float(input("Enter resistor 2: "))
            r3 = float(input("Enter resistor 3: "))
            x = r1 + r2 + r3 #Calculations for series
            rp1 = 1/r1
            rp2 = 1/r2
            rp3 = 1/r3
            inverse_sum = rp1 + rp2 + rp3 #Calculations for parallel
            y = 1/inverse_sum
            calculation_type = str(input("Choose enter calculation type:(series or parallel)")) #Asking the user for what they want to calculate
            if calculation_type == "series":
                print("The sum is:", x) #Output if series
            elif calculation_type == "parallel" :
                print("The sum is:", y) #Output if parallel
            else :
                print("Please enter 'parallel' or 'sum' only")  #Only allowing series or parallel to be typed
        except ValueError :
            print("Please enter numbers only")
    elif select == 4 : #conditions and calculations if user wants to select 4 resistors
        try :
            r1 = float(input("Enter resistor 1: ")) #prompting user for resistors to calculate for 4
            r2 = float(input("Enter resistor 2: "))
            r3 = float(input("Enter resistor 3: "))
            r4 = float(input("Enter resistor 4: "))
            x = r1 + r2 + r3 + r4 #Calculations for series
            rp1 = 1/r1
            rp2 = 1/r2
            rp3 = 1/r3
            rp4 = 1/r4
            inverse_sum = rp1 + rp2 + rp3 + rp4 #Calculations for parallel
            y = 1/inverse_sum
            calculation_type = str(input("Choose enter calculation type:(series or parallel)")) #Asking the user for what they want to calculate
            if calculation_type == "series":
                print("The sum is:", x)  #Output if series
            elif calculation_type == "parallel" :
                print("The sum is:", y) #Output if parallel
            else :
                print("Please enter 'parallel' or 'series' only")  #Only allowing series or parallel to be typed
        except ValueError :
            print("Please enter numbers only") 
    else :
        print("Please enter '2', '3' or '4' ") #Output for other number of resistors

except ValueError :
    print("Please enter '2', '3' or '4'") #Error Output
