def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def percent_to_float(p):
    P=(p).strip("%") 
    return (float(P)/100)


def pounds_to_float(d):
    D=(d).strip("£") 
    return (float(D))
   


main()