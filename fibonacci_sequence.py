# To print the first 50 terms of the Fibonacci sequence sequentially
# Recurrence relation : F(n) = F(n-1) + F(n-2)


previous = 0 #F(n-1)
current = 1 #F(n)
i = 1 #term

while i <= 50:
    print(current)
    temp = previous #F(n-2)
    previous = current
    current = current + temp
    i += 1
