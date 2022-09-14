# Challenge ex17.py: 
#     Given a quadratic equation, find its roots using the Bhaskara formula.

a = int(input("Enter de coefficient a value with the + or - sign:"))
if a == 0:
    print("The a coefficient is a non-zero term.")
    quit()
b = int(input("Enter de coefficient b value with the + or - sign:"))
c = int(input("Enter de constant c value with the + or - sign:"))

import math
number = ((b*b) - (4*a*c))
if number < 0:
    print('The roots of the equation do not exist or are imaginary')
else:
    discriminant = math.sqrt(number)   
    root1 = (-b+ discriminant)/(2*a)
    root2 = (-b- discriminant)/(2*a)
    print(f'The roots of the equation are:', root1, 'and',root2)
#return:
# Enter de coefficient a value with the + or - sign:+4
# Enter de coefficient b value with the + or - sign:+5
# Enter de constant c value with the + or - sign:-6
# The roots of the equation are: 0.75 and -2.0