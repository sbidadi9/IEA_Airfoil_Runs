import yaml, json, glob, sys
from pathlib import Path
import numpy as np
import pandas as pd

# Specify the location of the directory where the grids reside:
grids_dir = "/lustre/orion/cfd116/scratch/sbidadi/ffa_w3/grids/"

# Specify the run_folder:
runf = "/lustre/orion/cfd162/scratch/sbidadi/ffa_w3_162/flat_plate_runs/nalu_runs"

run_type = "static"

def gen_static_case(af_name, mesh_file, aoa, run_folder='nalu_runs', template="ffa_w3_template.yaml"):

    if ( not Path(template).exists() ):
        print("Template file ", template, " doesn't exist. Please check your inputs")
        sys.exit()

    tfile = yaml.load(open(template),Loader=yaml.UnsafeLoader)

    if ( not Path(mesh_file).exists() ):
        print("Mesh file ", mesh_file, " doesn't exist. Please check your inputs")
        sys.exit()

    Path(run_folder+'/{}/static/aoa_{}'.format(af_name,aoa)).mkdir(parents=True, exist_ok=True)

    tfile['linear_solvers'][0]['hypre_cfg_file'] = run_folder + '/job_list/hypre_file.yaml'
    tfile['linear_solvers'][1]['hypre_cfg_file'] = run_folder + '/job_list/hypre_file.yaml'
    tfile['linear_solvers'][2]['hypre_cfg_file'] = run_folder + '/job_list/hypre_file.yaml' 

    tfile['realms'][0]['mesh'] = str(Path(mesh_file).absolute())

    tfile['Time_Integrators'][0]['StandardTimeIntegrator']['termination_step_count'] = 16001
    tfile['Time_Integrators'][0]['StandardTimeIntegrator']['time_step'] = 0.00013335

    tfile['realms'][0]['output']['output_data_base_name'] = run_folder + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/results/{}_{}.e'.format(af_name, aoa)
    tfile['realms'][0]['output']['output_frequency'] = 1000
    tfile['realms'][0]['post_processing'][0]['output_file_name'] = run_folder + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/pp_'+af_name+'_'+str(aoa)+'.dat'
    tfile['realms'][0]['post_processing'][1]['output_file_name'] = run_folder + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/' + af_name+'_'+str(aoa)+'.dat'
    tfile['realms'][0]['restart']['restart_data_base_name'] = run_folder + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/restart/{}_{}.e'.format(af_name, aoa)
    tfile['realms'][0]['restart']['restart_frequency'] = 1000
    tfile['realms'][0]['solution_options']['turbulence_model'] = 'sst_iddes'

    yaml.dump(tfile, open(run_folder+'/{}/static/aoa_{}/{}_static_aoa_{}.yaml'.format(af_name, aoa, af_name, aoa),'w'), default_flow_style=False)



def gen_ffa_w3_static_cases(af_name, aoa_range = [32, 50], run_folder='nalu_runs', template="ffa_w3_template.yaml"):
 
    for aoa in aoa_range:
        gen_static_case(af_name, grids_dir+af_name+'/'+af_name+'_'+str(aoa)+'.exo', aoa, run_folder, template)



if __name__=="__main__":

    aoa_array = [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30, -33,
              -40, -50, -60, -70, -80, -90,
              -100, -110, -120,
              -128, -136, -144, -152, -160,
              -165, -170, -175, -180,
              0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
              40, 50, 60, 70, 80, 90,
              100, 110, 120,
              128, 136, 144, 152, 160,
              165, 170, 175, 180]

    mesh_files = ["ffa_w3_211", "ffa_w3_241", "ffa_w3_270", "ffa_w3_301", "ffa_w3_330", "ffa_w3_360", "ffa_w3_500"]

    for mfile in mesh_files:
        gen_ffa_w3_static_cases(mfile, aoa_range=aoa_array, run_folder=runf)
