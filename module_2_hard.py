
n = int(input('Введите число: '))

dividers = list()
resul = str()
for div in range(3, n//2+1):
    if n % div == 0:
        dividers.append(div)
dividers.append(n) # print(dividers) => [3, 4, 6, 12]

for j in  range(1, n//2):
    for div in dividers:
        if j < div:
            div % j ==0
            resul += f'{j} + {div-j} '

print(resul)





