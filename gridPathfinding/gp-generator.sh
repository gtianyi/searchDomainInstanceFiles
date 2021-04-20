#!/bin/bash

for (( i=1; i <= 100; i++ )); do
    #python make-gp.py -s $i > "$i.gp"; 
    #python make-gp.py -t startObstacle -s $i > "$i.gp"; 
    python make-gp.py -t uniform -s $i > "$i.gp"; 
done
