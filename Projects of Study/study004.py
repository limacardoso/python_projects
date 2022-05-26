print('=' * 41)
print('Sorteio'.upper().center(41))
print('=' * 41)

'''qtd = int(input('Quantos nomes a sua lista terá? '))
while True:
    per = ' '
    while per not in 'SN':        
        for c in range (0, qtd):
            nome = str(input('nome: '))    
        per = str(input('Mais algum nome [S/N]? ').upper().strip()[0])
    if per == 'N':
        print('Fim')
        break              
    qtd = int(input('Quantos nomes? '))              
    if qtd == 0:
       print('Fim')
       break'''
       
from random import randint, choice
from time import sleep
qtd = int(input('Quantos nomes a sua lista terá? '))
lista = [ ] 
while True:
    per = ' '
    while per not in 'SN':        
        for c in range (0, qtd):
            nome = str(input('nome: '))    
            lista.append(nome)            
        per = str(input('Mais algum nome [S/N]? ').upper().strip()[0])                    
    if per == 'N':
        print('')
        print('-' * 41)
        print('Entao, vamos ao sorteio, em...')
        sleep(1)
        print ('3...') 
        sleep(1)
        print('2...')
        sleep(1) 
        print('1...')  
        sleep(1)       
        sorteado = choice(lista)
        #print(sorteado)
        print('')
        print('-' * 41)
        print(f'        parabéns, \033[1;92m{sorteado}\033[m!!'.center(41))   
        print('Você foi sorteado(a)!'.center(41))
        print('-' * 41)   
        print('')
        print('Confira a lista com os nomes dos participantes deste sorteio:\n')         
        print(lista)
        break   
    qtd = int(input('Quantos nomes? '))              
    if qtd == 0:
        print('Entao, vamos ao sorteio, em...')
        sleep(1)
        print('3...') 
        sleep(1)
        print('2...')
        sleep(1) 
        print('1...')  
        sleep(1)
        sorteado = choice(lista)
        #print(sorteado)
        print('parabéns, \033[1;92m{sorteado}\033[m!!')
        print('Você foi sorteado(a)!')
        print(lista)
        break
    
 