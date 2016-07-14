#Paredes Mendoza Gabriel Orlando
print ("PROGAMA PARA VER SI UN TRIANGULO ES TRIANGULO")

def triangulo(a,b,c):
    if ((((a+b)>c)and(abs(a-b)<c))and(((a+c)>b)and(abs(a-c)<b))and(((c+b)>a)and(abs(c-b)<a))):
        t="Si es un triangulo"
    if ((((a+b)<c)or(abs(a-b)>c))or(((a+c)<b)or(abs(a-c)>b))or(((c+b)<a)or(abs(c-b)>a))):
        t="No es un triangulo"
    return t

x=float(input("Ingrese un lado del triangulo :"))
y=float(input("Ingrese un lado del triangulo :"))
z=float(input("Ingrese un lado del triangulo :"))

print ("El resultado es :{}".format(triangulo(x,y,z)))
