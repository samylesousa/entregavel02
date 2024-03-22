quant_tarefas = int(input("Quantas tarefas seu sistema vai executar?"))

tarefas_tempo = {}
tarefas_intervalo = {}
tarefas_prioridade = {}

for i in range(quant_tarefas):
    chave = input("Qual o nome da tarefa: ")
    valor = int(input("Qual a duração para ela ser executada? (tempo de execução) "))
    intervalo = int(input("Em qual intervalo (período) ela deve ser repetida? "))
    prioridade = int(input("Qual a prioridade RM dessa tarefa? "))
    tarefas_tempo[chave] = valor
    tarefas_intervalo[chave] = intervalo
    tarefas_prioridade[chave] = prioridade

tarefasPrioridade = sorted(tarefas_prioridade)
resultado = 0
print(tarefasPrioridade)

#calculando a escabilidade
for i in range(quant_tarefas):
    resultado = resultado + (tarefas_tempo[tarefasPrioridade[i]]/tarefas_intervalo[tarefasPrioridade[i]])

print(resultado)
print((quant_tarefas*(2**(1/quant_tarefas))-1))
if(resultado <= (quant_tarefas*(2**(1/quant_tarefas))-1)):
    print("Escalonável")
else:
    print("Não escalonável")