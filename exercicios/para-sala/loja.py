# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

# exclui o import time porque não sei o que vou immportar.
  

                                                       #### REALIZADO EM GRUPO####


lista_produtos = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

id_produto = 1
def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            mostrar_todos_os_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
           deletar()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)



def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):  # o get vai servir para puxar a lista do dicionário.
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


def mostrar_todos_os_detalhes():   # usei para definir a função e retorná-la.
    mostar_item = int(input("Insira a id:"))
    
    for index in lista_produtos:  
        if mostar_item == index.get("id"): 
           print(f"{index}")  # usei o "f" para imprimir dentro do texto.

def deletar():
    apagar_produto = int(input("Insira o número de id que precisa apagar:"))

    for index in range(len(lista_produtos)): 
        if index < len(lista_produtos):     
            if lista_produtos[index].get("id") == apagar_produto:
                lista_produtos.pop(index)   
                print("O item foi apagado com sucesso!")   
# usei o len é pra definir o tamanho e números de itens. Coloquei o comentário embaixo pois o código estava dando erro quando estava na linha 95.  

menu()
