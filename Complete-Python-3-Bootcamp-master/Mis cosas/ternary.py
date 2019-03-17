import math

def func (x):
    return 2 * x**2 - 12 * x + 7 

def minternarySearch(l, r, f):
    for i in range (200):
        mid1 = l + (r - l) / 3.0
        mid2 = r - (r - l) / 3.0

        if math.abs(l - mid1) < 0.5 or math.abs(r - mid2) < 0.5:
        	break

        if f(mid1) < f(mid2):
            r = mid2
        else:
            l = mid1
            
    return min(f(l), f(r))

n = int(input())
for i in range (1):
    parameters = list(map(int, input().split(' ')))
    print( round(minternarySearch(parameters[0], parameters[1], func)) )
    
