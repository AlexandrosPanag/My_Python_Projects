primes = []

num = 2

while len(primes)< 100 :
    x = num//2
    while x> 1:
        if num % x == 0:
            break
        x -= 1
    else:
        primes.append(num)
    num+=1
    print(primes)
