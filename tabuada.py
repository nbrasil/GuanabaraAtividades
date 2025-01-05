num = int(input('Digite um número para ver a sua tabuada: '))
x = 1
for i in range(1,11,1):
    print(f'{num}x{x}={num*x}')
    x += 1
