# this script is used to call the cgyro_plot to plot the quansities that you wish to see
# the name, value and ky should be specified
plots=root['SETTINGS']['PLOTS']
if plots['iflwphy']==1:
    plots['paraval_eigen']=root['SETTINGS']['PHYSICS']['Range'][0]
effnum=plots['effnum']
para=plots['Para']
paraval_eigen=plots['paraval_eigen']
ky_eigen=plots['ky_eigen']
datanode=root['OUTPUTScan'][para][str(paraval_eigen)[0:effnum]]['lin'][str(ky_eigen)[0:effnum]]
# what we do is to use the cgyro_plot to plot the eigenfunction
deploypath='/home/jianx/temp/'
datanode.deploy(deploypath)
cmd='cd '+deploypath+' ;'
cmd=cmd + 'module purge;'
cmd=cmd + 'module load omfit/unstable;'
cmdcore=plots['cmd']
cmd=cmd + cmdcore
os.system(cmd)
