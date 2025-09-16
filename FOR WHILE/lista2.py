numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
numeros.insert(1, 15)
print("Lista final (Questão 1):", numeros)




lista = [5, 10, 15, 20, 25]
lista.remove(10)
lista.pop()
lista.pop(0)
print("Lista final (Questão 2):", lista)




valores = [8, 3, 10, 1, 7]
print("Lista original:", valores)
valores.sort()
print("Ordem crescente:", valores)
valores.sort(reverse=True)
print("Ordem decrescente:", valores)
valores.reverse()
print("Lista invertida:", valores)



notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print("Quantidade de notas:", len(notas))
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
