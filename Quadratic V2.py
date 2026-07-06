import re
import math
import cmath


def quadratic_solver():
  #The OG Input 
    Equation=input("Enter the Quadratic Equation").lower()
  
    a = Equation.split("x")
    b=Equation.replace(" ","")
    b=re.split(r'\^2',a[1] , maxsplit=2)

    #coeffecients
    coeff_a=int(a[0])
    coeff_b=int(b[1])
    coeff_c=int(a[2])

    #Adding the Components 
    b_squared=coeff_b**2
    four_ac=4*coeff_a*coeff_c
    Discriminant=b_squared-four_ac
#Real Soln
    if Discriminant >=0:
        sqrt_discriminant=math.sqrt(Discriminant)
        multiplication=-1*coeff_b+sqrt_discriminant
        multiplication2=-1*coeff_b-sqrt_discriminant
        two_a=2*coeff_a
        case_1=multiplication/two_a
        case_2=multiplication2/two_a
        print("Your roots are:",case_1,"and",case_2)
#imaginary Soln
    if Discriminant<0:
        sqrt_discriminant=cmath.sqrt(Discriminant)
        multiplication3=-1*coeff_b+sqrt_discriminant
        multiplication4=-1*coeff_b-sqrt_discriminant
        two_a=2*coeff_a
        case_3=multiplication3/two_a
        case_4=multiplication4/two_a
        print("Your roots are:",case_3,"and",case_4)  
    print(coeff_a,coeff_b,coeff_c)
    print(a)
    
    
    

print("Welcome,To the Quadratic Solver V2")

while True:    
    quadratic_solver()    