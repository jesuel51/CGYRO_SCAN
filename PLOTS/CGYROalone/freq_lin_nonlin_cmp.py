# this script is used to compare the frequency of linear and nonlinear run versus ky
# the linear frequency should be acted as input
nl=root['SETTINGS']['PLOTS']['nl']
freq_lin=nl['freq_lin']  # which should be array([3,nky]), the rows are ky, freq and gamma
# get the nonlinear freq
casename=nl['case_t_trace']
case=root['OUTPUTS'][casename]
t_ind=int((1-nl['t_ave'])*case['n_time'])
lw=2
fs1=24
fs2=20
fs3=16
# plot the ky spectrum of the omege and freq
ky_nl=sign(case['kyrhos'][1])*case['kyrhos']
plot(ky_nl,mean(case['freq']['omega'].T[t_ind:-1],0),'-ro',linewidth=lw,label='nonlin')
# data of linear calculation, 
#ky_lin=nl['freq_lin'][0]
#freq_lin=nl['freq_lin'][1]
#gamma_lin=nl['freq_lin'][2]
plot(freq_lin['ky'],freq_lin['omega'],'-ko',linewidth=lw,label='lin')
ylim([-12,0])
xticks(fontsize=fs2)
yticks(fontsize=fs2)
ylabel('$\omega$',fontsize=fs1)
legend(loc=0,fontsize=fs2).draggable(True)
xlabel('$k_y$',fontsize=fs1,family='serif')
ylabel('$\\omega$',fontsize=fs1,family='serif')

