# this script is used to plot the time traces of different field and n in a single figure
pltnl=root['SETTINGS']['PLOTS']['nl']
t_ave=pltnl['t_ave']  # average over [1-t_ave,1]*time_tot
path=pltnl['path']
#n_case=len(path.keys())
casename=root['SETTINGS']['PLOTS']['nl']['case_t_trace']
#for k in range(n_case):
#    casename.append(path.keys()[k])
#t_ind=zeros([n_case])
outputs=root['OUTPUTS']
#for k in range(n_case):
#    t_ind[k]=int((1-t_ave)*outputs[casename[k]]['n_time'])
#t_ind=[int(item) for item in t_ind]
figure()
fs1=24
fs2=20
fs3=16
lw=2
lab=['-b','-r','-k','-g','-m','-c']
lab2=['--b','--r','--k','--g','--m','--c']
chan=pltnl['chan']  # which chanel to be compared, like  phi_*, apar_*,bpar_*, multiple value is availabel, * is the poloidal mode number
#field=int(pltnl['field'])  # 0,1,2, only single value is permitted
dic1={'phi':0,'apar':1,'bpar':2}
nchan=len(chan)
case=outputs[casename]
for ic in range(nchan):
    case.getbigfield()
    field=dic1[chan[ic].split('_')[0]]
    kmode=chan[ic].split('_')[1]
    kmode=int(kmode)
    fk,ftk = case.kxky_select(0,field,'phi',0)
    pk=sum(fk[:,:,:],axis=0)/case.rho
    plot(case['t'],pk[kmode,:],lab[ic],linewidth=lw,label=chan[ic])
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    title(chan[ic],fontsize=fs1)
    xlabel('$time(a/c_s)$',fontsize=fs1,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
