import numpy as np

aoa_array = [-180, -175, -170, -165,
                -160, -152, -144, -136, -128,
                -120, -110, -100, 
                -90, -80, -70, -60, -50, -40
                -33, -30, -27, -24, -21, -18,
                -15, -12, -9, -6, -3,
                0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
                40, 50, 60, 70, 80, 90,
                100, 110, 120,
                128, 136, 144, 152, 160,
                165, 170, 175, 180]

###############################################################
# User inputs:
numpts = 335
af_name = "ffa_w3_211"

# numpts for the rest of the airfoils, flat plate and cylinder:
# 241: 328
# 270: 325
# 301: 320
# 330: 315
# 360: 315
# 500: 300
# flat plate: 339
# cylinder: 228
###############################################################

for i, aoa in enumerate(aoa_array):

    with open('IEA_Airfoil_Mesh.glf','r') as firstfile, open('tmp_grid_'+str(aoa)+'.glf','w') as secondfile: 
      
         # read content from first file 
         for line in firstfile: 
               
             # write content to second file 
             secondfile.write(line)

for i, aoa in enumerate(aoa_array):

    with open('tmp_grid_'+str(aoa)+'.glf','r') as file:

         data = file.read()
         data = data.replace("335", str(numpts))
         data = data.replace("32", str(aoa))       
         data = data.replace("ffa_w3_211_coords.dat", af_name+"_coords.dat")
     
         if aoa < 0:
            data = data.replace("set percent_ule 1",  "set percent_ule 50")       
            data = data.replace("set percent_lle 50",  "set percent_lle 1")       
          
         if np.abs(aoa) > 110: 
            data = data.replace("$_TMP(PW_5) setName inlet", "$_TMP(PW_5) setName outlet")    
            data = data.replace("$_TMP(PW_3) setName outlet", "$_TMP(PW_3) setName inlet")
    
    with open('tmp_grid_'+str(aoa)+'.glf', 'w') as file: 
  
         # Writing the replaced data in our 
         # text file 
         file.write(data) 

    subprocess.call(["/projects/hfm/Fidelity/Pointwise/Pointwise2022.1.2/pointwise", "-b", "tmp_grid_"+str(aoa)+".glf"])
