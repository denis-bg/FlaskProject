import os

def readfile():
    file=os.getcwd()+'/app/public/lttfiles/DEFAULT-LTT.LCF'
    with open(file, 'r') as f:
        list = [line.rstrip('\n') for line in f]

    premiere_ligne = list.pop(0)
    lttinfos = dict(kv.split('=') for kv in list)

    lttinfos['Unit'] = '3'
    return lttinfos
