import time

#Versão interativa
def cronometro_interativo(n):
    print('Início')
    while n >= 0:
        print(n)
        time.sleep(1) #Para a execução do programa por 1seg
        n -= 1
    print('Fim')

cronometro_interativo(10)

#Forma recursiva
def cronometro_recursivo(n):
    #1. Caso base: Evita o loop infinito
    if(n < 0):
        print('Fim')
        return 
    #2. Ação que a função vai executar
    print(n)
    time.sleep(1)
    cronometro_recursivo(n-1)

cronometro_recursivo(10)