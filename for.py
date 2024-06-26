lista = [1,2,3,4,5]

for elemento  in lista:
    print(elemento)


print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionatio - chaves")
for chaves in pessoa.keys():
    print(chaves)

print("\nFor utilizando dicionatio - valores")
for valores in pessoa.values():
    print(valores)

print("\nFor utilizando dicionatio - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0,1,2,3,4]
print("\n Utilizando a função range()")
for numero in range(5):
  print("Numero:", numero)

print("\n Utilizando a função range() com len()")
for indice in range(0, len(lista)):
  print("Indice:", indice)
  print("Elemento:", lista[indice])
  if indice == 3:
      lista[indice] = 5
  else:
      lista[indice]=0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(indice,valor)
    if indice == 1:
        print("Idice 1")