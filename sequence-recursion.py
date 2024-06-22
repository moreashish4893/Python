def sequence(n):
    if n < 1:             # <---- base case
        return
    print(n)
    sequence(n-1)

sequence(10)    