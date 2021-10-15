from collections import defaultdict

list_1 = []
list_2 = []
list_aux_1 = []
list_aux_2 = []
  
dict_1 = {}

list_1.append(input("Frase 1: "))
list_2.append(input("Frase 2: "))

#função para separar as palavras da frase e remover espaços etc...
list_1 = ''.join(list_1) 
list_2 = ''.join(list_2)

x = list_1.split()
y = list_2.split()


#juntando as listas com as duas frases e separando cada palavra
list = []

list = x + y

new_list = set(list)

#laço que separa os itens que se repete e os que não se repetem
for i in new_list:
    if(list.count(i) > 1):
        list_aux_1.append(i)
    else:
        list_aux_2.append(i)

dict_1 = {
        'Iguais' : list_aux_1,
        'Diferentes' : list_aux_2,
    }
    
print(dict_1)
 