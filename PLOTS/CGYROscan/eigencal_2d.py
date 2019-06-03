# this script is used to do the detailed analysis of the eigenfunction
#deploypath='/home/task1/xiangjian/temp'
deploypath=root['SETTINGS']['REMOTE_SETUP']['workDir']
plots=root['SETTINGS']['PLOTS']
effnum=plots['effnum']
Para_x=plots['2d']['Para_x']
Para_y=plots['2d']['Para_y']
para_x_eigen=plots['2d']['para_x_eigen']
para_y_eigen=plots['2d']['para_y_eigen']
ky_eigen=plots['ky_eigen']
if root['SETTINGS']['PLOTS']['idimplt']==0:
    datanode=root['OUTPUTScan'][Para_x][str(para_x_eigen)[0:effnum]][Para_y][str(para_y_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
else:
    datanode=root['OUTPUTScan'][Para_x][str(para_y_eigen)[0:effnum]][Para_y][str(para_x_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
datanode.deploy(deploypath)
tag=str(plots['paraval_eigen'])+'_'+str(plots['ky_eigen'])
root['OUTPUTS'][tag]=OMFITcgyro(deploypath)
# transform from theta space to r space
output=root['OUTPUTS'][tag]
ball=output['balloon']
phi=ball['balloon_phi'].T[-1]
apar=ball['balloon_apar'].T[-1]
bpar=ball['balloon_bpar'].T[-1]
theta=ball['theta_b_over_pi']*pi
ky=output['input.cgyro.gen']['KY']
kys=ky*output['input.cgyro.gen']['S']
kr=theta*kys
# get the b_theta and j_par ,function of kr and ky
btheta=kr*apar
jpar=(kr**2+ky**2)*apar
# do the fourier transform
nr=output['input.cgyro.gen']['N_RADIAL']
ntheta=len(theta)
#n_rarr=2*ntheta+1
n_rarr=2*(ntheta/4)+1
r_arr=linspace(-4*nr,4*nr,n_rarr)  # a good start from nr and ntheta
phi_r_arr=zeros(n_rarr)+1j*zeros(n_rarr)
apar_r_arr=zeros(n_rarr)+1j*zeros(n_rarr)
btheta_r_arr=zeros(n_rarr)+1j*zeros(n_rarr)
jpar_r_arr=zeros(n_rarr)+1j*zeros(n_rarr)
bpar_r_arr=zeros(n_rarr)+1j*zeros(n_rarr)
for k in range(n_rarr):
    phi_r_arr[k]=sum([complex(real(phi[p]+phi[p+1])/2.,imag(phi[p]+phi[p+1])/2.)*exp(1j*(kr[p]+kr[p+1])/2.*r_arr[k])*(kr[k+1]-kr[k]) for p in range(ntheta-1)])
    apar_r_arr[k]=sum([complex(real(apar[p]+apar[p+1])/2.,imag(apar[p]+apar[p+1])/2.)*exp(1j*(kr[p]+kr[p+1])/2.*r_arr[k])*(kr[k+1]-kr[k]) for p in range(ntheta-1)])
    btheta_r_arr[k]=sum([complex(real(btheta[p]+btheta[p+1])/2.,imag(btheta[p]+btheta[p+1])/2.)*exp(1j*(kr[p]+kr[p+1])/2.*r_arr[k])*(kr[k+1]-kr[k]) for p in range(ntheta-1)])
    jpar_r_arr[k]=sum([complex(real(jpar[p]+jpar[p+1])/2.,imag(jpar[p]+jpar[p+1])/2.)*exp(1j*(kr[p]+kr[p+1])/2.*r_arr[k])*(kr[k+1]-kr[k]) for p in range(ntheta-1)])
#bpar_r_arr[k]=sum([complex(real(bpar[p]+bpar[p+1])/2.,imag(bpar[p]+bpar[p+1])/2.)*exp(1j*(kr[p]+kr[p+1])/2.*r_arr[k])*dkr for p in range(ntheta)])
# so we store the data
output['kr']=kr
output['kys']=kys
output['nr']=nr
output['theta']=theta
output['phi']=phi
output['apar']=apar
output['btheta']=btheta
output['jpar']=jpar
output['r_arr']=r_arr
output['phi_r_arr']=phi_r_arr
output['apar_r_arr']=apar_r_arr
output['btheta_r_arr']=btheta_r_arr
output['jpar_r_arr']=jpar_r_arr
