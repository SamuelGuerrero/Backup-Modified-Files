def modificarScript(mensaje):

    nuevoMensaje = '#!/bin/bash\nFECHA_HORA=`date "+%d-%m-%y_%H-%M-%S"`\nARCHIVO="respaldo_$FECHA_HORA.tgz"\nDESTINO="./respaldos"\nRESPALDAR="'+mensaje+'"\nmkdir -p "$DESTINO"\ntar cfvz "$DESTINO/$ARCHIVO" "$RESPALDAR" '
    return nuevoMensaje

def limpiarRegistro(entrada):
    salida = ''
    if(len(entrada) < 7 ):
        return None
    elif(ord(entrada[6]) == 47):
        
        if("swp" in entrada):
            return None

        i = 7
        while(ord(entrada[i]) != 92 ):
            print(entrada[i])
            salida = salida + entrada[i]
            i = i+1        
    else:
        i = 4
        while(ord(entrada[i]) != 92 ):
            print(entrada[i])
            salida = salida + entrada[i]
            i = i+1
    return salida
    
#!/usr/bin/env python3

import subprocess
import time
from os import system


while(1):
    proc = subprocess.Popen(["find -mmin -0.01"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    if(limpiarRegistro(str(out)) != None):
        msg = modificarScript(limpiarRegistro(str(out)))
        f = open('final.sh','w')
        try:
            f.write(msg)
        finally:
            f.close()        
        #
        try: 
            system("chmod +x final.sh")
            system("./final.sh")
        except:
            print("B")

    time.sleep(0.6)

