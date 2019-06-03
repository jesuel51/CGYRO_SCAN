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
for k in range(n_case):
    casek=outputs[casename[k]]
    print(casename[k])
    casek.getbigfield()
# kxky_select(itheta,field,moment,0)
#    field =0
    itheta=0
    moment='phi'
    fk,ftk = casek.kxky_select(itheta,field,moment,0)
#    fk,ftk=casek.kxky_select(0,field,'phi',0)
    pk=sum(fk[:,:,:],axis=0)/casek.rho
    kyrhos=sign(casek['kyrhos'][1])*casek['kyrhos']
#    plot(sign(kyrhos,mean(pk.T[t_ind[k]:-1],0),lab[k],linewidth=lw,label=casename[k])
    ax.errorbar(kyrhos[1:],mean(pk.T[t_ind[k]:-1],0)[1:],std(pk.T[t_ind[k]:-1],0)[1:],color=clr[k],linewidth=lw,label=casename[k])
    # plot ky*phi
#    ax.plot(kyrhos[1:],kyrhos[1:]*mean(pk.T[t_ind[k]:-1],0)[1:],color=clr[k*2],linewidth=lw)
    if root['SETTINGS']['PLOTS']['ilogx']==1:
        ax.set_xscale('log')
        xlim([kyrhos[1],kyrhos[-1]])
    if root['SETTINGS']['PLOTS']['ilogy']==1:
        ax.set_yscale('log')
    print(mean(mean(pk.T[t_ind[k]:-1],0)[1:10],0))
    legend(loc=0,fontsize=fs2).draggable(True)
    title(field_name[field],fontsize=fs1,family='serif')
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('$k_y\\rho_s$',fontsize=fs1,family='serif')
# temp plot
#figure()
#phi_ave=zeros(n_case)
#for k in range(n_case):
#    phi_ave[k]=mean(mean(pk.T[t_ind[k]:-1],0),0)
#plot(array([-0.8,-0.6,-0.4,0.25]),phi_ave,'-ro')
