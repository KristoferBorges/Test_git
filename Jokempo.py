import random
import time

print('\033[36mVAMOS JOGAR JOKEMPO!\033[m')
time.sleep(1)
print('\033[36mPODE ESCOLHER ENTRE \033[m')
time.sleep(0.5)
falas_comp = ['Você é fraco', 'Achei fácil', 'Isso aqui é muito chato...', 'GG izi', 'Vou fechar os olhos!',
              'Você não é páreo para mim!', 'Foi moleza!', 'Isso está ficando entediante...',
              'Vou acabar com você em um instante!', 'Isso é brincadeira de criança!',
              'Parece que você está suando frio!', 'Você é apenas um iniciante!', 'Isso não é nem um desafio para mim!',
              'Vamos ver se você consegue acompanhar!', 'Parece que eu estou jogando contra um bot!']
ganhando = False
inteligencia = True
cont = 0
ganhas = 0
perdidas = 0
while True:
    if inteligencia:
        empatou_userwin = False
        if ganhas < perdidas:
            ganhando = True
        else:
            ganhando = False
        possible_choices = ['pedra', 'papel', 'tesoura']
        computer_choice = random.choice(possible_choices)
        print('\033[36m[PEDRA - PAPEL - TESOURA]\033[m')
        print('\n')
        user_choice = str(input('\033[33mQual você escolhe: \033[m')).lower()
        if len(user_choice) == 0:
            user_choice = random.choice(possible_choices)
        if user_choice == computer_choice:
            print('-----EMPATE-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----EMPATE-----')
            empatou_userwin = True

        elif user_choice == 'tesoura' and computer_choice == 'papel':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
            ganhas = ganhas + 1
            empatou_userwin = True

        elif user_choice == 'tesoura' and computer_choice == 'pedra':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
            perdidas = perdidas + 1

        elif user_choice == 'papel' and computer_choice == 'pedra':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
            ganhas = ganhas + 1
            empatou_userwin = True

        elif user_choice == 'papel' and computer_choice == 'tesoura':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
            cont = cont - 1
            perdidas = perdidas + 1

        elif user_choice == 'pedra' and computer_choice == 'tesoura':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
            ganhas = ganhas + 1
            empatou_userwin = True

        elif user_choice == 'pedra' and computer_choice == 'papel':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
            perdidas = perdidas + 1

        else:
            print('Error')
        print(f'       {ganhas}x{perdidas}')
        if ganhando and not empatou_userwin:
            print(f'\033[34mCOMPUTADOR: ' + random.choice(falas_comp) + '\033[m')

    else:
        possible_choices = ['pedra', 'papel', 'tesoura']
        computer_choice = random.choice(possible_choices)
        print('\033[36m[PEDRA - PAPEL - TESOURA]\033[m')
        print('\n')
        user_choice = str(input('\033[33mQual você escolhe: \033[m')).lower()
        if len(user_choice) == 0:
            user_choice = random.choice(possible_choices)
        if user_choice == computer_choice:
            print('-----EMPATE-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----EMPATE-----')
        elif user_choice == 'tesoura' and computer_choice == 'papel':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
        elif user_choice == 'tesoura' and computer_choice == 'pedra':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
        elif user_choice == 'papel' and computer_choice == 'pedra':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
        elif user_choice == 'papel' and computer_choice == 'tesoura':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
        elif user_choice == 'pedra' and computer_choice == 'tesoura':
            print('-----VENCEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----VENCEDOR-----')
        elif user_choice == 'pedra' and computer_choice == 'papel':
            print('-----PERDEDOR-----')
            print('\033[33mUsuário:\033[m {}'.format(user_choice))
            print('\033[33mComputador:\033[m {}'.format(computer_choice))
            print('-----PERDEDOR-----')
        else:
            print('Error')
