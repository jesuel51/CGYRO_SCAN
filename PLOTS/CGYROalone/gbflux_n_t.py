# this script is used to plot the flux spectrum variation versus time for a single case
pltnl=root['SETTINGS']['PLOTS']['nl']
t_trace=pltnl['t_trace']
t_ave=pltnl['t_ave']  # average over t_trace-t_ave/2*time_tot,t_trace+t_ave/2*time_tot
path=pltnl['path']
n_time=len(t_trace)
#t_trace=[]
#for k in range(n_time):
#    t_trace.append(path.keys()[k])
#t_ind=zeros([n_time])
t_ind=ones([n_time,2])
case_t_trace=root['SETTINGS']['PLOTS']['nl']['case_t_trace']
outputs=root['OUTPUTS'][case_t_trace]
dt_acs=outputs['t'][-1]/outputs['n_time']
for k in range(n_time):
    t_ind[k]=array([int((t_trace[k]/dt_acs-t_ave/2.*outputs['n_time'])),int((t_trace[k]/dt_acs+t_ave/2.*outputs['n_time']))])
figure()
fs1=24
fs2=20
fs3=16
lw=2
lab=['-bo','-ro','-ko','-go','-mo','-co']
lab2=['--b','--r','--k','--g','--m','--c']
chan=pltnl['chan']  # which channel to be compared, including  Q_*, G_*,P_*, multiple value is available
field=int(pltnl['field'])  # 0,1,2, only single value is permicted
dic1={'Q':'energy','G':'particle','P':'momentum'}
nchan=len(chan)
chan_ave=zeros(n_time)
#speci=int(speci)
dky=sign(outputs['kyrhos'][1])*outputs['kyrhos'][1]
inorm=0
for ic in range(nchan):
    subplot(2,nchan,ic+1)
    for k in range(n_time):
        chan_name_in=dic1[chan[ic].split('_')[0]]
        speci=chan[ic].split('_')[1]
        speci=int(speci)
        flux_n=mean(outputs['flux_ky'][chan_name_in][speci][field].T[int(t_ind[k][0]):int(t_ind[k][1])],0)/dky
        flux_n_std=std(outputs['flux_ky'][chan_name_in][speci][field].T[int(t_ind[k][0]):int(t_ind[k][1])],0)/dky
        ky_rhos=sign(outputs['kyrhos'][1])*outputs['kyrhos']
        if inorm==0:
#            plot(ky_rhos,flux_n,lab[k],linewidth=lw,label=t_trace[k])
            errorbar(ky_rhos,flux_n,flux_n_std,lab[k],linewidth=lw,label=t_trace[k])
        else:
            plot(ky_rhos,flux_n/max(flux_n),lab[k],linewidth=lw,label=t_trace[k])
        chan_ave[k]=mean(outputs['flux_t'][chan_name_in][speci][field][int(t_ind[k][0]):int(t_ind[k][1])])
#        print(chan[ic]+'-'+t_trace[k]+':%6.2f'%float(chan_ave[k]))
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlim([ky_rhos[1],ky_rhos[-1]])
    title(chan[ic],fontsize=fs1)
    xlabel('$k_y\\rho_s$',fontsize=fs1,family='serif')
    if ic==0:
        legend(loc=0,fontsize=fs2).draggable(True)
        ylabel('$'+chan[ic]+'/\\Delta_{ky}$',fontsize=fs1)
    subplot(2,nchan,nchan+ic+1)
    semilogy(outputs['t'],outputs['flux_t'][chan_name_in][speci][field],'-b',linewidth=lw)
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('t',fontsize=fs1,family='serif')
    xlim([0,outputs['t'][-1]])
