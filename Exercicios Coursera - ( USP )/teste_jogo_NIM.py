def computador_escolhe_jogada(n,m):
    computador_remove = 1
    pontos = 0
    while computador_remove != m:
        if (n - computador_remove)% (m+1) == 0:
            n-=n-computador_remove
             
            print (computador_remove)
            return usuario_escolhe_jogada(n,m)
        else:
            computador_remove+=1
    print(computador_remove)
    n-=computador_remove
    return usuario_escolhe_jogada(n,m)


def vitoria(n):
    pontos = 0
    if n == 0:
        pontos+=1
        10

def usuario_escolhe_jogada(n,m):
    while True:
        opcao = int(input("Quantas pecas deseja retirar"))
        if opcao in range(1,(m+1)):
            n-=opcao
            pontos = 0
            if n == 0:
                pontos+=1
                if pontos == 3:
                    print("Parabens Voce ganhou")
                    return partida()
            print(opcao)
            print (computador_escolhe_jogada(n,m))
            break
        else:
            print("Digite uma jogada valida")
            continue

def partida():
    n = int(input("Digite a quantidade de peças"))
    m = int(input("Digite o Limite maximo para retirada"))
    if n % (m+1) == 0:
        print("Você começa")
        return usuario_escolhe_jogada(n,m)
    else:
        print("Computador comeca")
        return computador_escolhe_jogada(n,m)
    




partida()

    

            
