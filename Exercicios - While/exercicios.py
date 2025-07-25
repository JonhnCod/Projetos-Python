listacompras = []

while True:
    print(''' ****** Menu de opcoes ******
1 - Adicionar item
2 - Remover item 
3 - Ver lista 
4 - sair  ''')
    opcao = int(input("Escolha uma opcao: "))
    if opcao == 1:
        item = input("Digite um item: ")
        listacompras.append(item)
    if opcao == 2:
        itemRemove = input("digite o item que deseja remover: ")
        listacompras.remove(itemRemove)
    if opcao == 3 :
        print(listacompras)
    if opcao == 4 :
        break

      
        