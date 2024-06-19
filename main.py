

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

  
def adicionar_item(lista, valor_total, itens, item, valor):
  if item in lista:
    print("O item já esta na lista!")
  else:
    item = item.title()
    lista.append(item)
    valor_total += valor
    itens += 1
        
  print("Item adicionado com sucesso!")
  
  return lista, valor_total, itens
  
def excluir_item(lista, valor_total, itens):

  if item in lista:
    item = item.title()
    lista.remove(item)
    itens -= 1
    print("O item foi excluido com sucesso!")
  else:
    print("O item não existe na lista, portanto nada foi alterado!")
  
  return lista, valor_total


def main():
  menu()
  valor_total = 0
  lista = []
  
  while True :
    
    opcao = escolha_opcao()
    
    if opcao == 1:
      item = input("Nome do item: ")
      
      valor = float(input("Valor do item: "))
      
      adicionar_item(
        lista = lista, 
        valor_total = valor_total, 
        itens = itens, 
        item = item, 
        valor = valor
        )
      
    elif opcao == 2: 
      item = input("Digite o item que deseja remover: ")
      excluir_item(lista, valor_total = valor_total, itens = itens)
    elif opcao ==3:
      print(lista)
      print(valor_total)
      print(len(lista))
main()
  