import numpy as numpy

def treasury_bill (i ,o):
    l = (o-i)
    t = (l/o)*100
    return t

# def 
print("T-Bill :",treasury_bill(99.026806, 100))