import string
from sympy import *

def func_mirroir(mot,val):
    if val <0:
        print("Error - val negative")
        return False
    
    if len(mot) < 1:
        print("Error - string vide")
        return False
    
    if val > len(mot):
        print("Error - val trop grand")
        return False

    return mot[:(val+1)]+''.join(reversed(mot[:(val+1)]))


def func_deriv(List_val):
    h_pas = 1
    List_output = []

    if len(List_val) < 2:
        print("Error - Liste trop courte")
        return False
    
    for val in range(len(List_val)-1):
        List_output.append((List_val[val+1]-List_val[val])/h_pas)
    return List_output

def func_deriv_sec(List_val):
    h_pas=1
    List_output = func_deriv(List_val)
    
    if not(List_output):
        print("Error - Liste trop courte")
        return False

    return func_deriv(List_output)

def func_approx(formula,point,approx):
    if len(formula) < 1:
        print("Error - Taille trop petite")
        return False
    
    if approx > 5 or approx < 0:
        print("Error - approx invalide 0 - 4")
        return False
    
    x = Symbol('x')
    deriv = diff(formula,x)
    fct = lambdify(x,deriv)

    return round(fct(point),approx)