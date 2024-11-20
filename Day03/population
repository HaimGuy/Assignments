import math
P0 = [8000000,3000000,5000000,1000000,700000,40000,10000000,6000000,200000,5000000] # initial populations size at time 0
r = float(input("What is the population's growth rate (as a decimal)? ")) # ask for Growth Rate 
t = 1 # time elapsed - one year  
P1_values = []
for P in P0:
    pt = P * math.exp(r * t)
    P1_values.append(pt)
    print(f"Initial population size: {P} mg/mL -> one year later: {pt:.2f}")
