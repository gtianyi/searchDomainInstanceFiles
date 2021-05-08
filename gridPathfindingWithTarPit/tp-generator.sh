#!/bin/bash

#mkdir -p startObstacle_large
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -r 100 -c 1000 -pd 0.2 -t startObstacle -s $i > ./startObstacle_large/"$i.tp"; 
#done

#mkdir -p goalObstacle_large
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -r 100 -c 1000 -pd 0.2 -t goalObstacle -s $i > ./goalObstacle_large/"$i.tp"; 
#done

#mkdir -p uniformObstacle_large
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -r 100 -c 1000 -pd 0.2 -t uniform -s $i > ./uniformObstacle_large/"$i.tp"; 
#done

mkdir -p startObstacle
for (( i=1; i <= 100; i++ )); do
    python make-tp.py -t startObstacle -s $i > ./startObstacle/"$i.tp"; 
done

mkdir -p goalObstacle
for (( i=1; i <= 100; i++ )); do
    python make-tp.py -t goalObstacle -s $i > ./goalObstacle/"$i.tp"; 
done

mkdir -p uniformObstacle
for (( i=1; i <= 100; i++ )); do
    python make-tp.py -t uniform -s $i > ./uniformObstacle/"$i.tp"; 
done


