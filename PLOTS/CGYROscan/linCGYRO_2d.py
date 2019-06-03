# this script is used to plot the eigenfrequency and growth rate for all the scanning cases, 
# the parameters and the value is specified in root['SETTINGS']['PLOTS']['2d']['Para_x'] and root['SETTINGS']['PLOTS']['Range_x'] as well as 
# root['SETTINGS']['PLOTS']['2d']['Para_y'] and root['SETTINGS']['PLOTS']['Range_y']
# note the stability analyis should be performed by CGYRO before running this plot scrip
# first we should define a function to read the date of out.gyro.freq, which contains the frequency and growth rate
#plt.close()
import numpy as np
from matplotlib import ticker, cm
def readfile(filename):
    f=open(filename,'Ur')
    fread=f.readlines()
# version 1
#    fread=array(fread)
#    print(fread)
#    data=[float(item) for item in fread.split()]
#    w1=array(data[-4:-2])
#    w2=array(data[-2:])
# version 2
    w1=[float(item) for item in fread[-2].split()]
    w2=[float(item) for item in fread[-1].split()]
    w1=array(w1)
    w2=array(w2)
    w=(w1+w2)/2.
    err_w=[abs(item) for item in (w1-w2)/2.]
    for k in range(2):
        if err_w[k]<1.e-6:   # avoid 0
            err_w[k]=1.e-6
    return w,err_w
    f.close()
# then read all the data
effnum=root['SETTINGS']['PLOTS']['effnum']
input_cgyro=root['INPUTS']['input.cgyro']
# note that it make no sense that scale the gamma_e in the linear run
plots=root['SETTINGS']['PLOTS']['2d']
physics=root['SETTINGS']['PLOTS']['2d']
if root['SETTINGS']['PLOTS']['iflwphy']==1:
    plots['Para_x']=physics['Para_x']
    plots['Para_y']=physics['Para_y']
    plots['Range_x']=physics['Range_x']
    plots['Range_x']=physics['Range_x']
    plots['kyarr']=physics['kyarr']
#kyarr=root['SETTINGS']['SETUP']['kyarr']
kyarr=plots['kyarr']
Para_x=plots['Para_x']
Para_y=plots['Para_y']
Range_x=plots['Range_x']
plt2d=root['SETTINGS']['PLOTS']['2d']
ilogx=plt2d['ilogx']
ilogy=plt2d['ilogy']
ilogz=plt2d['ilogz']
Range_y=plots['Range_y']
# determine whether plot the ExB shearing rate, the capability of plotting ExB is unvailable at present
#ipltExB=root['SETTINGS']['PLOTS']['ipltExB']
#gammae_eff = 0.3*sqrt(kappa)*gamma_e
num_ky=len(kyarr)
#nRange=len(root['INPUTS']['TGYRO']['input.tgyro']['DIR'])
nRange_x=len(Range_x)
nRange_y=len(Range_y)
w_arr=zeros([nRange_x,nRange_y,num_ky])     # dominate mode frequency
err_w_arr=zeros([nRange_x,nRange_y,num_ky])     # error in dominate mode frequency
gamma_arr=zeros([nRange_x,nRange_y,num_ky]) # dominate mode growth rate
err_gamma_arr=zeros([nRange_x,nRange_y,num_ky]) # error in dominate mode growth rate
# if the growth rate is smaller than 0, then we may need to put the really number to be a artificial one which is slightly smaller than 0 so that the over all contour plot is more sensible, this is controlled by iblw0
ibelow0=root['SETTINGS']['PLOTS']['ibelow0']
# all the information about frequency and growth rate can be get
for k in range(0,nRange_x):
    for p in range(0,nRange_y):
        count2=0
    #    print(str(Range[k]))
        for ky in kyarr:
            try:
                filename=root['OUTPUTScan'][Para_x][str(Range_x[k])[0:effnum]][Para_y][str(Range_y[p])[0:effnum]]['lin'][str(ky)[0:effnum]]['out.cgyro.freq'].filename
#                print(filename)
                w,err_w=readfile(filename)
#            filename=root['OUTPUTScan'][Para_x][str(Range_x[k])[0:effnum]][Para_y][str(Range_y[p])[0:effnum]]['lin'][str(ky)[0:effnum]]['out.cgyro.freq'].filename
#            w,err_w=readfile(filename)
                if ibelow0[0]==1:
                    if w[1]<ibelow0[1]:
                        w[1]=ibelow0[1]
            except:
#            print('not work.')
                w=array([0,0])
                err_w=array([1,1])
            w_arr[k][p][count2]=w[0]
            gamma_arr[k][p][count2]=w[1]
            err_w_arr[k][p][count2]=err_w[0]
            err_gamma_arr[k][p][count2]=err_w[1]
            count2=count2+1
########################################
# based on the profiles we get, then all the linear information can be plotted
lab=['-kd','-md','-bd','-rd','-gd','-ko','-mo','-bo','-ro','-go','-k*','-m*','-b*','-r*','-g*'\
     '--k','--m','--b','--r','--g','-k', '-m', '-b', '-r' ];#       '-ko','-k*','-md','-mo','-m*','-bd','-bo','-b*','-rd','-ro','-r*','-gd','go','-g*']
lw=2
fs1=20
fs2=16
fs3=24
plots=OMFIT['CGYRO_SCAN']['SETTINGS']['PLOTS']['2d']
physics=OMFIT['CGYRO_SCAN']['SETTINGS']['PHYSICS']['2d']
if plots['iflwphy']==1:
    plots['Para_x']=physics['Para_x']
    plots['Para_y']=physics['Para_y']
    plots['Range_x']=physics['Range_x']
    plots['Range_y']=physics['Range_y']
    plots['kyarr']=physics['kyarr']
# do the contourf plot
idimplt=root['SETTINGS']['PLOTS']['idimplt']
nky=len(plots['kyarr'])
if idimplt==0:
    Range_x_grid,Range_y_grid=meshgrid(Range_x,Range_y)
else:
    Range_x_grid,Range_y_grid=meshgrid(Range_y,Range_x)
for k in range(nky):
    fig=figure(str(kyarr[k]),figsize=[12,12])
    ax = fig.gca(projection='3d')
    ax1=subplot(2,2,1)
    if idimplt==0:
        contourf(Range_x,Range_y,w_arr.T[k],cmap='seismic')
        if ilogx==1:
            ax1.set_xscale('log')
        if ilogy==1:
            ax1.set_yscale('log')
        colorbar()
#        try:
#            cs=contour(Range_x_grid,Range_y_grid,w_arr.T[k],[0])
#            p = cs.collections[0].get_paths()[0]
#            v = p.vertices
#            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
#        except:
#            print('not work at the 221')
#            continue
    else:
        contourf(Range_y,Range_x,w_arr.T[k].T,cmap='seismic')
        colorbar()
        if ilogx==1:
            ax1.set_yscale('log')
        if ilogy==1:
            ax1.set_xscale('log')
        try:
            cs=contour(Range_x_grid,Range_y_grid,w_arr.T[k].T,[0])
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
            print('not work at the 221')
            continue
    if idimplt==0:
        ylabel(plots['Para_y'],fontsize=fs2,family='serif')
    else:
        ylabel(plots['Para_x'],fontsize=fs2,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    title('$\omega$',fontsize=fs1,family='serif')
    ax3=subplot(2,2,3)
    if idimplt==0:
        if ilogz==1:
            contourf(Range_x,Range_y,gamma_arr.T[k],locator=ticker.LogLocator(),cmap='seismic')
        else:
            contourf(Range_x,Range_y,gamma_arr.T[k],cmap='seismic')
        if ilogx==1:
            ax3.set_xscale('log')
        if ilogy==1:
            ax3.set_yscale('log')
        colorbar()
        cs=contour(Range_x_grid,Range_y_grid,gamma_arr.T[k],[0])
        try:
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
            print('not work at the 223')
            print('2223 no w=0 data!')
#            continue
    else:
        if ilogz==1:
#            contourf(Range_x,Range_y,gamma_arr.T[k],locator=ticker.LogLocator(),cmap='seismic')
            contourf(Range_y,Range_x,gamma_arr.T[k].T,locator=ticker.LogLocator(),cmap='seismic')
        else:
            contourf(Range_y,Range_x,gamma_arr.T[k].T,cmap='seismic')
        if ilogx==1:
            ax3.set_yscale('log')
        if ilogy==1:
            ax3.set_xscale('log')
        colorbar()
        cs=contour(Range_x_grid,Range_y_grid,gamma_arr.T[k].T,[0])
        try:
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
            print('not work at the 223')
            print('2223 no w=0 data!')
#            continue
    if idimplt==0:
        xlabel(plots['Para_x'],fontsize=fs2,family='serif')
        ylabel(plots['Para_y'],fontsize=fs2,family='serif')
    else:
        xlabel(plots['Para_y'],fontsize=fs2,family='serif')
        ylabel(plots['Para_x'],fontsize=fs2,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    title('$\gamma$',fontsize=fs1,family='serif')
    ax2=subplot(2,2,2)
    if idimplt==0:
        contourf(Range_x,Range_y,log10(err_w_arr.T[k]))
        if ilogx==1:
            ax2.set_xscale('log')
        if ilogy==1:
            ax2.set_yscale('log')
        colorbar()
        try:
            cs=contour(Range_x_grid,Range_y_grid,err_w_arr.T[k],[1.e-3])
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw)
        except:
            print('not work at the 222')
            print('222 no log10(Err)=-3 data!')
    else:
        contourf(Range_y,Range_x,log10(err_w_arr.T[k].T))
        if ilogx==1:
            ax2.set_yscale('log')
        if ilogy==1:
            ax2.set_xscale('log')
        colorbar()
        try:
            cs=contour(Range_x_grid,Range_y_grid,err_w_arr.T[k].T,[1.e-3])
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
            print('222 no log10(Err)=-3 data!')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    title('$err_\omega$',fontsize=fs1,family='serif')
    ax4=subplot(2,2,4)
    if idimplt==0:
        contourf(Range_x,Range_y,log10(err_gamma_arr.T[k]))
        if ilogx==1:
            ax4.set_xscale('log')
        if ilogy==1:
            ax4.set_yscale('log')
        colorbar()
        try:
            cs=contour(Range_x_grid,Range_y_grid,err_gamma_arr.T[k],[1.e-3])
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
#            continue
            print('not work at the 224')
            print('224 no log10(Err)=-3 data!')
    else:
        contourf(Range_y,Range_x,log10(err_gamma_arr.T[k].T))
        if ilogx==1:
            ax4.set_yscale('log')
        if ilogy==1:
            ax4.set_xscale('log')
        colorbar()
        try:
            cs=contour(Range_x_grid,Range_y_grid,err_gamma_arr.T[k].T,[1.e-3])
            p = cs.collections[0].get_paths()[0]
            v = p.vertices
            plot(v[:,0],v[:,1],'--r',linewidth=lw*2)
        except:
#            continue
            print('224 no log10(Err)=-3 data!')
    if idimplt==0:
        xlabel(plots['Para_x'],fontsize=fs2,family='serif')
#        ylabel(plots['Para_y'],fontsize=fs2,family='serif')
    else:
        xlabel(plots['Para_y'],fontsize=fs2,family='serif')
#        xlabel(plots['Para_x'],fontsize=fs2,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    title('$err_\gamma$',fontsize=fs1,family='serif')
# # ===================================
iwritelin=root['SETTINGS']['PLOTS']['iwritelin']  # determine whether to write out to a file
numky=len(kyarr) 
nmodes=1
if iwritelin==1 and root['SETTINGS']['DEPENDENCIES'].has_key('linout'):
    eigenout=root['SETTINGS']['DEPENDENCIES']['linout']
    fid=open(eigenout,'w')
# first write the scanned parameter name into the file
    fid.write(Para_x+'    '+Para_y)
    fid.write('\n')
# write the nRange and the para_val into the file
    fid.write(str(len(Range_x))+'    '+str(len(Range_y)))
    fid.write('\n')
    line=''
    for m in range(len(Range_x)):
        line=line+str(Range_x[m])+'    '
    fid.write(line)
    fid.write('\n')
    line=''
    for m in range(len(Range_y)):
        line=line+str(Range_y[m])+'    '
    fid.write(line)
    fid.write('\n')
# write nmodes into the file    
    fid.write(str(nmodes)+'    '+str(numky))
    fid.write('\n')
    for k in range(numky):
        line=str(kyarr[k])
        for p in range(len(Range_x)):
            for q in range(len(Range_y)):
# w_arr=zeros([nRange_x,nRange_y,num_ky])
#            line=line+'    '+str(w_arr[p][k])+'    '+str(gamma_arr[p][k])+'    '+str(err_w_arr[p][k])+'    '+str(err_gamma_arr[p][k])
                line=line+'    '+str(w_arr[p][q][k])+'    '+str(gamma_arr[p][q][k])
        fid.write(line)
        fid.write('\n')
    fid.close()
