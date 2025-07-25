import random
lista_de_palavras = [
    "banana",
    "abacaxi",
    "laranja",
    "uva",
    "limão",
    "maçã",
    "pera",
    "melão",
    "caju",
    "manga",
    "figo",
    "pêssego",
    "kiwi",
    "morango",
    "pitaya",
    "jabuticaba",
    "goiaba",
    "abacate",
    "melão",
    "coco"
]
def embaralha_palavra(palavra):
    ch_palavra = list(palavra)
    random.shuffle(ch_palavra)
    palavra_embaralhada = "".join(ch_palavra)
    return palavra_embaralhada

palavra_escolhida = random.choice(lista_de_palavras)

palavra = embaralha_palavra(palavra_escolhida)
print(palavra)
erros = 0
while True:
    if erros == 6:
        print(f'Voce perdeu!! A palavra e {palavra_escolhida}')
        break
    else:
        resposta = input("Qual a palavra: ")
        if resposta != "".join(palavra_escolhida):
            print("Voce errou")
            erros+=1
        else:
            print("parabens acertou")
            break






