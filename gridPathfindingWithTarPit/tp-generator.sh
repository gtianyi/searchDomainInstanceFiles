#!/bin/bash

mkdir -p only_corridor_big_checkerboard
for (( i=1; i <= 200; i++ )); do
    python make-tp-checkerBoard-and-obs.py -r 50 -c 200 -s $i -pc 1000 > ./only_corridor_big_checkerboard/"$i.tp"; 
done

#mkdir -p startObstacle_big_checkerboard
#for (( i=1; i <= 100; i++ )); do
    #python make-tp-checkerBoard.py -r 50 -c 200 -t startObstacle -s $i -pc 1000 > ./startObstacle_big_checkerboard/"$i.tp"; 
#done

#mkdir -p goalObstacle_big_checkerboard
#for (( i=1; i <= 100; i++ )); do
    #python make-tp-checkerBoard.py -r 50 -c 200 -t goalObstacle -s $i -pc 1000 > ./goalObstacle_big_checkerboard/"$i.tp"; 
#done

#mkdir -p uniformObstacle_big_checkerboard
#for (( i=1; i <= 100; i++ )); do
    #python make-tp-checkerBoard.py -r 50 -c 200 -t uniformObstacle -s $i -pc 1000 > ./uniformObstacle_big_checkerboard/"$i.tp"; 
#done

#mkdir -p startObstacle
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -t startObstacle -s $i > ./startObstacle/"$i.tp"; 
#done

#mkdir -p goalObstacle
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -t goalObstacle -s $i > ./goalObstacle/"$i.tp"; 
#done

#mkdir -p uniformObstacle
#for (( i=1; i <= 100; i++ )); do
    #python make-tp.py -t uniformObstacle -s $i > ./uniformObstacle/"$i.tp"; 
#done


