while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if nota >= 0 and nota <= 10:
        break  # Sai do loop se a nota for válida
    
    print("Valor inválido! Digite uma nota entre zero e dez.")

print("Nota válida informada:", nota)
