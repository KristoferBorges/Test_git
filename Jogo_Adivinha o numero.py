import random
import emoji

print('\n')
print('\033[34mCOMPUTADOR: Vamos brincar de adivinha!\033[m')
print('\033[36mVou pensar em um número de (1 a 6)')
print('Tente adivinhar qual estou pensando!\n')
print(emoji.emojize('Tentativas :thumbs_down:| 0 x 3 |:thumbs_up:'))

escolhido = random.randint(1, 6)

print('Você tem | 1 x 3 | chances!\033[m')
escolha = int(input('\033[33mQual número estou pensando?\n--> \033[m'))
print('\n')
if escolha != escolhido:
    print('\033[31mVocê errou! HaHa, tente de novo!')
    print('| 2 x 3 | chances!\033[m')
    escolha = int(input('\033[33mQual número estou pensando?\n--> \033[m'))
    print('\n')
    if escolha != escolhido:
        print('\033[31mVocê errou mais uma vez! HaHa, tente de novo!')
        print('| 3 x 3 | chances!\033[m')
        escolha = int(input('\033[33mQual número estou pensando?\n--> \033[m'))
        print('\n')
        if escolha != escolhido:
            print('\033[31mVocê não ganhou de mim! HaHa.')
            print('acabou suas chances!')
            print('O número era:\033[m {}{}{}'.format('\033[32m', escolhido, '\033[m'))
            print('\033[1;36mObrigado por jogar!\033[m')
            print('\n')
        else:
            print('\033[36mUol, você adivinhou!| 3 x 3 |')
            print('O número era:\033[m \033[32m{}\033[m'.format(escolhido))
            print('\033[1;36mObrigado por jogar!\033[m')
            print('\n')
    else:
        print('\033[36mUol, você adivinhou!| 2 x 3 |')
        print('O número era:\033[m \033[32m{}\033[m'.format(escolhido))
        print('\033[1;36mObrigado por jogar!\033[m')
        print('\n')
else:
    print('\033[36mUol, você adivinhou!| 1 x 3 |')
    print('O número era:\033[m \033[32m{}\033[m'.format(escolhido))
    print('\033[1;36mObrigado por jogar!\033[m')
    print('\n')
