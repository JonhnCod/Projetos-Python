A = float(input("Digite o valor de 'A': "))
B = float(input("Digite o valor de 'B': "))
C = float(input("Digite o valor de 'C': "))
delta = (B**2) - (4*A*C)
raiz1 = (-B + delta ** (1/2)) / (2*A)
raiz2 = (-B - delta ** (1/2)) / (2*A)
print(delta,raiz1,raiz2)
        
