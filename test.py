import numpy as np

print("Hallo")

print("Philip")

def phil_Weibull_Cal(wind_speed, a, k = 2):
    WeiDist = k / a * (wind_speed/a)**(k-1)*np.exp(-(wind_speed/a)**k)
    return WeiDist
    
    