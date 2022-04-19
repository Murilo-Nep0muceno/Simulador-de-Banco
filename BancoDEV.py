from time import sleep
print('='*30)
print('{:^30}'.format('BANCO DEV'))
print('='*30)
nome=''
senha= 0
ação=0
dinhero=0
dinhero1=0
deposito=''
sair =''
pase=''
deseja='S'
print('{:^20}'.format('Selecione uma opção abaixo'))
opcao=int(input('''Seja bem Vindo ao banco DEV
 [ 1 ] Cadastro
 [ 2 ] sair
 Digite uma: '''))
while True:
    if opcao == 1:
        if pase == 'PASS':
            ação = int(input('''Selecione uma opção abaixo
[ 1 ] Deposito
[ 2 ] Saque
[ 3 ] Dinheiro em Conta
[ 4 ] Sair
Qual oção desejada? '''))
        else:
            nome= str(input('Digite Seu primeiro nome: ')).strip()
            senha = int(input('Digite sua senha: '))
            print(f'Parabens {nome} Você foi cadastrado no Banco DEV\nREDIRECIONANDO...')
            sleep(1)
            ação=int(input('''Selecione uma opção abaixo
[ 1 ] Deposito
[ 2 ] Saque
[ 3 ] Dinheiro em Conta
[ 4 ] Sair
Qual oção desejada? '''))
        if ação == 1:

            dinhero1=int(input('Qual o valor que você quer depositar? R$'))
            dinhero+=dinhero1
            print('Contando...')
            sleep(1)
            print(f'Depositado o valor de R${dinhero}')
            sair=str(input('Deseja Finalizar a seção? [S/N]')).upper().strip()[0]
        elif ação == 2:
            valor = int(input('Digite o valor do saque: R$'))
            if dinhero == valor:
                total = valor
                ced = 100
                totalced = 0
                while True:
                    if total >= ced:
                        total -= ced
                        totalced += 1
                    else:
                        if totalced > 0:
                            print(f'foi {totalced} cédulas de R${ced}')
                        if ced == 100:
                            ced = 50
                        elif ced == 50:
                            ced = 20
                        elif ced == 20:
                            ced = 10
                        elif ced == 10:
                            ced = 1
                        totalced = 0
                        dinhero-=dinhero
                        if total == 0:
                            break
            else:
                print(f'Você não tem o Valor digitado\n (dinheiro na carteira de R${dinhero})')
                dinhero1 =int(input('Faça o deposito Agora R$'))
                deseja =str(input('Deseja sacar? [S/N]')).strip().upper()[0]
                if deseja == 'S':
                    total = valor
                    ced = 100
                    totalced = 0
                    while True:
                        if total >= ced:
                            total -= ced
                            totalced += 1
                        else:
                            if totalced > 0:
                                print(f'foi {totalced} cédulas de R${ced}')
                            if ced == 100:
                                ced = 50
                            elif ced == 50:
                                ced = 20
                            elif ced == 20:
                                ced = 10
                            elif ced == 10:
                                ced = 1
                            totalced = 0
                            if total == 0:
                                break
                else:
                    ação = int(input('''Selecione uma opção abaixo
[ 1 ] Deposito
[ 2 ] Saque
[ 3 ] Dinheiro em Conta
[ 4 ] Sair
Qual oção desejada? '''))
                    pase='PASS'
        elif ação == 3:
            print(f'Você tem R${dinhero} em sua conta\nO que desejas fazer?')
            ação =int(input('''Digite [ 1 ] para voltar'''))
            pase='PASS'
        elif ação == 4:
            print(f'Obrigado {nome}, Por escolher o Banco DEV ')
            print('Finalizando...')
            sleep(2)
            break
        else:
            ação = int(input('''Selecione uma opção abaixo
            [ 1 ] Deposito
            [ 2 ] Saque
            [ 3 ] Dinheiro em Conta
            [ 4 ] Sair
            Qual oção desejada? '''))
    elif opcao == 2:
        print('Obrigado por usar o banco DEV, tenha um Bom dia')
        break
        print('Fim do Programa')
    else:
        print('Por favor digite uma opção corretamente')
        opcao = int(input('''Seja bem Vindo ao banco DEV
[ 1 ] Cadastro
[ 2 ] sair
Digite uma: '''))

    if sair == 'S':
        break
    elif sair == 'N':
        pase='PASS'




