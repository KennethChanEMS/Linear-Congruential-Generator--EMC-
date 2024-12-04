from datetime import datetime

Modulus = 6
Times = datetime.now().minute
Const = datetime.now().second
start = datetime.now().hour
term = 997

def recursion(n, m, a, c, X):
    if  n == 0:
        return X
    else:
        stuff = a*recursion(n-1, m, a, c, X) + c
        return (stuff % m) + 1

print(recursion(term, Modulus, Times, Const, start))
