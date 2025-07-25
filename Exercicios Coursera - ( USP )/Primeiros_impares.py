n = int(input("Digite a quantidade de números ímpares a serem impressos: "))

impares = 0
numero = 1

while impares < n:
    if numero % 2 != 0:
        print(numero)
        impares += 1
    numero += 1
 
    
