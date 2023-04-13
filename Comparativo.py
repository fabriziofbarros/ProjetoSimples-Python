while True:
    print("Menu Principal")
    print("1 - Cadastrar mês de referência")
    print("2 – Exibir dados do mês de referência")
    print("3 – Relatório comparativo – Referência 2019")
    print("4 – Listar todos os meses cadastrados")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        dados = dict()
        lista = list()
        somaHabitantes = 0
        somaObitos = 0
        print("CADASTRANDO MÊS-ANO DE REFERÊNCIA")
        while True:
            dados.clear()
            dados['mes_ano'] = str(input("Digite o mês-ano desejado "))

            dados['habitantesTot'] = int(input("Digite o total de habitantes "))
            somaHabitantes += dados['habitantesTot']

            dados['obitosTot'] = int(input("Digite o total de obitos "))
            somaObitos += dados['obitosTot']

            lista.append(dados.copy())
            resp = str(input('Quer continuar? [S/N]')).upper()[0]
            if resp == 'N':
                break
        print("***** Gravado com sucesso *****")

    #########################################
    elif opcao == 2:
        print("CONSULTANDO MÊS-ANO DE REFERÊNCIA")
        mesAnoCadastrado = str(input("Digite o mês-ano desejado "))
        if mesAnoCadastrado != dados['mes_ano']:
            print("***** Mês-ano não cadastrado! *****")
            mesAnoCadastrado = str(input("Digite o mês-ano desejado "))
        else:
            print(dados)
            print("***** Registro encontrado *****")

    #########################################
    elif opcao == 3:
        print("RELATÓRIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL")
        ano = int(input("Digite ano a ser comparado "))
        print(f'Total de habitantes: {somaHabitantes}')
        print(f'Total de óbitos: {somaObitos}')
        media = somaObitos/somaHabitantes
        print(f'Taxa por 100k habitantes - {ano}: {media}%')
        print('Taxa por 100k habitantes - 2019: 15%')
        print(f'Comparativo % entre {ano}-2019: {0.15/media}')

    #########################################
    elif opcao == 4:
        for mes in lista:
            print(f'{mes["mes_ano"]}')

    else:
        print("Numero inválido")    