def menu():
    print("""
Seja bem-vindo ao nosso aplicativo!
Selecione a opção abaixo:
        """)

def escolha_opcao():
    print("""
[1] Adicionar Item a Lista
[2] Excluir item da lista
[3] Lista completa
[4] Sair
        """)
    opcao = int(input("Digite a opção: "))
    return opcao

def adicionar_item(lista, valor_total, item):
    if any(produto['nome'] == item.title() for produto in lista):
        print("O item já está na lista!")
    else:
        item = item.title()
        valor = float(input("Digite o valor: "))
        lista.append({"nome": item, "valor": valor})
        valor_total += valor
        print("Item adicionado com sucesso!")

    return lista, valor_total

def excluir_item(lista, valor_total, item):
    item = item.title()
    for produto in lista:
        if produto['nome'] == item:
            lista.remove(produto)
            valor_total -= produto['valor']
            print("O item foi excluído com sucesso!")
            return lista, valor_total
    print("O item não existe na lista, portanto nada foi alterado!")
    return lista, valor_total

def lista_completa(lista, valor_total):
    resultado = ''
    for produto in lista:
        item_compra = f"""
------------------
Item: {produto['nome']}
Valor: {produto['valor']}
        """
        resultado += item_compra
    resultado += f"\nValor total: {valor_total}"
    print(resultado)

def main():
    menu()
    valor_total = 0
    lista = []

    while True:
        opcao = escolha_opcao()

        if opcao == 1:
            item = input("Nome do item: ")
            lista, valor_total = adicionar_item(lista, valor_total, item)

        elif opcao == 2:
            item = input("Digite o item que deseja remover: ")
            lista, valor_total = excluir_item(lista, valor_total, item)

        elif opcao == 3:
            lista_completa(lista, valor_total)

        elif opcao == 4:
            print("Saindo do aplicativo...")
            break

if __name__ == "__main__":
    main()