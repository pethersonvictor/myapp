import json
import os

if os.path.exists("tarefas.json"):
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []

def mostrar_tarefas():
    print("Essas são todas suas taferas disponíveis:" + str(tarefas))
mostrar_tarefas()

def remover_tarefas():
    mostrar_tarefas()
    numero = int(input("Digite o numero da tarefa que você quer remover (Começa do 0): "))
    if 0 <= numero <len(tarefas):
        tarefa_removida = tarefas.pop(numero)
        print(f"Tarefa removida: {tarefa_removida}")
    else:
        print("Número inválido.")
remover_tarefas()
