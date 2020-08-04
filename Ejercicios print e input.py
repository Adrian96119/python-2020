
A=int(input("ingrese dia de nacimiento:"))
B=int(input("ingrese mes de nacimiento:"))
C=int(input("ingrese año de nacimiento:"))

print (A,"/", B,"/", C)

fecha=int(input("Fecha de formato DDMMAAA: "))

B=(fecha%10000)
A=(fecha//1000000)
C=(fecha//10000)%100

print(A,"/",C,"/",B)


fecha=input("fecha de formato DDMMAAAA:")

A=fecha[:2]
B=fecha[2:4]
C=fecha[4:]

print(A,"/",B,"/",C)

kmsporlitros=float(input("kilometros por litro:"))
capacidad=float(input("capacidad:"))
kilometrostotales=float(input("recorrido:"))
Tanquestotales=kmsporlitros*capacidad
print("cuantos tanques necesita", kilometrostotales/Tanquestotales, "Tanques")

