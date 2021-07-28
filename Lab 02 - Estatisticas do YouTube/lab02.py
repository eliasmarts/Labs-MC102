nome_canal = input()

N = int(input())
soma_18 = 0
dias_18 = 0
soma_19 = 0
dias_19 = 0
soma_20 = 0
dias_20 = 0

# analisa a entrada e joga na soma do ano
for i in range(N):
    data = input().split('-')
    views = int(input())
    if data[0] == '2018':
        soma_18 += views
        dias_18 += 1
    elif data[0] == '2019':
        soma_19 += views
        dias_19 += 1
    elif data[0] == '2020':
        soma_20 += views
        dias_20 += 1

#calculo das estatisticas
total_view = soma_18 + soma_19 + soma_20
media_view = total_view / (dias_18 + dias_19 + dias_20)
if total_view != 0:
    p_18 = (soma_18 / total_view)*100
    p_19 = (soma_19 / total_view)*100
    p_20 = (soma_20 / total_view)*100

med_18 = soma_18 / dias_18
med_19 = soma_19 / dias_19
med_20 = soma_20 / dias_20

print('Canal:', nome_canal)
print('Total de views do trienio:', total_view)
print('Media de views do trienio:', format(media_view, '.2f'))
print('')

print('2018')
print('Total:', soma_18)
if total_view != 0:
    print('Porcentagem das views do trienio:', format(p_18, '.2f'))
else:
    print('Porcentagem das views do trienio: indeterminada')
print('Media:', format(med_18,'.2f'))
print('')

print('2019')
print('Total:', soma_19)
if total_view != 0:
    print('Porcentagem das views do trienio:', format(p_19, '.2f'))
else:
    print('Porcentagem das views do trienio: indeterminada')
print('Media:', format(med_19,'.2f'))
print('')

print('2020')
print('Total:', soma_20)
if total_view != 0:
    print('Porcentagem das views do trienio:', format(p_20, '.2f'))
else:
    print('Porcentagem das views do trienio: indeterminada')
print('Media:', format(med_20,'.2f'))
