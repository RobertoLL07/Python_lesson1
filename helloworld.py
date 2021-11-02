var = "mundo"
num = 1234
num2 = 5678

flotante = 123.4
flotante2 = 456.31
carac = 'c'
carac2 = 'd'

bol = True
bol2 = False
bol3 = None


print(var)
print(carac + carac2)
print(var + carac)

print(num + num2)
print(flotante + flotante2)

print(not bol)
print(not bol2)
print(bol or bol2)
print(bol and bol2)

if 10 > 5:
    print('10 es mayor que 5')
elif 10 > 5:
    print('Eso es imposible viejo')

if bol:
    print ('Usamos la variable bol')

if True:
    print('Es verdadero')

if not False:
    print ('La negaion es falso')

var_rapida = 0

while bol != bol2:
    if var_rapida > 10:
        bol = False
    print(var_rapida)
    var_rapida += 2
print("-------------")

for i in range(1, 101):
    if(i % 2 == 0):
        print(i)
        i += 1
    else:
        i += 1

print("------")

for i in range(1, 101):
    if(i % 2 == 0):
        i += 1
    else:
        print(i)
        i += 1
