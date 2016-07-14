#Paredes Mendoza Gabriel Orlando
print ("PROGRAMA PARA HALLAR QUE NUMERO ES MAYOR")

def numero(a,b):
    if (a>b):
        h="El numero a es mayor que b"
    if (a<b):
        h="El numero b es mayor que a"
    if (a==b):
        h="El numero a es igual que b"
    return h
x=float(input("Ingrese el valor de a :"))
y=float(input("Ingrese el valor de b :"))

print ("El resultado es :{}".format(numero(x,y)))

    
    
