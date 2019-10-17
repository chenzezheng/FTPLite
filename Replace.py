import os

def ReplaceMD(filepath, remotepath):
    f = open(filepath, 'r', encoding='utf-8')
    f_bak = open(filepath + '.bak', 'w', encoding='utf-8')

    for line in f:
        if line[0] == '!' :
            if '\\' in line :
                period = line.split('\\', 1)
                line = period[0] + remotepath + period[1]
        f_bak.write(line)
    
    f.close()
    f_bak.close()

    f = open(filepath, 'w', encoding='utf-8')
    f_bak = open(filepath + '.bak', 'r', encoding='utf-8')

    for line in f_bak:
        f.write(line)

    f.close()
    f_bak.close()

    os.remove(filepath + '.bak')