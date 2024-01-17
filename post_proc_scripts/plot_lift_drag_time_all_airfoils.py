# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator
import matplotlib as mpl 
from cycler import cycler

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
print(colors)


mpl.rcParams['lines.linewidth'] = 2 
mpl.rcParams['axes.titlesize'] = 30
mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['legend.fontsize'] = 8
#mpl.rcParams['figure.figsize'] = (6.328, 5.328)
mpl.rcParams['figure.figsize'] = (7.328, 5.328)
mpl.rcParams["figure.autolayout"] = True

rho = 1.2
u_infty = 75.0
dyn_pres = 0.5 * rho * (u_infty ** 2)
N = 8000


#aoa_array = [-180, -175, -170, -165,
#                -160, -152, -144, -136, -128,
#                -120, -110, -100, 
#                -90, -80, -70, -60, -50, -40
#                -33, -30, -27, -24, -21, -18,
#                -15, -12, -9, -6, -3,
#                0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
#                40, 50, 60, 70, 80, 90,
#                100, 110, 120,
#                128, 136, 144, 152, 160,
#                165, 170, 175, 180]

# FFA_W3_211:
#af_name='ffa_w3_211'
aoa_211 = [-180, -175, -170, -165,
           -160, -152, -144, -136, -128,
           -120, -110, -100,
           -90, -80, -70, -60, -50, -40,
           -33, -30, -27, -24, -21, -18,
           -15, -12, -9, -6, -3,
           0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
           40, 50, 60, 70, 80, 90, 100, 110, 120,
           128, 136, 144, 152, 160,
           165, 170, 175, 180]

#af_name='ffa_w3_241'
aoa_241 = [-180, -175, -170, -165, -160, -152, -144, -136, -128,
       -120, -110, -100, -90, -80, -70, -60, -50, -40, 
       -33, -30, -27, -24, -21, -18,
       -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
       40, 50, 60, 70, 80, 90, 100, 110, 120,
       128, 136, 144, 152, 160, 165, 170, 175, 180]

#af_name='ffa_w3_270'
aoa_270 = [-180, -175, -170, -165,
                -160, -152, -144, -136, -128,
                -120, -110, -100, 
                -90, -80, -70, -60, -50, -40, -33,
                -30, -27, -24, -21, -18,
                -15, -12, -9, -6, -3,
                0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
                40, 50, 60, 70, 80, 90,
                100, 110, 120,
                128, 136, 144, 152, 160,
                165, 170, 175, 180]

#af_name='ffa_w3_301'
aoa_301 = [-180, -175, -170, -165, -160, -152, -144, -136, -128, 
-120, -110, -100, -90, -80, -70, -60, -50, -40, -33, -30, -27, -24, -21, -18,
-15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
40, 50, 60, 70, 80, 90, 100, 110, 120,
128, 136, 144, 152, 160, 165, 170, 175, 180]

#af_name='ffa_w3_330'
aoa_330 = [-180, -175, -170, -165, -160, -152, -144, -136, -128, -120, -110, -100, 
       -90, -80, -70, -60, -50, -40, 
       -33, -30, -27, -21, -18,
       -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 40, 50, 60, 70, 80, 90, 100, 110, 120, 
       128, 136, 144, 152, 160, 
       165, 170, 175, 180]

# FFA_W3_360:
#af_name='ffa_w3_360'
aoa_360 = [-180, -175, -170, -165,
           -160, -152, -144, -136, -128,
           -120, -110, -100,
           -90, -80, -70, -60, -50, -40,
           -33, -30, -27, -24, -21, -18,
           -15, -12, -9, -6, -3,
           0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
           40, 50, 60, 70, 80, 90,
           100, 110, 120,
           128, 136, 144, 152, 160,
           165, 170, 175, 180]

# FFA_W3_500:
#af_name='ffa_w3_500'
aoa_500 = [-180, -175, -170, -165, -160,
-152, -144, -136, -128, -120, -110,
-100, -90, -80, -70, -60, -50, -40, -33, -30,
-27, -24, -21, -18, -15, -12, 
-9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 40, 50, 60, 70, 80, 90,
100, 110, 120, 128,
136, 144, 152, 160,
165, 170, 175, 180]


aoa_airfoils = [aoa_211, aoa_241, aoa_270, aoa_301, aoa_330, aoa_360, aoa_500]
aoa_rad_airfoils = [np.multiply(aoa_211, np.pi/180.0), np.multiply(aoa_241, np.pi/180.0), 
                    np.multiply(aoa_270, np.pi/180.0), np.multiply(aoa_301, np.pi/180.0),
                    np.multiply(aoa_330, np.pi/180.0), np.multiply(aoa_360, np.pi/180.0),
                    np.multiply(aoa_500, np.pi/180.0)]

af_type = ['ffa_w3_211', 'ffa_w3_241', 'ffa_w3_270', 'ffa_w3_301', 'ffa_w3_330', 'ffa_w3_360', 'ffa_w3_500']
af_thick = ['211', '241', '270', '301', '330', '360', '500']

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_211_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_211_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_241_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_241_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_270_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_270_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_301_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_301_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_330_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_330_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_360_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_360_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

#ref_data = {
#    'cl' : pd.read_csv('ref_data/cl_ffa_w3_500_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cl']),
#    'cd' : pd.read_csv('ref_data/cd_ffa_w3_500_ref_data.txt',header=None,sep='\t', lineterminator='\n',names=['aoa','cd']),
#}

def get_avg_data(af_name, aoa):
    """Get average lift and drag data for a given grid"""
    case_data = [pd.read_csv(af_name+'/'+'data_files/'+af_name+'_'+str(aoa[i])+'.dat', sep="\s+", skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float).iloc[-N:] for i, c in enumerate(aoa)]
    case_cl = [ np.average((c["Fpy"] + c["Fvy"])/dyn_pres/4.0) for c in case_data]
    case_cd = [ np.average((c["Fpx"] + c["Fvx"])/dyn_pres/4.0) for c in case_data]
    case_cm = [ np.average(c["Mtz"]/dyn_pres/4.0) for c in case_data]
    return case_cl, case_cd, case_cm

def get_case_data(af_name, aoa_one_airfoil):
    print(af_name+'/'+'data_files/'+af_name+'_'+str(aoa_one_airfoil)+'.dat')
    return pd.read_csv(af_name+'/'+'data_files/'+af_name+'_'+str(aoa_one_airfoil)+'.dat', sep="\s+", skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float)

def get_std_data():
    """Get average lift and drag data for a given turbulence model, upwinding and grid"""
    case_data = [pd.read_csv(c+'/'+'iddes_ffa_w3_211_'+str(aoa[i])+'.dat', sep="\s+", 
skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float).iloc[-N:] for i, c in enumerate(case_dirs)]
    case_cl_std = [ np.std((c["Fpy"] + c["Fvy"])/dyn_pres/4.0) for c in case_data]
    case_cd_std = [ np.std((c["Fpx"] + c["Fvx"])/dyn_pres/4.0) for c in case_data]
    return case_cl_std, case_cd_std

with PdfPages('cl_all_airfoils.pdf') as pfpgs:
     fig = plt.figure()

     for j, af_name in enumerate(af_type):
         print(af_name)
         case_cl, case_cd, case_cm = get_avg_data(af_name, aoa_airfoils[j])
         plt.plot(aoa_airfoils[j], case_cl, marker = 'o', color=colors[j], label=af_thick[j])

     plt.xlabel(r'$\alpha$')
     plt.ylabel('$C_l$')
     plt.xlim([-182.0,182.0])
     plt.ylim([-2.0,2.5]) 
     plt.legend(loc='best', ncol=8)
     plt.minorticks_on()
     plt.tight_layout()
     pfpgs.savefig()
     plt.close(fig)
     plt.show()

with PdfPages('cd_all_airfoils.pdf') as pfpgs:
     fig = plt.figure()

     for j, af_name in enumerate(af_type):
         case_cl, case_cd, case_cm = get_avg_data(af_name, aoa_airfoils[j])
         plt.plot(aoa_airfoils[j], case_cd, marker = 'o', color=colors[j], label=af_thick[j])

     plt.xlabel(r'$\alpha$')
     plt.ylabel('$C_d$')
     plt.xlim([-182.0,182.0])
     plt.ylim([-0.1,2.0]) 
     plt.legend(loc='best', ncol=8)
     plt.minorticks_on()
     plt.tight_layout()
     pfpgs.savefig()
     plt.close(fig)
     plt.show()

with PdfPages('cm_all_airfoils.pdf') as pfpgs:
     fig = plt.figure()

     for j, af_name in enumerate(af_type):
         case_cl, case_cd, case_cm = get_avg_data(af_name, aoa_airfoils[j])
         plt.plot(aoa_airfoils[j], case_cm, marker = 'o', color=colors[j], label=af_thick[j])

     plt.xlabel(r'$\alpha$')
     plt.ylabel('$C_m$')
     plt.xlim([-182.0,182.0])
#     plt.ylim([-0.1,2.0]) 
     plt.legend(loc='best', ncol=8)
     plt.minorticks_on()
     plt.tight_layout()
     pfpgs.savefig()
     plt.close(fig)
     plt.show()
