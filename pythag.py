def main():
    a= float(input("how long is a?"))
    b= float(input("how long is b?"))
    pythag(a,b)

    
import math 

def pythag(x,y):
    print(math.sqrt((x*x)+(y*y)))

main()