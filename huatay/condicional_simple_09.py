import os
# CALCULO DE LA DENSIDAD DE UN OBJETO
MASA,VOLUMEN=0.0,0.0

# ASIGNACION DE VALORES
MASA=float(os.sys.argv[1])
VOLUMEN=int(os.sys.argv[2])/1000
# el volumen lo dividimos entre mil ya que esta expresado en mililitros

# CALCULO
densidad=MASA/VOLUMEN

# CONDICIONAL SIMPLE:
if VOLUMEN==0:
    print("VALOR INGRESADO DEL VOLUMEN INCORRECTO")
# MOSTRAR VALORES
print("La masa del objeto es: "+str(MASA))
print("El volumen del objeto es: "+str(VOLUMEN))
print("LA densidad del objeto es: "+str(densidad))


