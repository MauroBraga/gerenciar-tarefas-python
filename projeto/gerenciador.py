
def adicionar_tarefa(tarefas,nome_tarefa):
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarrefa {nome_tarefa} foi adicionada com sucesso!")
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice,tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")


def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
  else:
    print("Índice de tarefas inválido.")

def completar_tarefa(tarefas, indice_tarefa):
  print(f"Tarefa {indice_tarefa} marcada como completada")
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    print(f"Tarefa {indice_tarefa} atualizada para completa ")
    tarefas[indice_tarefa_ajustado]["completada"] = True
  return

def deletar_tarefa():
  for tarefa in tarefas:
    if(tarefa["completada"]==True):
      tarefas.remove(tarefa)
  print("\n Tarefas completadas foram deletadas:")
  return

tarefas=[]

while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar Tarefas")
  print("4. Completar Tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha=="2":
    ver_tarefas(tarefas)
  elif escolha=="3":
    indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar:"))
    nome_tarefa = input("Digite o nome da tarefa que deseja alterar1: ")
    atualizar_nome_tarefa(tarefas,indice_tarefa,nome_tarefa)
  elif escolha == "4":
    indice_tarefa = int(input("Digite o número da tarefa que deseja completar:"))
    completar_tarefa(tarefas, indice_tarefa)
  elif escolha == "5":
    deletar_tarefa()
  elif escolha == "6":
    break

print("Programa finalizado")