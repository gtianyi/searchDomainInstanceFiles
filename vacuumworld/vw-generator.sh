#!/bin/bash

for (( i=1; i <= 200; i++ )); do
    ./make-vw 200 200 0.35 6 -seed $i > "$i.vw"; 
done
