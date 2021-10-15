
n = int(input('Digite um número: '))
cont = 0
if n >= 1 and n <= 100:
    def list_of_dividers(n):#função para encontrar todos os numeros que dividido por (n) sobre 0 
        for x in range(1, n//2+1):
            if n % x == 0: 
                yield x#yield foi feito para me ajudar com o controle dos numeros
        yield n

    #laço para contar quantos divisores o (n) tem
    for i in list(list_of_dividers(n)):
        if i % 2 == 0:
            cont = cont + 1
    
    print('Divisores: ',list(list_of_dividers(n)))
    print('output: ', cont)
else:
    print('O numero tem que ser entre 1 e 100!')    