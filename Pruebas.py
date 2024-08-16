list = [200,225,232,221,243,256,255]
dias =['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
b=0
j =0
for i in list:
    a = i  
    if a < b:
        print("El día ",dias[j], " el precio bajó desde a ", b, "hasta ", a)
    b = a
    j += 1
