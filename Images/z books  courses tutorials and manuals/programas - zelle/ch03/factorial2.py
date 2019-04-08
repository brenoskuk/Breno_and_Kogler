# factorial2.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator and long ints

def main():
    n = input("Please enter a whole number. ")
    fact = 1L    # Use a long int here
    for factor in range(n,0,-1): 
       fact = fact * factor
    print "The factorial of", n, "is", fact

main()
