# this script is used to plot the comparison, that's phi versus frequency, which is more convinient for the comparison of diagnostics
# 2*2, phi, delta_n, apar, br versus freq(in the unit of kHz)
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
fig=figure()
ax=fig.add_subplot(1,1,1)
fs1=24
fs2=20
fs3=16
lw=2
lab=['-bo','-ro','-ko','-go','-mo','-co']
clr=['b','r','k','g','m','c']
lab2=['--b','--r','--k','--g','--m','--c']
field=int(pltnl['field'])  # 0,1,2, only 1 is permitted
field_name={0:'phi',1:'apar',2:'bpar'}
# plot the field fluctuation spectrum
for k in range(n_case):
    casek=outputs[casename[k]]
    print(casename[k])
    casek.getbigfield()
# kxky_select(itheta,field,moment,0)
#    field =0
    itheta=0
    moment='phi'
    freq=mean(casek['freq']['omega'].T[t_ind[k]:-1],0)[1:]
    freq=sign(freq[1])*freq
    fk,ftk = casek.kxky_select(itheta,field,moment,0)
#    fk,ftk=casek.kxky_select(0,field,'phi',0)
    pk=sum(fk[:,:,:],axis=0)/casek.rho
    kyrhos=sign(casek['kyrhos'][1])*casek['kyrhos']
#    plot(sign(kyrhos,mean(pk.T[t_ind[k]:-1],0),lab[k],linewidth=lw,label=casename[k])
#    ax.errorbar(kyrhos[1:],mean(pk.T[t_ind[k]:-1],0)[1:],std(pk.T[t_ind[k]:-1],0)[1:],color=clr[k],linewidth=lw,label=casename[k])
    ax.errorbar(freq,mean(pk.T[t_ind[k]:-1],0)[1:],std(pk.T[t_ind[k]:-1],0)[1:],color=clr[k],linewidth=lw,label=casename[k])
    if root['SETTINGS']['PLOTS']['ilogx']==1:
        ax.set_xscale('log')
        xlim([kyrhos[1],kyrhos[-1]])
    print(mean(mean(pk.T[t_ind[k]:-1],0)[1:10],0))
    legend(loc=0,fontsize=fs2).draggable(True)
    title(field_name[field],fontsize=fs1,family='serif')
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('$f(cs/a)$',fontsize=fs1,family='serif')
# plot the density fluctuation spectrum
for k in range(n_case):
    casek=outputs[casename[k]]
    print(casename[k])
    casek.getbigfield()
# kxky_select(itheta,field,moment,0)
#    field =0
    itheta=0
    moment='n'
    freq=mean(casek['freq']['omega'].T[t_ind[k]:-1],0)
    freq=sign(freq[1])*freq
    fk,ftk = casek.kxky_select(itheta,field,moment,3)
#    fk,ftk=casek.kxky_select(0,field,'phi',0)
    pk=sum(fk[:,:,:],axis=0)/casek.rho
#    kyrhos=sign(casek['kyrhos'][1])*casek['kyrhos']
#    plot(sign(kyrhos,mean(pk.T[t_ind[k]:-1],0),lab[k],linewidth=lw,label=casename[k])
#    ax.errorbar(kyrhos[1:],mean(pk.T[t_ind[k]:-1],0)[1:],std(pk.T[t_ind[k]:-1],0)[1:],color=clr[k],linewidth=lw,label=casename[k])
    ax.errorbar(freq,mean(pk.T[t_ind[k]:-1],0)[1:],std(pk.T[t_ind[k]:-1],0)[1:],color=clr[k],linewidth=lw,label=casename[k])
    if root['SETTINGS']['PLOTS']['ilogx']==1:
        ax.set_xscale('log')
        xlim([kyrhos[1],kyrhos[-1]])
    print(mean(mean(pk.T[t_ind[k]:-1],0)[1:10],0))
    legend(loc=0,fontsize=fs2).draggable(True)
    title(field_name[field],fontsize=fs1,family='serif')
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('$f(cs/a)$',fontsize=fs1,family='serif')
