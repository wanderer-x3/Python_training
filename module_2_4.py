numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0

for i in numbers[1:]:
    for j in numbers[1:i-1]:
        if i % j == 0:
            k +=1
            not_primes.append(i)
            break

    if k == 0:
        primes.append(i)
    else:
        k = 0

print(primes)
print(not_primes)