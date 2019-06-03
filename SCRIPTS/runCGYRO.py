# this is used to run the linear GYRO
##===================================
### input
##==================================
inputs=[(root['INPUTS']['input.cgyro'],'input.cgyro'),
        (root['INPUTS']['input.profiles'],'input.profiles'),
        (root['INPUTS']['input.profiles.geo'],'input.profiles.geo')
       ]

inputcgyro=root['INPUTS']['input.cgyro']
##----------------------
### output
##----------------------
outputs=['out.cgyro.freq','out.cgyro.info', \
         'out.cgyro.phi','out.cgyro.phib',  \
         'out.cgyro.apar','out.cgyro.aparb',\
         'out.cgyro.bpar','out.cgyro.bparb']
executable=root['SETTINGS']['SETUP']['executable']
ncore=int(executable.split()[-1])  # cores needed
jn=int(ceil(ncore/24.))              # get the number of nodes
if ncore<24:
    cn=ncore
else:
    cn=24
executable ='pbsMonitor -jn '+str(jn)+' -cn '+str(cn)+' -exe  '+executable
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
for item in outputs:
    root['OUTPUTS'][item]=OMFITasciitable(item)
