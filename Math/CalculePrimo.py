#Procura e lista numeos primos.

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
