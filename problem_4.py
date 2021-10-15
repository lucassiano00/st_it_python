import re

pm = []
lista = []
cont = 0
cont_2 = 0

with open("coordenadas.txt", "r") as archive:
    coordinates = archive.read()


#fução para remover todos os caracteres espaços e etc
coordinates = re.sub('[^0-9-]', '', coordinates)

#loop para reconhecer numeros negativos
for i in coordinates:
    if coordinates[cont] == '-':
        aux = cont + 1
        co_aux = coordinates[cont] + coordinates[aux]
        lista.append(co_aux)       
    else:
        lista.append(coordinates[cont])

    cont = cont + 1

int_list = list(map(int, lista))

#laço para remover numeros repetidos 
for i in int_list:
    if int_list[cont_2] < 0 :
        aux = cont_2 + 1
        int_list.pop(aux)
    cont_2 = cont_2 + 1    

#setando os valores dos pontos A e B
Ax = int_list[0]
Ay = int_list[1]
Bx = int_list[2]
By = int_list[3]

#função para fazer o calculo da media entre os dois pontos
def calculation(Ax, Ay, Bx, By):
    
    calculation_1 = Ax + Bx
    calculation_1 = calculation_1 / 2

    calculation_2 = Ay + By
    calculation_2 = calculation_2 / 2

    pm.append(calculation_1)
    pm.append(calculation_2)
    
    return pm

print(calculation(Ax, Ay, Bx, By))

