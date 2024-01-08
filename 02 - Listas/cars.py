carros = ['bmw', 'audi', 'toyota', 'subaru']

# Altera a ordem dos elementos de forma definitiva dentro da lista
# carros.sort()
# print(carros)

# Ordenando de forma reversa
# carros.sort(reverse=True)
# print(carros)

# A função sorted preserva a ordem original na lista
print("Aqui está a lista original:")
print(carros)

print("Aqui está a lista ordenada:")
print(sorted(carros))

print("Aqui está a lista original:")
print(carros)

print("Aqui está a lista ordenada (reverse):")
print(sorted(carros, reverse=True))

print("Aqui está a lista original:")
print(carros)

# Inverter a ordem da lista
print("Aqui está a lista em ordem inversa:")
carros.reverse()
print(carros)
