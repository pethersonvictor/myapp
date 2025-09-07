import json
import os

if os.path.exists("tarefas.json"):
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []

def adicionar_tarefas():
    nova_tarefa = input ("Adicione uma nova tarefa à lista:")
    tarefas.append(nova_tarefa)
    print("Nova tarefa adionada!", tarefas)
adicionar_tarefas()

salvar_tarefas = input("Desaja salvar suas tarefas? (s/n): ")
if salvar_tarefas == "s":
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)
        print("Tarefa salva!!")
else:
    print("Tarefa não foi salva.")