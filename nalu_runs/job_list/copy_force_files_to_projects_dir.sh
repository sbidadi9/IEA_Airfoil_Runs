#!/bin/bash

grids=../$1/static/
case=$1
list_of_cases=($(ls ${grids}))

# **** Modify the following variables ****
# Number of AOA simulations:
N_aoas=58

# Location to copy the files:
proj_dir=/ccs/proj/cfd116/sbidadi/ecp_project/plots/
# ****************************************

for idx in `seq 0 $N_aoas`

   do

      echo " "
      echo "Job: "$idx &
      echo "Case: "${list_of_cases[$idx]} &
      dir_to_copy=$proj_dir$case/data_files
      echo $dir_to_copy
      cp $grids${list_of_cases[$idx]}/"${case}_${list_of_cases[$idx]##*_}.dat" $dir_to_copy

   done

wait
