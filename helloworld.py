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

if type(var_rapida) is int:
    print('Es un entero')

if type(var) is str:
    print('Es una cadena')

if type(flotante) is float:
    print('Es flotante')

if type(flotante) is int:
    print('Es entero')

arr_num = [0, 1, 2, 3]
arr_car = ['c', 'h', 'a', 'r']

print(arr_car[0])
print(arr_car[1])
print(arr_car[3])
print(len(arr_car))
print(arr_car[len(arr_car)-1])

for cualquiernombredevariable in arr_num:
    print(cualquiernombredevariable)

for i in range (5):
    print(var[i])


#print("-------------")

#for i in range(1, 101):
#    if(i % 2 == 0):
#       print(i)
#        i += 1
#    else:
#        i += 1

print("------")

#for i in range(1, 101):
#    if(i % 2 == 0):
#        i += 1
#    else:
#        print(i)
#        i += 1

#for i in range (1, 101, 2):
#    print(i)
    
c = [i for i in xrange(2,101) 
if (i%2!=0 or i==2) 
and (i%3!=0 or i==3) 
and (i%5!=0 or i==5) 
and (i%7!=0 or i==7)]
print c