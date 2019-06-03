# this script is used to raad the eigenfunction of the ky and parameter that you specified
# the name, value and ky should be specified
plots=root['SETTINGS']['PLOTS']
effnum=plots['effnum']
para=plots['Para']
paraval_eigen=plots['paraval_eigen']
ky_eigen=plots['ky_eigen']
datanode=root['OUTPUTScan'][para][str(paraval_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
# what we do is to use the cgyro_plot to plot the eigenfunction
#deploypath='/home/xiangjian/temp/'
deploypath=root['SETTINGS']['REMOTE_SETUP']['workDir']
datanode.deploy(deploypath)
# two methods can be used to plot the eigenfunction, 
# 0: system plot , default
# 1: plot by myself, very time consuming
ipltmthd=0
# determine the xlabel to be theta or kr
# 0: kr
# 1: theta
ikrtheta=1
if ipltmthd==0:
    cmd='cd '+deploypath+' ;'
    cmd=cmd + 'module purge;'
    cmd=cmd + 'module load omfit/unstable;'
    cmd=cmd + 'cgyro_plot -plot ball -field 0;'
    if datanode['input.cgyro']['N_FIELD']>1:
        cmd=cmd+'cgyro_plot -plot ball -field 1'
    os.system(cmd)
else:
    # caleigen
#    root['PLOTS']['CGYROscan']['eigencal.py'].run()
    # get the data
    plots=root['SETTINGS']['PLOTS']
    tag=str(plots['paraval_eigen'])+'_'+str(plots['ky_eigen'])
    output=root['OUTPUTS'][tag]
    theta=output['theta']
    kr=output['kr']
    kys=output['kys']
    nr=output['nr']
    phi=output['phi']
    apar=output['apar']
    btheta=output['btheta']
    jpar=output['jpar']
    r_arr=output['r_arr']
    phi_r_arr=output['phi_r_arr']
    apar_r_arr=output['apar_r_arr']
    btheta_r_arr=output['btheta_r_arr']
    jpar_r_arr=output['jpar_r_arr']
    # plot
    figure(figsize=[20,12])
    fs1=24
    fs2=20
    fs3=16
    lw=2
    phi_0=spline(theta,phi,0)
    apar_0=spline(theta,apar,0)
    btheta_0=spline(theta,btheta,0)
    jpar_0=spline(theta,jpar,0)
    phi_r_0=spline(r_arr,phi_r_arr,0)
    apar_r_0=spline(r_arr,apar_r_arr,0)
    btheta_r_0=spline(r_arr,btheta_r_arr,0)
    jpar_r_0=spline(r_arr,jpar_r_arr,0)
    phi_norm=phi/phi_0
    apar_norm=apar/apar_0
    btheta_norm=btheta/btheta_0
    jpar_norm=jpar/jpar_0
    phi_r_norm=phi_r_arr/phi_r_0
    apar_r_norm=apar_r_arr/apar_r_0
    btheta_r_norm=btheta_r_arr/btheta_r_0
    jpar_r_norm=jpar_r_arr/jpar_r_0
    subplot(4,3,1)
    if ikrtheta==1:
#        plot(theta/pi,real(phi)/max(abs(real(phi)+1j*imag(phi))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(phi)/max(abs(real(phi)+1j*imag(phi))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-r',linewidth=lw,label='real-norm')
        plot(theta/pi,imag(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'--r',linewidth=lw,label='imag-norm')
        legend(loc=0,fontsize=fs3).draggable(True)
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
        xlim([-nr+1,nr-1])
    else:
#        plot(kr/pi,real(phi)/max(abs(real(phi)+1j*imag(phi))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(phi)/max(abs(real(phi)+1j*imag(phi))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-r',linewidth=lw,label='real-norm')
        plot(kr/pi,imag(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'--r',linewidth=lw,label='imag-norm')
        legend(loc=0,fontsize=fs3).draggable(True)
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
        xlim([(-nr+1)*kys,(nr-1)*kys])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    title('$\phi$',fontsize=fs1,family='serif')
    subplot(4,3,4)
    if ikrtheta==1:
#        plot(theta/pi,real(apar)/max(abs(real(apar)+1j*imag(apar))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(apar)/max(abs(real(apar)+1j*imag(apar))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-r',linewidth=lw,label='real-norm')
        plot(theta/pi,imag(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([-nr+1,nr-1])
#        xlabel('$\\theta(\pi)$',fontsize=fs2,family='serif')
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    else:
#        plot(kr/pi,real(apar)/max(abs(real(apar)+1j*imag(apar))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(apar)/max(abs(real(apar)+1j*imag(apar))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-r',linewidth=lw,label='real-norm')
        plot(kr/pi,imag(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([(-nr+1)*kys,(nr-1)*kys])
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
#        xlabel('$k_r(\pi)$',fontsize=fs2,family='serif')
    title('$A_{||}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,7)
    if ikrtheta==1:
#        plot(theta/pi,real(btheta)/max(abs(real(btheta)+1j*imag(btheta))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(btheta)/max(abs(real(btheta)+1j*imag(btheta))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(btheta_norm)/max(abs(real(btheta_norm)+1j*imag(btheta_norm))),'-r',linewidth=lw,label='real-norm')
        plot(theta/pi,imag(btheta_norm)/max(abs(real(btheta_norm)+1j*imag(btheta_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([-nr+1,nr-1])
        xlabel('$\\theta(\pi)$',fontsize=fs2,family='serif')
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    else:
#        plot(kr/pi,real(btheta)/max(abs(real(btheta)+1j*imag(btheta))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(btheta)/max(abs(real(btheta)+1j*imag(btheta))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(btheta_norm)/max(abs(real(btheta_norm)+1j*imag(btheta_norm))),'-r',linewidth=lw,label='real-norm')
        plot(kr/pi,imag(btheta_norm)/max(abs(real(btheta_norm)+1j*imag(btheta_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([(-nr+1)*kys,(nr-1)*kys])
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
#        xlabel('$k_r(\pi)$',fontsize=fs2,family='serif')
    title('$b_{\\theta}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,10)
    if ikrtheta==1:
#        plot(theta/pi,real(jpar)/max(abs(real(jpar)+1j*imag(jpar))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(jpar)/max(abs(real(jpar)+1j*imag(jpar))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(jpar_norm)/max(abs(real(jpar_norm)+1j*imag(jpar_norm))),'-r',linewidth=lw,label='real-norm')
        plot(theta/pi,imag(jpar_norm)/max(abs(real(jpar_norm)+1j*imag(jpar_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([-nr+1,nr-1])
        xlabel('$\\theta(\pi)$',fontsize=fs2,family='serif')
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    else:
#        plot(kr/pi,real(jpar)/max(abs(real(jpar)+1j*imag(jpar))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(jpar)/max(abs(real(jpar)+1j*imag(jpar))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(jpar_norm)/max(abs(real(jpar_norm)+1j*imag(jpar_norm))),'-r',linewidth=lw,label='real-norm')
        plot(kr/pi,imag(jpar_norm)/max(abs(real(jpar_norm)+1j*imag(jpar_norm))),'--r',linewidth=lw,label='imag-norm')
        xlim([(-nr+1)*kys,(nr-1)*kys])
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
        xlabel('$k_r(\pi)$',fontsize=fs2,family='serif')
    title('$j_{||}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,2)
#    plot(r_arr,real(phi_r_arr)/max(abs(phi_r_arr)),'-b',linewidth=lw)
#    plot(r_arr,imag(phi_r_arr)/max(abs(phi_r_arr)),'--b',linewidth=lw)
    plot(r_arr,real(phi_r_norm)/max(abs(phi_r_norm)),'-r',linewidth=lw)
    plot(r_arr,imag(phi_r_norm)/max(abs(phi_r_norm)),'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    title('$\phi$',fontsize=fs1,family='serif')
    subplot(4,3,5)
#    plot(r_arr,real(apar_r_arr)/max(abs(apar_r_arr)),'-b',linewidth=lw)
#    plot(r_arr,imag(apar_r_arr)/max(abs(apar_r_arr)),'--b',linewidth=lw)
    plot(r_arr,real(apar_r_norm)/max(abs(apar_r_norm)),'-r',linewidth=lw)
    plot(r_arr,imag(apar_r_norm)/max(abs(apar_r_norm)),'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
#    xlabel('r',fontsize=fs2,family='serif')
    title('$A_{||}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,8)
#    plot(r_arr,real(btheta_r_arr)/max(abs(btheta_r_arr)),'-b',linewidth=lw)
#    plot(r_arr,imag(btheta_r_arr)/max(abs(btheta_r_arr)),'--b',linewidth=lw)
    plot(r_arr,real(btheta_r_norm)/max(abs(btheta_r_norm)),'-r',linewidth=lw)
    plot(r_arr,imag(btheta_r_norm)/max(abs(btheta_r_norm)),'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlabel('r',fontsize=fs2,family='serif')
    title('$b_{\\theta}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,11)
#    plot(r_arr,real(jpar_r_arr)/max(abs(jpar_r_arr)),'-b',linewidth=lw)
#    plot(r_arr,imag(jpar_r_arr)/max(abs(jpar_r_arr)),'--b',linewidth=lw)
    plot(r_arr,real(jpar_r_norm)/max(abs(jpar_r_norm)),'-r',linewidth=lw)
    plot(r_arr,imag(jpar_r_norm)/max(abs(jpar_r_norm)),'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
#    xlabel('r',fontsize=fs2,family='serif')
    title('$j_{||}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,3)
    plot(r_arr,abs(phi_r_arr)/max(abs(phi_r_arr)),'-k',linewidth=lw,label='mode')
    plot(r_arr,angle(phi_r_arr)/pi,'--k',linewidth=lw,label='arg($\pi$)')
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--r',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--r',linewidth=lw/2.)
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    legend(loc=0,fontsize=fs2).draggable(True)
    title('$\phi$',fontsize=fs1,family='serif')
    subplot(4,3,6)
    plot(r_arr,abs(apar_r_arr)/max(abs(apar_r_arr)),'-k',linewidth=lw)
    plot(r_arr,angle(apar_r_arr)/pi,'--k',linewidth=lw)
    legend(loc=0,fontsize=fs2).draggable(True)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--r',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--r',linewidth=lw/2.)
    title('$A_{||}$',fontsize=fs2,family='serif')
#    xlabel('r',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,9)
    plot(r_arr,abs(btheta_r_arr)/max(abs(btheta_r_arr)),'-k',linewidth=lw)
    plot(r_arr,angle(btheta_r_arr)/pi,'--k',linewidth=lw)
    legend(loc=0,fontsize=fs2).draggable(True)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--r',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--r',linewidth=lw/2.)
    title('$b_{\\theta}$',fontsize=fs2,family='serif')
    xlabel('r',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    subplot(4,3,12)
    plot(r_arr,abs(jpar_r_arr)/max(abs(jpar_r_arr)),'-k',linewidth=lw)
    plot(r_arr,angle(jpar_r_arr)/pi,'--k',linewidth=lw)
    legend(loc=0,fontsize=fs2).draggable(True)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--r',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--r',linewidth=lw/2.)
    title('$j_{||}$',fontsize=fs2,family='serif')
#    xlabel('r',fontsize=fs2,family='serif')
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    # figure on the jpar
    figure(figsize=[20,12])
#    btheta=gradient(apar_r_arr)/gradient(r_arr)
#    jpar=gradient(btheta)/gradient(r_arr)
#    btheta=btheta_r_arr
#    jpar=jpar_r_arr
    subplot(3,2,1)
    plot(r_arr,real(apar_r_arr)/max(abs(apar_r_arr)),'-r',linewidth=lw,label='real')
    plot(r_arr,imag(apar_r_arr)/max(abs(apar_r_arr)),'--b',linewidth=lw,label='imag')
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    ylabel('$A_{||}$',fontsize=fs3,family='serif')
    legend(loc=0,fontsize=fs3).draggable(True)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    subplot(3,2,3)
    plot(r_arr,real(btheta_r_arr)/max(abs(btheta_r_arr)),'-r',linewidth=lw)
    plot(r_arr,imag(btheta_r_arr)/max(abs(btheta_r_arr)),'--b',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    ylabel('$b_{\\theta}$',fontsize=fs3,family='serif')
    subplot(3,2,5)
    plot(r_arr,real(jpar_r_arr)/max(abs(jpar_r_arr)),'-r',linewidth=lw)
    plot(r_arr,imag(jpar_r_arr)/max(abs(jpar_r_arr)),'--b',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    ylabel('$j_{||}$',fontsize=fs1,family='serif')
    xlabel('$r$',fontsize=fs1,family='serif')
    subplot(3,2,2)
    plot(r_arr,abs(apar_r_arr)/max(abs(apar_r_arr)),'-b',linewidth=lw,label='amp')
    plot(r_arr,angle(apar_r_arr)/pi,'--r',linewidth=lw,label='arg($\pi$)')
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
#    ylabel('$A_||$',fontsize=fs3,family='serif')
    legend(loc=0,fontsize=fs3).draggable(True)
    subplot(3,2,4)
    plot(r_arr,abs(btheta_r_arr)/max(abs(btheta_r_arr)),'-b',linewidth=lw)
    plot(r_arr,angle(btheta_r_arr)/pi,'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
#    ylabel('$b_{\\theta}$',fontsize=fs3,family='serif')
    subplot(3,2,6)
    plot(r_arr,abs(jpar_r_arr)/max(abs(jpar_r_arr)),'-b',linewidth=lw)
    plot(r_arr,angle(jpar_r_arr)/pi,'--r',linewidth=lw)
    plot(array([r_arr[0],r_arr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    xlim([r_arr[0],r_arr[-1]])
    ylim([-1,1])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
#    ylabel('$A_||$',fontsize=fs1,family='serif')
    xlabel('$r$',fontsize=fs1,family='serif')
# plot the presentation results
    figure(figsize=[8,10])
    subplot(2,1,1)
    if ikrtheta==1:
#        plot(theta/pi,real(phi)/max(abs(real(phi)+1j*imag(phi))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(phi)/max(abs(real(phi)+1j*imag(phi))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-r',linewidth=lw,label='real')
        plot(theta/pi,imag(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-b',linewidth=lw,label='imag')
        legend(loc=0,fontsize=fs3).draggable(True)
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
        xlim([-nr+1,nr-1])
    else:
#        plot(kr/pi,real(phi)/max(abs(real(phi)+1j*imag(phi))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(phi)/max(abs(real(phi)+1j*imag(phi))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-r',linewidth=lw,label='real')
        plot(kr/pi,imag(phi_norm)/max(abs(real(phi_norm)+1j*imag(phi_norm))),'-b',linewidth=lw,label='imag')
        legend(loc=0,fontsize=fs3).draggable(True)
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
        xlim([(-nr+1)*kys,(nr-1)*kys])
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    title('$\phi$',fontsize=fs1,family='serif')
    subplot(2,1,2)
    if ikrtheta==1:
#        plot(theta/pi,real(apar)/max(abs(real(apar)+1j*imag(apar))),'-b',linewidth=lw,label='real')
#        plot(theta/pi,imag(apar)/max(abs(real(apar)+1j*imag(apar))),'--b',linewidth=lw,label='imag')
        plot(theta/pi,real(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-r',linewidth=lw,label='real')
        plot(theta/pi,imag(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-b',linewidth=lw,label='imag')
        xlim([-nr+1,nr-1])
        xlabel('$\\theta(\pi)$',fontsize=fs2,family='serif')
        plot(array([theta[0],theta[-1]]),array([0,0]),'--k',linewidth=lw/2.)
        plot(array([0,0]),array([-1,1]),'--k',linewidth=lw/2.)
    else:
#        plot(kr/pi,real(apar)/max(abs(real(apar)+1j*imag(apar))),'-b',linewidth=lw,label='real')
#        plot(kr/pi,imag(apar)/max(abs(real(apar)+1j*imag(apar))),'--b',linewidth=lw,label='imag')
        plot(kr/pi,real(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-r',linewidth=lw,label='real')
        plot(kr/pi,imag(apar_norm)/max(abs(real(apar_norm)+1j*imag(apar_norm))),'-b',linewidth=lw,label='imag')
        xlim([(-nr+1)*kys,(nr-1)*kys])
        xlabel('$k_r(\pi)$',fontsize=fs2,family='serif')
        plot(array([kr[0],kr[-1]]),array([0,0]),'--k',linewidth=lw/2.)
    xticks(fontsize=fs3,family='serif')
    yticks(fontsize=fs3,family='serif')
    title('$A_{||}$',fontsize=fs1,family='serif')
