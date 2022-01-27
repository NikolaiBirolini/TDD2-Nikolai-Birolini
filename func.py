import string

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