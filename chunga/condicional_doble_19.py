# TICKET DE CINE
import os
cliente =(os.sys.argv[1])
pelicula =(os.sys.argv[2])
precio =  float(os.sys.argv[3])
unidades =  int(os.sys.argv[4])
total = precio * unidades

print ( " ############################################### ########## " )
print ( " # CINEMARK # " )
print ( " # " )
print ( " # CLIENTE: "  + cliente)
print ( " # PELICULA: "  + pelicula)
print ( " # PU: "  +  str (precio))
print ( " # UNIDADES: "  +  str (unidades))
print ( " # TOTAL: "  +  str (total))
print ( " # " )
if total>=60:
    print("Disfruten en grupo")
else:
    print("Disfrute en pareja")
print ( " ############################################### ########## " )
