Each slurm script corresponds to an IEA 15MW airfoil. The scripts launch a collection of AOA jobs simultaneously.

Based on strong scaling studies, each AOA run utilizes 32 GPU nodes.

The directory also contains the following shell scripts:

1. copy_force_files_to_projects_dir.sh:
	- Copies all AOA data files for a given airfoil from the AOA directories to a directory under projects folder. 

2. line_number_check.sh:
	- Goes through data files in AOA directories and prints the number of time steps the cases ran for.
	- Purpose is to check if the number matches what is specified in the input file.
	  
3. success.sh:
	- Checks which of the airfoil cases ran with less than 3 seconds per time step. 

- Input to the scripts is the airfoil name (ex. ffa_w3_211).
