#Paredes Mendoza Gabriel Orlando
print ("PROGRAMA PARA HALLAR EL PROMEDIO DE LAS TRES MEJORES NOTAS")

def prom(a,b,c,d):
    if ((a>d)and(b>d)and(c>d)):
        r=(a+b+c)/3
        if r>=11:
            y="El alumno esta aprobado"
        if r<11:
            y="El alumno esta desaprobado"
    if ((a>c)and(b>c)and(d>c)):
        r=(a+b+d)/3
        if r>=11:
            y="El alumno esta aprobado"
        if r<11:
            y="El alumno esta desaprobado"
    if ((a>b)and(c>b)and(d>b)):
        r=(a+d+c)/3
        if r>=11:
            y="El alumno esta aprobado"
        if r<11:
            y="El alumno esta desaprobado"
    if ((b>a)and(c>a)and(d>a)):
        r=(d+b+c)/3
        if r>=11:
            y="El alumno esta aprobado"
        if r<11:
            y="El alumno esta desaprobado"
    return (round(r,1),y)

w=int(input("Ingrese la primera nota :"))
x=int(input("Ingrese la segunda nota :"))
y=int(input("Ingrese la tercera nota :"))
z=int(input("Ingrese la cuarta nota :"))

print ("El resultado de promediar las tres mejores notas nos da :{}".format(prom(w,x,y,z)))

    
    
