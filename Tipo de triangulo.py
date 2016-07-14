#Paredes Mendoza Gabriel Orlando
print ("PROGAMA PARA VER EL TIPO DE TRIANGULO")

def triangulo(a,b,c):
    if ((((a+b)>c)and(abs(a-b)<c))and(((a+c)>b)and(abs(a-c)<b))and(((c+b)>a)and(abs(c-b)<a))):
        t="Si es un triangulo"
    if ((((a+b)<c)or(abs(a-b)>c))or(((a+c)<b)or(abs(a-c)>b))or(((c+b)<a)or(abs(c-b)>a))):
        t="No es un triangulo"
    return t
def tipo(r,s,t):
    if ((r==s)or(s==t)or(t==r)):
        h="Isoceles"
    if ((r==s)and(s==t)):
        h="Equilatero"
    if(((r>s)and(s>t))or((r>t)and(t>s))or((s>r)and(r>t))or((s>t)and(t>r))or((t>r)and(r>s))or((t>s)and(s>r))):
        h="Escaleno"
        
    return h

x=float(input("Ingrese un lado del triangulo :"))
y=float(input("Ingrese un lado del triangulo :"))
z=float(input("Ingrese un lado del triangulo :"))

print ("El resultado es :{}".format(triangulo(x,y,z)))
print ("Es de tipo :{}".format(tipo(x,y,z)))
