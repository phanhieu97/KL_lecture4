import numpy as np

def compound_interest(principle, rate, time):
    
    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))
    # print("Compound interest is", CI)
    return np.round(CI, 5)

# PV: amount, i : rate, n: time per year grows , t :year 
def frequencies_compounding(PV, i, n ,t):
    FV = PV*pow((1+((i/100)/n)),(n*t))
    return np.round(FV,5)

def Continuous_compounding(principle, rate, year):
    CI = principle*np.exp((rate/100)*year)
    return np.round(CI, 5)

# Amout $1 , rate : 10%
print("Compoud-interest :",compound_interest(1, 10, 1))
print("annually :",frequencies_compounding(1, 10, 1, 1))
print("semiannually :",frequencies_compounding(1, 10, 2, 1))
print("quarterly :",frequencies_compounding(1, 10, 4, 1))
print("monthly :",frequencies_compounding(1, 10, 12, 1))
print("daily :",frequencies_compounding(1, 10, 365, 1))
print("continuously :",Continuous_compounding(1, 10, 1))