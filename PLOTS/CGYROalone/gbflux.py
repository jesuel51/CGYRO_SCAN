# this script is used to plot the comparison of time traces of different flux channel, including Qi, Qe, Gamma_E, PI
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
lab=['-b','-r','-k','-g','-m','-c']
lab2=['--b','--r','--k','--g','--m','--c']
chan=pltnl['chan']  # which channel to be compared, including  Q_*, G_*,P_*, multiple value is available
field=int(pltnl['field'])  # 0,1,2, only single value is permitted
dic1={'Q':'energy','G':'particle','P':'momentum'}
nchan=len(chan)
chan_ave=zeros(n_case)
chan_std=zeros(n_case)  # standard error
for ic in range(nchan):
    subplot(1,nchan,ic+1)
    for k in range(n_case):
        casek=outputs[casename[k]]
        chan_name_in=dic1[chan[ic].split('_')[0]]
        speci=chan[ic].split('_')[1]
        speci=int(speci)
        plot(casek['t'],casek['flux_t'][chan_name_in][speci][field],lab[k],linewidth=lw,label=casename[k])
        chan_ave[k]=mean(casek['flux_t'][chan_name_in][speci][field][t_ind[k]:-1])
        chan_std[k]=std(casek['flux_t'][chan_name_in][speci][field][t_ind[k]:-1])
        plot(array([casek['t'][t_ind[k]],casek['t'][-1]]),array([chan_ave[k],chan_ave[k]]),lab2[k],linewidth=lw)
        plot(array([casek['t'][t_ind[k]],casek['t'][-1]]),array([chan_ave[k]-chan_std[k],chan_ave[k]-chan_std[k]]),lab2[k],linewidth=lw/2)
        plot(array([casek['t'][t_ind[k]],casek['t'][-1]]),array([chan_ave[k]+chan_std[k],chan_ave[k]+chan_std[k]]),lab2[k],linewidth=lw/2)
#        text(outputs[casename[k]]['t'][-1],chan_ave[k],chan_ave[k],'color',lab[k][0])
        text(outputs[casename[k]]['t'][-1],chan_ave[k],str(int(10000.*chan_ave[k])/1.e4)+'+-'+str(int(10000.*chan_std[k])/1.e4))
        print(chan[ic]+'-'+casename[k]+':%6.2f'%float(chan_ave[k]))
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    title(chan[ic],fontsize=fs1)
    xlabel('$time(a/c_s)$',fontsize=fs1,family='serif')
    if ic==0:
        legend(loc=0,fontsize=fs2).draggable(True)
