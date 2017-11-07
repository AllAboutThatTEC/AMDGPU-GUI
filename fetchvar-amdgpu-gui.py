#part of AMDGPU-GUI by Thomas Collins
#version 0.0.1
#this isnt done yet its a work in progress
#make sure you have lm-sensors installed
#this only works on linux with amdgpu driver 
#it has been tested on debian stretch
#please visit the github page for more info: https://github.com/AllAboutThatTEC/AMDGPU-GUI

import os
import subprocess

gpu_pre = subprocess.check_output(["sensors | grep amdgpu"], shell=True) #finds the name of the amd gpu im the system

gpu = (gpu_pre.decode('ascii').strip()) #converts the output of the above command from bytes format to ascii and removes skip line characters

#print (gpu) #for debug purposes prints the name of the graphics card

fetch_temp_cmd = "sensors -u "+ gpu #constructs the command to find the temperature data and stores it as a string 

#print (fetch_temp_cmd) #for debug purposes prints the constructed command

data_pre = subprocess.check_output([fetch_temp_cmd], shell=True) #exectutes the command

data = (data_pre.decode('ascii').strip()) #converts the output from bytes to ascii and removes skip line characters

print (data) #prints the full decoded hopefully correct temp data




