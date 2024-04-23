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