# CISC 475 - Group 4
# sumnumbers
# - This code returns the sum from 1 to n
# - user defined function for pl/python
def sumnumbers(n):
    sum = 0
    for i in range(1, n+1):
         sum = i + sum
    return sum

