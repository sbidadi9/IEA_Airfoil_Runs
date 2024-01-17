# Collection of utilities to generate nalu-wind input files for airfoil
# simulations

import yaml, json, glob, sys
from pathlib import Path
import numpy as np
import pandas as pd

nalu_runs = "/lustre/orion/cfd116/scratch/sbidadi/ffa_w3/nalu_runs"
run_type = "static"

def gen_static_case(af_name, mesh_file, aoa, rey, run_folder='nalu_runs', template="/lustre/orion/cfd116/scratch/sbidadi/ffa_w3/static/ffa_w3_500/ffa_w3_301.yaml"):
    """Generate a nalu input file for simulation of flow past an airfoil
    using k-w-SST turbulence model

    Args:
        af_name (string):
        mesh_file (string):
        aoa (double): Angle of attack in degrees
        rey (double): Reynolds number
        template (string): Path to template nalu input file in yaml format

    Returns:
        None

    """

    if ( not Path(template).exists() ):
        print("Template file ", template, " doesn't exist. Please check your inputs")
        sys.exit()

    tfile = yaml.load(open(template),Loader=yaml.UnsafeLoader)

    if ( not Path(mesh_file).exists() ):
        print("Mesh file ", mesh_file, " doesn't exist. Please check your inputs")
        sys.exit()

    Path(run_folder+'/{}/static/aoa_{}'.format(af_name,aoa)).mkdir(parents=True, exist_ok=True)

    tfile['linear_solvers'][0]['hypre_cfg_file'] = nalu_runs + '/job_list/hypre_file.yaml'
    tfile['linear_solvers'][1]['hypre_cfg_file'] = nalu_runs + '/job_list/hypre_file.yaml'
    tfile['linear_solvers'][2]['hypre_cfg_file'] = nalu_runs + '/job_list/hypre_file.yaml' 

    tfile['realms'][0]['mesh'] = str(Path(mesh_file).absolute())

    tfile['Time_Integrators'][0]['StandardTimeIntegrator']['termination_step_count'] = 9000
    tfile['Time_Integrators'][0]['StandardTimeIntegrator']['time_step'] = 0.00013335

    tfile['realms'][0]['output']['output_data_base_name'] = nalu_runs + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/results/{}_{}.e'.format(af_name, aoa)
    tfile['realms'][0]['post_processing'][0]['output_file_name'] = nalu_runs + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/pp_'+af_name+'_'+str(aoa)+'.dat'
    tfile['realms'][0]['post_processing'][1]['output_file_name'] = nalu_runs + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/' + af_name+'_'+str(aoa)+'.dat'
    tfile['realms'][0]['restart']['restart_data_base_name'] = nalu_runs + '/' + af_name + '/' + run_type + '/aoa_' + str(aoa) + '/restart/{}_{}.e'.format(af_name, aoa)
    tfile['realms'][0]['solution_options']['turbulence_model'] = 'sst_iddes'

    yaml.dump(tfile, open(run_folder+'/{}/static/aoa_{}/{}_static_aoa_{}.yaml'.format(af_name, aoa, af_name, aoa),'w'), default_flow_style=False)

def gen_ffa_w3_static_cases(af_name, rey=10.0e6, aoa_range = [32, 50], run_folder='nalu_runs', template="/lustre/orion/cfd116/scratch/sbidadi/ffa_w3/static/ffa_w3_500/ffa_w3_301.yaml"):
 
    """Generate static cases for the FFA-W3-500 airfoil
    Args:
        aoa_range (np.array): Angle of attack range

    Return:
       None

    """

    print(aoa_range)
    for aoa in aoa_range:
        print(aoa)
        gen_static_case(af_name, '/lustre/orion/cfd116/scratch/sbidadi/ffa_w3/grids/'+af_name+'/'+af_name+'_'+str(aoa)+'.exo', aoa, rey, run_folder, template)


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


#    mesh_files = ["ffa_w3_211", "ffa_w3_241", "ffa_w3_270", "ffa_w3_301", "ffa_w3_330", "ffa_w3_360", "ffa_w3_500"]
    mesh_files = ["ffa_w3_211"]

    print(aoa_array)

    for mfile in mesh_files:
        print(mfile)
        gen_ffa_w3_static_cases(mfile, rey=10.0e6, aoa_range=aoa_array)
