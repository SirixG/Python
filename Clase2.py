x = 1
print(type(x))
x=[1,2,3]
y=x
print(x)

#modificacion con metodo
x.append(4)
print(y)

#Evaluacion de datos simples

dato_num = 8
dato_float = 8.1
dato_booleano_1 = True
dato_booleano_2 =False
dato_string = "Soy Alan"

print(dato_num)
print(type(dato_float))

#Datos estructurados (Dict) diccionario = { key: value, key: value , ……………..}

persona = {'nombre':'Alan','edad':18,'profesion':'Finanzas'}
print(persona['nombre'])

print(type(persona))

#Listas
my_list = [1,5,3,2,'tres',5.21,'hi']
print(my_list[2])
print(type(my_list))

my_tuple = (2,3,4,1)
print(my_tuple)
print(type(my_tuple))

#Estructuras de control
#Sintaxis para ejecutar estrucutras de control

#For
rango = range(1,10)
print(type(rango))

print('el primer elemento es: ', rango[0])

for i in rango: 
    a = i +1
    b = a*i

    print(i,a,b)
    
#While
s =1

while s <=10:
    print(s)
    s+=1
    
#if
test = 10
if test <5:
    print('Es menor a 5')
elif test <9:
    print('es menor a 9')
else:
    print('es mayor a 9')
    
#for + if

for i in rango:
    if i<=4:
        print('primer grupo', i)
    elif i < 6:
        print('otra cosa', i*2)
    else:
        print('final ', i**2)
        
list = [200,225,232,221,243,256,255]
dias =['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
b=-1
for i in list:
    a = list[b+1]    
    if a < i:
        print(i,dias[b+1])


#Funciones
argument_1 = 1
argument_2 = 5
def my_func(argument_1,argumento_2):
    resultado_1= argument_1*2
    resultado_2= argument_2/2
    resultado_final= resultado_1 - resultado_2
    return resultado_final

my_func(argumento_1=10,argumento_2=4)

def func_class(x): 
    if x<=4:
        resultado = 'Primer grupo ' + str(x)
    elif x <= 6:
        resultado = 'Otra cosa ' + str(x*2)
    else:
        resultado = 'final es ' + str(x**2)
    return my_func

for i in rango:
    print (func_class(i))
