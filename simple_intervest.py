import numpy as np 
#PV: future value, m : cycle , r :rate , In : coupoding interest
def simple_intervest(PV, m, r):
    In = PV*m*(r/100)
    return np.round(In,3)

# r: lai xuat , n so ky tinh lai, PV : von 
def value_future(PV, r, n):
    Fn = PV*(1+(r/100)*n)
    return np.round(Fn,3)


print(simple_intervest(100, 5, 20))
print(value_future(100, 20, 5))


