# this script is used to load the nonlin data, by default, from cori
# to the output tree
server='xiang@cori.nersc.gov'
tunnel='jianx@cybele.gat.com:22'
pltnl=root['SETTINGS']['PLOTS']['NL']
npath=len(pltnl['path'].keys())
outputs=root['OUTPUTS']
# set the default server
sever='kuafu'
for k in range(npath):
    keyname=pltnl['path'].keys()[k]
#    outputs[keyname]=OMFITcgyro([pltnl['path'][keyname],server,tunnel],extra_files=['bin.cgyro.kxky_apar','bin.cgyro.kxky_bpar'])
    if sever=='cori':
        outputs[keyname]=OMFITcgyro([pltnl['path'][keyname],server,tunnel],extra_files=['bin.cgyro.kxky_apar','bin.cgyro.kxky_bpar','bin.cgyro.kxky_n'])
    else:
        outputs[keyname]=OMFITcgyro(pltnl['path'][keyname])
