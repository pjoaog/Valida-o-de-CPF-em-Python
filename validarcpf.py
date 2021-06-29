cpf = list()
cpfnum = dict()
cpft = list()
cpfr = list()

quantv = 0
quantiv = 0
quant = 0
while True:
    quant += 1
    resultvalid = ' '
    soma = 0
    dig1 = 0
    dig2 = 0
    num = input('Digite seu CPF completo (sem pontos e traços): ')
    test = num.isdigit()
    while len(num) > 11 or len(num) < 11 or test == False:
        num = input('CPF não aceito, digite novamente: ')
        test = num.isdigit()

    for x in num:
        x = int(x)
        cpf.append(x)

    cpft = cpf[0:9]
    y = 10
    res = 0
    for x in range(0,9):
        res = y * cpft[x]
        soma += res
        y -= 1

    resto = soma % 11
    if resto < 2:
        cpft.append(0)
        dig1 = 0
    else:
        res = 11 - resto
        cpft.append(res)
        dig1 = res

    z = 11
    soma2 = 0
    res2 = 0
    for x in range(0,10):
        res2 = z * int(cpft[x])
        soma2 += res2
        z -= 1

    resto2 = soma2 % 11
    if resto2 < 2:
        cpft.append(0)
        dig2 = 0
    else:
        res2 = 11 - resto2
        cpft.append(res2)
        dig2 = res2

    if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
        print('CPF válido!')
        resultvalid = 'CPF válido!'
        quantv += 1
    else:
        print('CPF inválido!')
        resultvalid = 'CPF inválido!'
        quantiv += 1

    cpfnum = {'CPF':cpf, 'validação':resultvalid}
    cpfr.append(cpfnum)

    del(cpf)
    cpf = []
    del(cpfnum)
    cpfnum = []
    del(cpft)
    cpft = []

    resp = str(input(('\nDeseja continuar testando CPFs? S/N: ')))
    print('')
    if resp != 'S':
        break

pcv = int((quantv / quant) * 100)
pciv = int((quantiv / quant) * 100)
print(f'{cpfr}')
print(f'\nQuantidade de CPFs testados: {quant}')
print(f'Quantidade de CPFs válidos: {quantv}')
print(f'Quantidade de CPFs inválidos: {quantiv}')
print(f'Porcentagem de CPFs válidos: {pcv}%')
print(f'Porcentagem de CPFs inválidos: {pciv}%')