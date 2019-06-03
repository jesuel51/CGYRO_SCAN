# this script is used to collect the CGYRO result of 2D scan in a good format
mode=root['SETTINGS']['PHYSICS']['mode']
if mode=='lin':
    root['SCRIPTS']['subscan_lin_2d.py'].run()
    case_tag=root['SETTINGS']['PHYSICS']['case_tag']
    for item in root['Cases'][case_tag].keys():
        item_temp=item.split('~')
        if not  root['OUTPUTScan'].has_key(item_temp[0]):
            root['OUTPUTScan'][item_temp[0]]=OMFITtree()
        if not  root['OUTPUTScan'][item_temp[0]].has_key(item_temp[1]):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]]=OMFITtree()
        if not  root['OUTPUTScan'][item_temp[0]][item_temp[1]].has_key(item_temp[2]):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]]=OMFITtree()
        if not  root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]].has_key(item_temp[3]):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]][item_temp[3]]=OMFITtree()
        if not root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]][item_temp[3]].has_key('lin'):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]][item_temp[3]]['lin']=OMFITtree()
        root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]][item_temp[3]]['lin'][item_temp[5]]=OMFITtree()
        for files in root['Cases'][case_tag][item]:
            root['OUTPUTScan'][item_temp[0]][item_temp[1]][item_temp[2]][item_temp[3]]['lin'][item_temp[5]][files]=root['Cases'][case_tag][item][files] 
else:
    root['SCRIPTS']['subscan_nonlin.py'].run()
    case_tag=root['SETTINGS']['PHYSICS']['case_tag']
    for item in root['Cases'][case_tag].keys():
        item_temp=item.split('~')
        if not  root['OUTPUTScan'].has_key(item_temp[0]):
            root['OUTPUTScan'][item_temp[0]]=OMFITtree()
        if not  root['OUTPUTScan'][item_temp[0]].has_key(item_temp[1]):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]]=OMFITtree()
        if not root['OUTPUTScan'][item_temp[0]][item_temp[1]].has_key('nonlin'):
            root['OUTPUTScan'][item_temp[0]][item_temp[1]]['nonlin']=OMFITtree()
        for files in root['Cases'][case_tag][item].keys():
            root['OUTPUTScan'][item_temp[0]][item_temp[1]]['nonlin'][files]=root['Cases'][case_tag][item][files] 
    
