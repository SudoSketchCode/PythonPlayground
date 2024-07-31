# Este código busca e lista números primos. 
# O método consiste em encontrar divisores de um inteiro usando números primos já encontrados,
# Os números primos utilizados devem ser menores do que a metade do inteiro em questão. 
# O algoritmo funciona em um loop infinito, listando números primos cada vez maiores.


inteiro = 2
primos = [2]

while True:
    inteiro += 1
    primos.append(inteiro)

    for operando in primos:

        if inteiro/2 <  operando:
            print(str(inteiro) + " é primo!")
            break

        if inteiro % operando == 0:
            del primos[-1]
            break
