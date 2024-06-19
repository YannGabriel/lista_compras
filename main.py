

def menu():
  print("""
Seja bem vindo ao nosso aplicativo!
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
  if item in lista:
    print("O item já esta na lista!")
    
  else:
    item = item.title()
    valor = float(input("Digite o valor: "))
    lista.append({"nome": item, "valor": valor})
    valor_total += valor
    
    print("Item adicionado com sucesso!")
    return lista, valor, valor_total
  
def excluir_item(lista, valor_total):
  item = input("Digite o item que deseja remover: ").title()
  if item in lista:
    lista.remove(item)

    print("O item foi excluido com sucesso!")
    return lista, valor_total
  else:
    print("O item não existe na lista, portanto nada foi alterado!")
  
  return lista, valor_total

def lista_completa(lista, valor_total):
    resultado = ''
    for item in lista:
        item_compra = f"""
------------------
Item: {item['nome']}
Valor: {item['valor']}
        """
        resultado += item_compra
    resultado += f"\nValor total: R${valor_total}"
    print(resultado)
    
def main():
  menu()
  valor_total = 0
  lista = [] 
  
  while True :
    
    opcao = escolha_opcao()
    
    if opcao == 1:
      item = input("Nome do item: ")
      adicionar_item(
        lista = lista, 
        valor_total = valor_total, 
        item = item, 
        )
      
    elif opcao == 2: 
      item = input("Digite o item que deseja remover: ")
      excluir_item(lista, valor_total = valor_total)
      
    elif opcao ==3:
      lista_completa(lista, valor_total)
      
    elif opcao ==4:
      print("""
Obrigado por acessar nosso aplicativo!

Volte sempre!
            """)
main()
  