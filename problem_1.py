
import numpy as np 
from numpy import linalg

n = int(input("Digite um valor para a quantidade de linhas e colunas: "))

def make_matrix():
    m = []
    for i in range(n):#laço que seta os valores para cada elemento da matriz
        line = []
        for j in range(n):
            number = int(input("Digite o valor dos elementos ["+ str(i) +"]["+ str(j) +"]: "))
            if number >= -100 and number <= 100:
                line.append(number)
            else:
                print("Escolha um numero entre -100 e 100")
                make_matrix() 


        m.append(line)#criando a matriz completa

    matrix = np.array(m)#transformando a lista em matriz 
    print(matrix)
    result = np.linalg.det(matrix)#função que calcula o determinante da matriz construida acima
    print("O determinante em número absoluto da matrix:")
    print("{:.2f}".format(result)) 

make_matrix()




