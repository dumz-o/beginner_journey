try :
    score = float(input("Enter score between 0 and 1: "))
    if 0.0 <= score <= 1.0 :
        if score >= 0.9 :
            print("A")
        elif score >= 0.8 :
            print("B")
        elif score >= 0.7 :
            print("C")
        elif score >= 0.6 :
            print("D")
        else :
            print("F")
    else :
        print("Please enter numbers between 0 and 1")
    
except ValueError:
    print("Please enter numbers only!!!")
