pnumero = int(input('Digite o primeiro número: '))
snumero = int(input('Digite o segundo número: '))
tnumero = int(input('Digite o terceiro número: '))

if pnumero > snumero and pnumero > tnumero:
    print(pnumero)
elif snumero > pnumero and snumero > tnumero:
    print(snumero)
else:
    print(tnumero)