frutas = ["maça", "banana", "laranja" , "morango"]
frutas.append("PERA") # ele adiciona no final da lista
print(frutas) # imprime ["maça", "banana", "laranja" , "morango"]

frutas.insert(1, "uva") # ele adiciona no lugar que eu quiser
print(frutas) # imprime ["maça", "uva", "banana", "laranja]

frutas.remove("banana") # ele remove o elemento que eu quiser
print(frutas) # imprime ["maça", "uva", "laranja"]

fruta_removida = frutas.pop(2) # ele remove o elemento que eu quiser e retorna ele
print(frutas) # imprime ["maça", "uva", "pera"]
print(fruta_removida) # imprime laranja

frutas.sort()# ele ordena a lista
print(frutas) # imprime ["pera", "uva", "maça"]

frutas.reverse() # ele inverte a lista  
print(frutas) # imprime ["maça", "uva", "pera"]

for i in range(10): 

    if i % 2 == 0: #
        continue 
    print(i) # imprime todos os números impares de 0 a 9

    