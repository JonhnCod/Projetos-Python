numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print( "não primo.")
else:
    divisor = 2
    primo = True

    while divisor <= numero**0.5:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print("Primo")
    else:
        print("não primo.")
