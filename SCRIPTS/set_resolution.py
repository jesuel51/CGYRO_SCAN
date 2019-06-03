# this script is used to setup the best resolution family according to the comments by Jeff in 
# https://fusion.gat.com/theory/Gyrousermanual
# only initial value is allowed here
input_cgyro=root['INPUTS']['input.cgyro']
reso_para=root['SETTINGS']['SETUP']['reso_para'] # they are a set of m,n and p 
m=reso_para[0]
n=reso_para[1]
p=reso_para[2]

# radial resolution
# normally, m = 3 is enough
input_cgyro['N_RADIAL'] = 2*m
input_cgyro['UP_RADIAL'] = 1.0

# poloidal resolution, normally n =4 is enough
input_cgyro['N_THETA']=2*n
input_cgyro['N_XI'] = n

# energy resolution, normally p = 0 is enough
input_cgyro['N_ENERGY']=8+p
input_cgyro['E_MAX']=int(6+sqrt(p))
