import math
def sinee(x):
    term = x 
    sum = x
    eps = 1E-8
    n = 2 
    
    while abs(term/sum) > eps:
      term = -term*x*x/((2*n - 1)*(2*n - 2)) 
      sum = sum + term 
      n = n + 1 
    return sum


x = float(input("Enter an angle: "))
if x > 360: 
   x = x % 360
x=x/360*math.pi
print("My sine function sin(x)=",sinee(x))
print("sin(x) = ", math.sin(x))