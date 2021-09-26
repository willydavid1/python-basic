# Tiene mejor performance vs las listas.
# Las tuplas son objetos inmutables. Los valores son constantes no se pueden modificar como las listas

tuple = (1, 2, 3, 4, 5)

# tuple.append(6) # Error

print(f'len(tuple): {len(tuple)}')

for i in tuple:
    print(i)
