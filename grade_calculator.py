
def main():
    score=int(input("What was your score?"))
    print(Grade(score))

def Grade(a):
    if a>=90 :   
        return ("A")
    elif a>=80:
        return ("B")
    elif a>=70:
        return("c")
    elif a>=60:
        return("D")
    else:
        return("F")

main()