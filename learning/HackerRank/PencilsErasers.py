def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    
def findWay(N, M, P, E):
    pencils = factorial(N) // (factorial(P) * factorial(N - P))
    erasers = factorial(M) // (factorial(E) * factorial(M - E))
    return pencils * erasers
    
    
N = int(input()) # Number of pencils avail in shop
M = int(input()) # Number of erasers avail in shop
P = int(input()) # Number of pencils to choose from N
E = int(input()) # Number of erasers to choose from M
print(findWay(N, M, P, E))