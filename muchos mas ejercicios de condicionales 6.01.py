A=int(input("escribe año:"))

if A%4 ==0 and A%100 !=0:
	print("es una año bisiesto")

elif A%400 ==0:
	print("también es bisiesto")

else:
	print("no es un año bisiesto")

