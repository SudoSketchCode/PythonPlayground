#Calcula a raiz quadrada de um valor ataves do 
#metodo de Newton.

passos = 0
controle = 0
raiz = int(input("Digite a raiz: "))
paupite = int(input("Digite um paupite: "))

def calcula(paupite, raiz):
    return( 0.5 * ( paupite + ( raiz / paupite )))


while paupite != controle:
    passos += 1
    controle = paupite
    paupite = calcula(paupite, raiz)
    print(str(passos) + " - " + str( paupite))

