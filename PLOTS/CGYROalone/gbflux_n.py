# this script is used to plot the comparison of flux spectrum
# specifically, the flux/dky will be plotted for better comparison
pltnl=root['SETTINGS']['PLOTS']['nl']
t_ave=pltnl['t_ave']  # average over [1-t_ave,1]*time_tot
path=pltnl['path']
n_case=len(path.keys())
casename=[]
for k in range(n_case):
    casename.append(path.keys()[k])
t_ind=zeros([n_case])
outputs=root['OUTPUTS']
for k in range(n_case):
    t_ind[k]=int((1-t_ave)*outputs[casename[k]]['n_time'])
t_ind=[int(item) for item in t_ind]
figure()
fs1=24
fs2=20
fs3=16
lw=2
lab=['-bo','-ro','-ko','-go','-mo','-co']
clr=['b','r','k','g','m','c']
lab2=['--b','--r','--k','--g','--m','--c']
chan=pltnl['chan']  # which channel to be compared, including  Q_*, G_*,P_*, multiple value is available
field=int(pltnl['field'])  # 0,1,2, only single value is permitted
dic1={'Q':'energy','G':'particle','P':'momentum'}
nchan=len(chan)
chan_ave=zeros(n_case)
for ic in range(nchan):
    ax=subplot(1,nchan,ic+1)
    for k in range(n_case):
        casek=outputs[casename[k]]
        chan_name_in=dic1[chan[ic].split('_')[0]]
        speci=chan[ic].split('_')[1]
        speci=int(speci)
        dky=sign(casek['kyrhos'][1])*casek['kyrhos'][1]
#        plot(sign(casek['kyrhos'][1])*casek['kyrhos'],mean(casek['flux_ky'][chan_name_in][speci][field].T[t_ind[k]:-1],0)/dky,lab[k],linewidth=lw,label=casename[k])
        errorbar(sign(casek['kyrhos'][1])*casek['kyrhos'],mean(casek['flux_ky'][chan_name_in][speci][field].T[t_ind[k]:-1],0)/dky,std(casek['flux_ky'][chan_name_in][speci][field].T[t_ind[k]:-1],0)/dky,color=clr[k],linewidth=lw,label=casename[k])
        chan_ave[k]=mean(casek['flux_t'][chan_name_in][speci][field][t_ind[k]:-1])
        print(chan[ic]+'-'+casename[k]+':%6.2f'%float(chan_ave[k]))
    if root['SETTINGS']['PLOTS']['ilogx']==1:
        ax.set_xscale('log')
        xlim([kyrhos[1],kyrhos[-1]])
    if root['SETTINGS']['PLOTS']['ilogy']==1:
        ax.set_yscale('log')
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    title(chan[ic],fontsize=fs1)
    xlabel('$k_y\\rho_s$',fontsize=fs1,family='serif')
    if ic==0:
        legend(loc=0,fontsize=fs2).draggable(True)
        ylabel('$'+chan[ic]+'/\\Delta_{ky}$',fontsize=fs1)
