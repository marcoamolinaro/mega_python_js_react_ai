def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(5))
    
