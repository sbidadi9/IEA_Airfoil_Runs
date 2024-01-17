#!/bin/bash

grids=../$1/static/
case=$1
list_of_cases=($(ls ${grids}))

# **** Modify the following variables ****
# Number of AOA simulations:
N_aoas=58
# ****************************************

for idx in `seq 0 $N_aoas`

   do

      echo " "
      echo "Job: "$idx &
      echo "Case: "${list_of_cases[$idx]} &

      awk 'NF{c=FNR}END{print c}' $grids${list_of_cases[$idx]}/"${case}_${list_of_cases[$idx]##*_}.dat"

   done

wait
