#el mayor de tres numeros
print("Prog. busca el mayor de tres numeros")
x1=int(input("ingrese el 1° valor:"))
x2=int(input("ingrese el 2° valor:"))
x3=int(input("ingrese el 3° valor:"))

#comparar "si" --> if - elif - else
#elif --> sino si(condicion) --> else if
#solo IF y ELIF llevan condicion, el ELSE jamas lleva cond.
# y = and, o = or
# el signo = asignacion
#el signo == comparacion

if(x1>x2) and (x1>x3):
    print("el mayor es:",x1)
elif(x2>x1) and (x2>x3):
    print("el mayor es:",x2)
else:
    print("el mayor es",x3)
