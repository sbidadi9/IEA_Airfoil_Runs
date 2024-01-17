# coding: utf-8
import numpy as np
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

#aoa = [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30, -33,
#       -40, -50, -60, -70, -80, -90,
#       -100, -110, -120,
#       -128, -136, -144, -152, -160,
#       -165, -170, -175, -180,
#       0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
#       40, 50, 60, 70, 80, 90,
#       100, 110, 120,
#       128, 136, 144, 152, 160,
#       165, 170, 175, 180]


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
aoa_rad_airfoils = [np.multiply(aoa_211, np.pi/180.0), np.multiply(aoa_360, np.pi/180.0), np.multiply(aoa_500, np.pi/180.0)]

af_type = ['ffa_w3_211', 'ffa_w3_241', 'ffa_w3_270', 'ffa_w3_301', 'ffa_w3_330', 'ffa_w3_360', 'ffa_w3_500']
af_thick = ['211', '241', '270', '301', '330', '360', '500']
N = 4000


def get_case_data(af_name, aoa_one_airfoil):
    return pd.read_csv(af_name+'/'+'data_files/'+af_name+'_'+str(aoa_one_airfoil)+'.dat', sep="\s+", skiprows=1,header=None, names=[ "Time","Fpx","Fpy","Fpz","Fvx","Fvy","Fvz","Mtx","Mty","Mtz","Y+min","Y+max"],dtype=float)


with PdfPages('cl_ffa_w3_amplitude.pdf') as pfpgs:
     fig = plt.figure()

     for j, af_name in enumerate(af_type):
         cl_ampl_list = []
         aoas = aoa_airfoils[j]

         for i, aoa_one_airfoil in enumerate(aoas):

              cdata = get_case_data(af_name, aoa_one_airfoil)
              cl = (cdata.iloc[-N:]["Fpy"] + cdata.iloc[-N:]["Fvy"])/dyn_pres/4.0
              cl_arr = np.array(cl)
              cl_arr_max_amp = cl_arr[argrelextrema(cl_arr, np.greater)[0]]
              cl_arr_min_amp = cl_arr[argrelextrema(cl_arr, np.less)[0]]

              if cl_arr_max_amp.size:
                 max_avg_amp = np.average(cl_arr_max_amp)
              else:
                 max_avg_amp = 0.0 

              if cl_arr_min_amp.size:
                 min_avg_amp = avg = np.average(cl_arr_min_amp)
              else:
                 min_avg_amp = 0.0;

              cl_amplitude = abs(max_avg_amp - min_avg_amp)
              cl_ampl_list.append(cl_amplitude)

         plt.plot(aoas, cl_ampl_list, marker = 'o', color=colors[j], label=af_thick[j])
     plt.xlabel(r'$\alpha$')
     plt.ylabel('Average Amplitude')
     plt.legend(loc='best', ncol=8)
     plt.minorticks_on()
     plt.tight_layout()
     pfpgs.savefig()
     plt.close(fig)


