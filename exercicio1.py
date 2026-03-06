numeros = [9, 8, 7, 6, 5]
#Interativa
def soma_lista_interativa(numeros):
    soma = 0
    for x in numeros:
        soma += x
    return soma

print(soma_lista_interativa(numeros)) #35

#Recursiva
def soma_lista_recursiva(lista, tamanho):
    #1. Caso base:
    if tamanho < 1:
        return 0
    #Passo recursivo
    return lista[tamanho - 1] + soma_lista_recursiva(lista, tamanho - 1)

print(soma_lista_recursiva(numeros, len(numeros))) #35

    