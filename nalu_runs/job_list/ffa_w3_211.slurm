#!/bin/bash

#SBATCH -A CFD162
#SBATCH -J ffa_w3_211
#SBATCH -t 12:00:00
#SBATCH -p batch
#SBATCH -N 1888
#SBATCH --mail-type=ALL
#SBATCH --mail-user=shreyas.bidadi@nrel.gov

#####
# N = number of nodes
# --ntasks-per-node = gpu_ranks_per_node
#####

##################
nodes_requested=$SLURM_JOB_NUM_NODES
ranks_requested=$SLURM_NTASKS
##################

export rocm_version=5.4.3

#module purge
module load PrgEnv-amd
module load amd/${rocm_version}
module load craype-accel-amd-gfx90a
module load cray-mpich

export FI_MR_CACHE_MONITOR=memhooks
export FI_CXI_RX_MATCH_MODE=software
#export HIP_LAUNCH_BLOCKING=1

export SPACK_MANAGER=/ccs/home/sbidadi/exawind/spack-manager
source ${SPACK_MANAGER}/start.sh
spack-start
spack env activate -d ${SPACK_MANAGER}/environments/uaero
spack load nalu-wind

grids=../ffa_w3_211/static/
echo ${grids}
list_of_cases=($(ls ${grids}))

for idx in {0..58};

   do

      echo " "
      echo "Job: "$idx &
      echo "Case: "${list_of_cases[$idx]} &
      echo "Directory contents of " ${list_of_cases[$idx]} &
      ls -alh ${grids}/${list_of_cases[$idx]} &

      date &
      
      echo "Yaml file: " $grids${list_of_cases[$idx]}/*.yaml
      srun -u -N32 -n256 --ntasks-per-gpu=1 --gpu-bind=closest naluX -i $grids${list_of_cases[$idx]}/*.yaml -o $grids${list_of_cases[$idx]}/log$idx.out &

      sleep 1

   done

wait
