import os
# CALCULO DE LA PRESION EJERCIDA DE UN OBJETO
FUERZA,AREA=0.0,0.0

# ASIGNACION DE VALORES
FUERZA=int(os.sys.argv[1])
AREA=int(os.sys.argv[2])

# CALCULO
presion=FUERZA/AREA

# CONDICIONAL MULTIPLE
if AREA==0:
    print("EL VALOR DEL AREA ES INCORRECTO")
elif presion>50:
    print("CUIDADO...,LA PRESION EJERCIDA PUEDE ROMPER EL OBJETO")
else:
    print("EL AREA TIENE UN VALOR CORRECTO")
# MOSTRAR VALORES
print("La fuerza ejercida por el objeto es: "+str(FUERZA))
print("El area ejercida por el objeto es: "+str(AREA))
print("La presion que se ejerce sobre el objeto es: "+str(presion))
