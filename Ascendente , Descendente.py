#Paredes Mendoza Gabriel Orlando
print ("PROGRAMA PARA ORDENAR EN FORMA ASCENDENTE Y DESCENDENTE")

x=int(input("Ingrese el primer numero :"))
y=int(input("Ingrese el sugundo numero :"))
z=int(input("Ingrese el tercer numero :"))

if ((x>y)and(y>z)):
    print ("La forma ascendente es:")
    print (z,y,x)
    print ("La forma descendente  es:")
    print (x,y,z)
if ((x>z)and(y<z)):
    print ("La forma ascendente es:")
    print (y,z,x)
    print ("La forma descendente  es:")
    print (x,z,y)
if ((x<y)and(x>z)):
    print ("La forma ascendente es:")
    print (z,x,y)
    print ("La forma descendente  es:")
    print (y,x,z)
if ((z<y)and(x<z)):
    print ("La forma ascendente es:")
    print (x,z,y)
    print ("La forma descendente  es:")
    print (y,z,x)
if ((x<z)and(x>y)):
    print ("La forma ascendente es:")
    print (y,x,z)
    print ("La forma descendente  es:")
    print (z,x,y)
if ((z>y)and(x<y)):
    print ("La forma ascendente es:")
    print (x,y,z)
    print ("La forma descendente  es:")
    print (z,y,x)
