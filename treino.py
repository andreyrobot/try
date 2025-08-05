# lista de mercado
lista = []
while lista !=0:
    compras = int(input("O que deseja Comprar: \n\n 1- Adicionar produto📥 \n 2- Ver Produtos Comprados👁️🗃️ \n 3- Modificar Produto↔🔂 \n 4- Remova Algum Produto \n"))
    if compras == 1:
        Produto = input("Qual Produto Deseja inserir?: \n\n")
        lista.append(Produto)
        print(f"\n Produto adicionar com Sucesso ! ➕{Produto}:\n\n")
    elif compras == 2:
        print(lista)
        try:
    elif compras == 3:
        Modificar = input("Modifique o Produto que deseja (●'◡'●): \n\n")
        if Modificar in lista:
            novo = input("Qual o Produtop Novo?: \n")
            index = lista.index(Modificar)
            lista[index] = novo
            print(f"Sua Lista Foi Atualizada🆕...:\n")
            print(lista)
    print("item não encontrado")
    elif compras == 4:
    Produto = input("digite o Produto Que deseja Remover: \n\n ")
lista.remove(Produto)
print(f"Seu item Foi Removido Com Sucesso❎")
print(lista)
except:
print("item não encontrado")