# coding: utf-8
import numpy as np
from scipy.fftpack import fft, fftfreq
import scipy.signal
from scipy.signal import argrelextrema
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
       -15, -12, -3, 0, 12, 15, 18, 21, 24, 27, 30, 33, 40, 50, 60, 70, 80, 90, 100, 110, 120,
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
chord_length = 1.0
chord_lengthn_airfoils = [np.sin(aoa_rad_airfoils[0]), np.sin(aoa_rad_airfoils[1]), np.sin(aoa_rad_airfoils[2]),
                          np.sin(aoa_rad_airfoils[3]), np.sin(aoa_rad_airfoils[4]), np.sin(aoa_rad_airfoils[5]),
                          np.sin(aoa_rad_airfoils[6])]

af_type = ['ffa_w3_211', 'ffa_w3_241', 'ffa_w3_270', 'ffa_w3_301', 'ffa_w3_330', 'ffa_w3_360', 'ffa_w3_500']
af_thick = ['211', '241', '270', '301', '330', '360', '500']

N = 8000
T = 0.00013335 # sample spacing
fs = 1/T
sf = 15

def get_avg_data(af_name, aoa):
    """Get average lift and drag data for a given grid"""
    case_data = [pd.read_csv(af_name+'/'+'data_files/'+af_name+'_'+str(aoa[i])+'.dat', sep="\s+", skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float).iloc[-N:] for i, c in enumerate(aoa)]
    case_cl = [ np.average((c["Fpy"] + c["Fvy"])/dyn_pres/4.0) for c in case_data]
    case_cd = [ np.average((c["Fpx"] + c["Fvx"])/dyn_pres/4.0) for c in case_data]
    return case_cl, case_cd

def get_case_data(af_name, aoa_one_airfoil):
    print(af_name+'/'+'data_files/'+af_name+'_'+str(aoa_one_airfoil)+'.dat')
    return pd.read_csv(af_name+'/'+'data_files/'+af_name+'_'+str(aoa_one_airfoil)+'.dat', sep="\s+", skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float)


with PdfPages('cl_all_airfoils_st.pdf') as pfpgs:
     fig = plt.figure()

     for j, af_name in enumerate(af_type):
         cl_max_freq_list = []
         st_list = []
         case_cl, case_cd = get_avg_data(af_name, aoa_airfoils[j])
         chord_lengthn = chord_lengthn_airfoils[j]
         aoas = aoa_airfoils[j]
         for i, aoa_one_airfoil in enumerate(aoas):
             cdata = get_case_data(af_name, aoa_one_airfoil)
             cl = (cdata.iloc[-N:]["Fpy"] + cdata.iloc[-N:]["Fvy"])/dyn_pres/4.0
             time = (cdata.iloc[-N:]["Time"])
             sampling_freq = fftfreq(N, T)[sf:N//2]
             cl_fft = fft(np.array(cl) - np.average(cl))
             energy = 2.0/N * np.abs(cl_fft[sf:N//2])
             max_value = np.max(energy)
             max_freq = sampling_freq[energy.argmax()]
             cl_max_freq_list.append(max_freq)

             st = np.abs(max_freq*chord_lengthn[i]/u_infty)
             st_list.append(st)
             print(j, aoa_one_airfoil, max_freq, st)
         plt.plot(aoas, st_list, marker = 'o', color=colors[j], label=af_thick[j])
         plt.hlines(0.2, -182.0, 182.0, linestyles='dashed', color='black')
#         plt.hlines(-0.2, -182.0, 182.0, linestyles='dashed', color='black')
     plt.xlabel(r'$\alpha$')
     plt.xlim([-182.0,182.0])
#     plt.ylim([-0.05,])
     plt.ylabel('St')
     plt.legend(loc='best', ncol=8)
     plt.tight_layout()
     pfpgs.savefig()
