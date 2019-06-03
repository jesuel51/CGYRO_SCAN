# this script is used to plot the frequency over the time of the ky and parameter that you specified
# the name, value and ky should be specified
plots=root['SETTINGS']['PLOTS']
#if plots['iflwphy']==1:
#    plots['paraval_eigen']=root['SETTINGS']['PHYSICS']['Range'][0]
effnum=plots['effnum']
#para=plots['Para']
#paraval_eigen=plots['paraval_eigen']
#ky_eigen=plots['ky_eigen']
#datanode=root['OUTPUTScan'][para][str(paraval_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
Para_x=plots['2d']['Para_x']
Para_y=plots['2d']['Para_y']
para_x_eigen=plots['2d']['para_x_eigen']
para_y_eigen=plots['2d']['para_y_eigen']
ky_eigen=plots['ky_eigen']
if root['SETTINGS']['PLOTS']['idimplt']==0:
    datanode=root['OUTPUTScan'][Para_x][str(para_x_eigen)[0:effnum]][Para_y][str(para_y_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
else:
    datanode=root['OUTPUTScan'][Para_x][str(para_y_eigen)[0:effnum]][Para_y][str(para_x_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
# what we do is to use the cgyro_plot to plot the eigenfunction
#deploypath='/home/jianx/temp/'
# define a function to read the out.cgyro.freq
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
    w=zeros([len(fread),1])
    gamma=zeros([len(fread),1])
    for k in range(len(fread)):
        w_temp=[float(item) for item in fread[k].split()]
        w[k]=w_temp[0]
        gamma[k]=w_temp[1]
    return w,gamma
    f.close()
ipltmthd=1
fs1=24
fs2=20
fs3=16
lw = 2
if ipltmthd == 0:
# use the system plot
    deploypath=root['SETTINGS']['REMOTE_SETUP']['workDir']
    datanode.deploy(deploypath)
    cmd='cd '+deploypath+' ;'
    cmd=cmd + 'module purge;'
    cmd=cmd + 'module load omfit/unstable;'
    cmd=cmd+'cgyro_plot -plot freq'
    os.system(cmd)
else:
# plot myself
    w,gamma=readfile(datanode['out.cgyro.freq'].filename)
    dt=datanode['input.cgyro']['DELTA_T']*datanode['input.cgyro']['PRINT_STEP']
    figure(figsize=[12,8])
    subplot(1,2,1)
    plot(linspace(dt,dt*len(w),len(w)),w,'-b',linewidth=lw)
    xlabel('t(a/cs)',fontsize=fs1,family='serif')
    ylabel('$\omega$(cs/a)',fontsize=fs1,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    subplot(1,2,2)
    plot(linspace(dt,dt*len(w),len(w)),gamma,'-b',linewidth=lw)
    xlabel('t(a/cs)',fontsize=fs1,family='serif')
    ylabel('$\gamma$(cs/a)',fontsize=fs1,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')

