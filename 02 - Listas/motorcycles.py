motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

# Alterando o elemento de uma lista
motorcycles[0] = 'Ducati'
print(motorcycles)

# Concatenando elemento no final da lista
motorcycles.append('Honda')
print(motorcycles)

brands = []

for brand in motorcycles:
    brands.append(brand)

print(f"Lista de marcas:{brands}")

# Inserindo elemento em uma posição determinada
brands.insert(0, 'Royal Enfield')
print(f"Lista de marcas:{brands}")

# Remover determinado elemento de uma lista por posição
del brands[0]
print(f"Lista de marcas:{brands}")

print(brands[0])

# O método pop remove o item da última posição
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

motorcycles.append('Honda')
print(motorcycles)

# Ao usar o pop podemos ainda utilizar o item removido e usando o pop por posição
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}.")
print(motorcycles)

# Removendo um item por valor
motorcycles.remove('Suzuki')
print(motorcycles)

print(brands)

# Removendo um item por valor armazenado em uma variável
too_expensive = 'Ducati'
brands.remove(too_expensive)
print(brands)
print(f"{too_expensive.title()} is to expensive for me!")
