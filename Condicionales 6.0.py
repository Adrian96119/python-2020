Nombre1=input("Ingresa nombre:")
Nombre2=input("Ingresa npmbre:")

if(Nombre1[0]==Nombre2[0]):
	print("COINCIDENCIA")
elif Nombre1[-1]==Nombre2[-1]:
	print("COINCIDENCIA")

#OTRA OPCIÓN A ELIF:

#indice_final_Nombre1=len(nombre1)-1
#indice_final_Nombre2=len(npmbre2)-2
#if(Nombre1[indice_final_Nombre1]==Nombre2[indice_final_Nombre2]:

else:
	print("NO COINCIDENCIA")

