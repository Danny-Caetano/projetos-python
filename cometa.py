from datetime import date
from time import sleep

atual = date.today().year
nsc = int(input('\033[35mQual seu ano de nascimento?: \033[m'))
idade = atual - nsc
ano = 1986
cometa = 76
expec = 2061


if nsc > ano:
    idade_atual = expec - nsc
    print('\033[32mVocê conseguirá ver Harley quando estiver\033[m')
    print(f'no ano de \033[32m{expec}\033[m')
    print(f'Estará com \033[32m{idade_atual}\033[m anos')
elif nsc < ano:
    idade_atual2 = ano - nsc
    idade2 = expec - nsc
    print(f'Última vez em que o cometa Harley passou foi no ano de \033[32m{ano}\033[m')
    print(f'No auge dos seus \033[32m{idade_atual2}\033[m anos...')
    print(f'Ele passará a próxima vez no ano de \033[32m{expec}\033[m')
    print(f'Você estará com \033[32m{idade2}\033[m anos')