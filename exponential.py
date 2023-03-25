"""
A python module for calculating the exponential of a number using exponential series
"""

def expo(x,debug=False):
    n=100
    m=1
    sum=1
    for i in range (1,n):
        m=m*x/i
        sum0=sum
        sum=sum+m
    if debug:
        if abs(sum-sum0)<1e-5:
            print("Series is converging in nature")
    return sum
