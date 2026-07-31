#import math library
import math
print("Condition: |g'(x)<1")
#Ask the user to enter g(x)
expression = input("Enter the function g(x): ")
#create a function to evaluate g(x)
def g(x):
    return eval(expression, {"x": x, **vars(math)})

#Fixed Point Iteration Method
def fixed_point_iteration(tol, p0, max_iter):

    i = 1

    while i <= max_iter:
        p = g(p0)

        #Check whether convergence has been achieved
        if abs(p - p0) < tol:
            print("The answer is:", p)
            print("It converged after", i, "iterations.")
            return p

        #Prepare for next iteration
        p0 = p
        i += 1

    print("The function did not converge.")
    return None
#Get inputs from the user
Tolerance = float(input("Enter the tolerance parameter: "))
F_Guess = float(input("Enter the initial guess: "))
n = int(input("Enter the maximum number of iterations: "))

#Call the function
fixed_point_iteration(Tolerance, F_Guess, n)
#examples
#1/2*(x+3/x)
#cos (x)
#(1-x)**(1/3)