#!/usr/bin/env python3

#part of AMDGPU-GUI by Thomas Collins
#version 0.0.2
#this isnt done yet its a work in progress
#make sure you have lm-sensors installed
#this only works on linux with amdgpu driver 
#it has been tested on debian stretch
#please visit the github page for more info: https://github.com/AllAboutThatTEC/AMDGPU-GUI

import os
import subprocess
import re

gpu_pre = subprocess.check_output(["sensors | grep amdgpu"], shell=True) #finds the name of the amd gpu im the system

gpu = (gpu_pre.decode('ascii').strip()) #converts the output of the above command from bytes format to ascii and removes skip line characters

#print (gpu) #for debug purposes prints the name of the graphics card

fetch_temp_cmd = "sensors -u "+ gpu #constructs the command to find the temperature data and stores it as a string 

#print (fetch_temp_cmd) #for debug purposes prints the constructed command

data_pre = subprocess.check_output([fetch_temp_cmd], shell=True) #exectutes the command

data = (data_pre.decode('ascii').strip()) #converts the output from bytes to ascii and removes skip line characters

data_file = open("temp_data.txt", "w") #create and open a file to store the temp data in

data_file.write(data) #writes the gathered data to the text file

data_file.close() #closes the file 

#print (data) #prints the full decoded hopefully correct temp data

temp1_input = subprocess.check_output(["cat temp_data.txt | grep temp1_input"], shell=True) #fetches the output of temp1_input 

print (temp1_input.decode('ascii').strip())


