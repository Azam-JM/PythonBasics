def fib_gen(n):
    if n <= 0:
        return -1
    x = 0 
    y = 1
    for _ in range(n):
        yield x
        x, y = y, x + y
    
gen = fib_gen(10)
print(list(gen))
