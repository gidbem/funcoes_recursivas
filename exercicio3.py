'''
Sequência de Fibonacci: 
Implemente uma função recursiva que receba um número n e retorne o 
n-ésimo termo da sequência de Fibonacci (onde cada número é a soma dos dois 
anteriores: 0, 1, 1, 2, 3, 5, 8...).

'''

def fibonacci_interativo(n):
    atual = 0
    proximo = 1
    for x in range(n):
        soma = atual + proximo
        atual = proximo
        proximo = soma    
    return atual

print(fibonacci_interativo(50))


def fibonacci_recursivo(n):
    if n <= 1:
        return n
    print(n, end=' ')
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

print(fibonacci_recursivo(50))