import random
lista_palavras = [
    'abacaxi',
    'laranja',
    'uva',
    'banana'
    'limao'
]

palavra = random.choice(lista_palavras)

letras_usadas = []

palavra_descobrir = "_"*len(palavra)
erro = 0
while "_" in palavra_descobrir:
    letra = input("Digite a letra: ")
    if letra in letras_usadas:
        print("Letra ja foi utilizada")
        continue
    else:
        letras_usadas.append(letra)
    if letra not in palavra:
        erro+=1
        if erro < 5:
            print(f'-> Você errou pela {erro}ª vez. Tente de novo!')
        elif erro == 5:
            print(f'Você errou pela {erro}ª vez. Essa e sua ultima chance!!')
        else:
            print('Fim de jogo, Voce perdeu!!!')
            break
    else:
        palavra_descobrir = "".join([ch + " " if ch in letras_usadas else "_ " for ch in palavra])
       
        

        print(f'A palavra e: {palavra_descobrir}')
if palavra.replace(" ","") == palavra_descobrir.replace(" ",""):
            print(f'Parabens voce acertou a palavra: {palavra}')
    

    

