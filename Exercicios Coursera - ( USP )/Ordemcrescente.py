n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
if n1 < n2 and n1 < n3 and n2 < n3:
    print("crescente")
else:
    print("não está em ordem crescente")
