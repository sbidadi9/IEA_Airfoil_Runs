#!/bin/bash

grids=../$1/static/
list_of_cases=($(ls ${grids}))

# **** Modify the following variables ****
iterations=100
N_aoas=58
# ****************************************

for idx in `seq 0 $N_aoas`

   do

      echo " "
      echo "Job: "$idx &
      echo "Case: "${list_of_cases[$idx]} &

      out_file=($(find $grids${list_of_cases[$idx]} -type f -name "log*.out"))

      time=($(grep "WallClockTime" $out_file | tail -$iterations | awk -v div="$iterations.0" '{s+=$10} END {printf "%.4f \n", s/div}'))

      wct_min="0.1"
      wct_max="3.0"

      if (( $(echo "$time < $wct_min" |bc -l) )); then
	 echo "Fails to run."
         echo "${list_of_cases[$idx]} $time"
      elif (( $(echo "$time > $wct_max" |bc -l)  )); then
	 echo "Exceeds 3 seconds per time step."
         echo "${list_of_cases[$idx]} $time"
      fi

   done

wait
