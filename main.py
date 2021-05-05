lista = list(range(30))

print(lista)
print(len(lista))

for num in lista:
    lista[num] = 2*num

print(lista)
print(len(lista))