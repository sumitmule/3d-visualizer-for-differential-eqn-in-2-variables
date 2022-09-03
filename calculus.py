from sympy import *
from sympy.abc import x, y
from sympy.plotting import plot3d
from sympy.plotting import plot3d_parametric_line

init_printing()

#------- to take function input from the user -------#

# F1 = input("Enter a function: ")
# F = parse_expr(F1)



#----- sample inputs -----#

# F = x**3 + 3*x*y**2 - 3*x**2 - 3*y**2 + 7
F = x**2+y**2+6*x+12
# F = x**3*y**2 - x**4*y**2 - x**3*y**3
# F = x**2 + 4*y**3 - 12*y**2 - 36*y+2
# F = x**2+y**2+x*y



p = diff(F,x)
q = diff(F,y)
r = diff(p,x)
s = diff(q,x)
t = diff(q,y)

eq1 = Eq(p, 0)
eq2 = Eq(q, 0)

sol = solve((eq1, eq2),(x, y))

f = r*t-s**2

if (str(type(sol)) == "<class 'list'>"):
    for i in sol:
        if str(f).isdigit() and f>0:
            if r >0:
                fmin = F.subs({x:i[0], y: i[1]})
                print("fmin =", fmin, "at ", i[0], ",",i[1])
            elif r<0:
                fmax = F.subs({x:i[0], y: i[1]})
                print("fmax =", fmax, "at ", i[0], ",",i[1])
                
        
        elif (f.subs({x:i[0], y: i[1]}) > 0):
            if r.subs({x:i[0], y: i[1]}) < 0:
                fmax = F.subs({x:i[0], y: i[1]})
                print("fmax =", fmax, "at ", i[0], ",",i[1])
            elif r.subs({x:i[0], y: i[1]}) > 0:
                fmin = F.subs({x:i[0], y: i[1]})
                print("fmin =", fmin, "at ", i[0], ",",i[1])

else:
    if f.subs({x:sol[x], y: sol[y]}) > 0:
        if r.subs({x:sol[x], y: sol[y]}) > 0:
            fmin = F.subs({x:sol[x], y: sol[y]})
            print("fmin=", fmin, "at ", sol[x], ",",sol[y])
        elif r.subs({x:sol[x], y: sol[y]}) < 0:
            fmax = F.subs({x:sol[x], y: sol[y]})
            print("fmax=", fmax, "at ", sol[x], ",",sol[y])
        

#plot3d(F, (x, -10,10), (y, -10,10))
plot3d(F)











