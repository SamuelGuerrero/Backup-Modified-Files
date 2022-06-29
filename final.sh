#!/bin/bash
FECHA_HORA=`date "+%d-%m-%y_%H-%M-%S"`
ARCHIVO="respaldo_$FECHA_HORA.tgz"
DESTINO="./respaldos"
RESPALDAR="programa.py"
mkdir -p "$DESTINO"
tar cfvz "$DESTINO/$ARCHIVO" "$RESPALDAR" 