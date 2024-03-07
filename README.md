Repository for generating meshes, input files, running cases and post-processing results for IEA 15MW airfoils.

1. Generate input files for the specified angles of attack (AOAs)
between -180 to +180 degrees and the seven IEA 15MW airfoils 
using gen_naluwind_inp_files_ffa_w3_airfoils.py script.

2. Exodus files for each AOA and airfoil is generated using mesh generation scripts.

3. Directory nalu_runs/job_list subdirectory contains slurm scripts for running the static airfoil cases.

4. Directory post_proc_scripts contains scripts for generating polars and for performing frequency analysis.
