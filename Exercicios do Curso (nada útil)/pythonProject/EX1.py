Nome = input('Digite seu nome:')
P1 = float(input('Nota P1:'))
P2 = float(input('Nota P2:'))
P3 = float(input('Nota P3:'))
T1 = float(input('Nota T1:'))
T2 = float(input('Nota T2:'))
T3 = float(input('Nota T3:'))

MF = (P1 + P2 + P3 + ((T1 + T2 + T3) / 3) ) / 4

print("Media final do aluno %s:" % Nome)
print("%f" % MF)

if MF > 7:
    print("%s está APROVADO" % Nome)
elif MF == 7:
    print("%s passou na rabiola, com o cu cravado" % Nome)
else:
    print("%s está REPROVADO" % Nome)
