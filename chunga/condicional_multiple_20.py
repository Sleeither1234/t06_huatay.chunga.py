# DISCO DE UN CANTANTE
import os
nombre_cantante = (os.sys.argv[1])
nombre_de_cancion = (os.sys.argv[2])
precio =  float(os.sys.argv[3])
unidades =  int(os.sys.argv[4])
total = precio * unidades

print ( " ############################################### ##### " )
print ( " # DISCO ELECTRO # " )
print ( " # " )
print ( " # NOM.CANTANTE: "  + nombre_cantante)
print ( " # NOM.CANCION: "  + nombre_de_cancion)
print ( " # PU: "  +  str (precio))
print ( " # UNIDADES: "  +  str (unidades))
print ( " # TOTAL: "  +  str (total))
print ( " # " )
if total>=1000:
    print("compra alta")
elif total>=800:
    print("Compra media")
elif total>=100:
    print("¿Por que no compra mas?")
else:
    print("Gran musica, compre")
print ( " ############################################### ####### " )
