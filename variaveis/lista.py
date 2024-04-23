#Declaração

minha_lista = [1,2,3,4,5, "rocktseat", True, False]
minha_lista = [1,2,3,4,5, 6,7,8]

print("Minha lista de exemplo=", minha_lista)

#minha_lista[0]='python'
print("Minha lista de exemplo=", minha_lista)

print("minha_lista[0]=",minha_lista[0])
print("minha_lista[5]=",minha_lista[5])

print("minha_lista[1:7]=",minha_lista[1:7])

print("minha_lista[:6]=",minha_lista[:6])

print("minha_lista[2:]=",minha_lista[2:])

#Métodos de lista

minha_lista.append(6)

print("Após append=", minha_lista)

indice = minha_lista.index(6)

print("Indice do elemento 6=", indice)


minha_lista.insert(2,10)

print("Após insert=", minha_lista)

elemento_removido =  minha_lista.pop(3)

print("Elemento Removido=", elemento_removido)
print("Minha lista após pop=", minha_lista)

minha_lista.remove(True)
print("Minha lista após remove=", minha_lista)

# Método sort
# minha_lista = [1, 10, 3, 3, 5, 6, 7, 8, 112]
minha_lista.sort()
print("Após sort()", minha_lista)
