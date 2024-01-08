lista_convidados = ["Veronica", "Laura", "Joao"]

for convidado in lista_convidados:
    print(f"Olá {convidado}, você está convidado para minha festa!")

print(f"O convidado {lista_convidados[-1]} não poderá comparecer!")

lista_convidados[-1] = "Pedro"

for convidado in lista_convidados:
    print(f"Olá {convidado}, você está convidado para minha festa!")

print("Encontrada nova mesa com mais lugares! Incluindo novos convidados...")

lista_convidados.insert(0, "Marcos")
lista_convidados.insert(int(len(lista_convidados)/2), "Carlos")
lista_convidados.append("Luis")

print(f"Ao todo foram convidadas {len(lista_convidados)} pessoas!")

for convidado in lista_convidados:
    print(f"Olá {convidado}, você está convidado para minha festa!")

print("Infelizmente a mesa não chegará a tempo, apenas dois convidados poderão participar...")

max_convidados = len(lista_convidados) - 2
i = 0

while i < max_convidados:
    convidado_excluido = lista_convidados.pop()
    print(f"{convidado_excluido}, infelizmente você foi excluído do jantar...")
    i += 1

for convidado in lista_convidados:
    print(f"Olá {convidado}, você está convidado para minha festa!")

del lista_convidados[0]
del lista_convidados[0]

print(lista_convidados)
