nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}\nSeu nome invertido é {nome[::-1]}\nA primeira letra do seu nome é {nome[0]}\nA última letra do seu nome eh {nome[-1]}\nSeu nome tem {len(nome)} letras')

    if ' ' in nome:
        print('Seu nome possui espaços')
    else:
        print('Seu nome não possui espaços')
else:
    print('Desculpe, você deixou campos em branco')