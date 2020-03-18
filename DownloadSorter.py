import os
import glob

while True:
    filenames = ['Compressed','Documents','Videos','Music','Applications', 'Photos']
    os.chdir("/home/ayaan/Downloads")
    def mvfiles(filename, foldername):
        os.system("mv \""+ filename +"\" "+ foldername)
        pass
    cfiles=glob.glob('*.wav')
    cfileslen = len(cfiles)
    if cfiles:
        x = -1
        cfl = cfileslen - 1
        while x < cfl:
            x += 1
            mvfiles(cfiles[x], filenames[3])
    cfiles=glob.glob('*.mp3')
    cfileslen = len(cfiles)
    if cfiles:
        x = -1
        cfl = cfileslen - 1
        while x < cfl:
            x += 1
            mvfiles(cfiles[x], filenames[3])
    cfiles=glob.glob('*.sh')
    cfileslen = len(cfiles)
    if cfiles:
        x = -1
        cfl = cfileslen - 1
        while x < cfl:
            x += 1
            mvfiles(cfiles[x], filenames[4])
    cfiles=glob.glob('*.zip')
    cfileslen = len(cfiles)
    if cfiles:
        x = -1
        cfl = cfileslen - 1
        while x < cfl:
            x += 1
            mvfiles(cfiles[x], filenames[0])
    crfiles=glob.glob('*.rar')
    crfileslen = len(crfiles)
    if crfiles:
        x = -1
        crfl = crfileslen - 1
        while x < crfl:
            x += 1
            mvfiles(crfiles[x], filenames[0])
    c7files=glob.glob('*.7z')
    c7fileslen = len(c7files)
    if c7files:
        x = -1
        c7fl = c7fileslen - 1
        while x < c7fl:
            x += 1
            mvfiles(c7files[x], filenames[0])
    dfiles=glob.glob('*.txt')
    dfileslen = len(dfiles)
    if dfiles:
        x = -1
        dfl = dfileslen - 1
        while x < dfl:
            x += 1
            mvfiles(dfiles[x], filenames[1])
    afiles=glob.glob('*.exe')
    afileslen = len(afiles)
    if afiles:
        x = -1
        afl = afileslen - 1
        while x < afl:
            x += 1
            mvfiles(afiles[x], filenames[4])
    apfiles=glob.glob('*.apk')
    apfileslen = len(apfiles)
    if apfiles:
        x = -1
        apfl = apfileslen - 1
        while x < apfl:
            x += 1
            mvfiles(apfiles[x], filenames[4])
    pfiles=glob.glob('*.jpeg')
    pfileslen = len(pfiles)
    if pfiles:
        x = -1
        pfl = pfileslen - 1
        while x < pfl:
            x += 1
            mvfiles(pfiles[x], filenames[5])
    p1files=glob.glob('*.png')
    p1fileslen = len(p1files)
    if p1files:
        x = -1
        p1fl = p1fileslen - 1
        while x < p1fl:
            x += 1
            mvfiles(p1files[x], filenames[5])
    p2files=glob.glob('*.jpg')
    p2fileslen = len(p2files)
    if p2files:
        x = -1
        p2fl = p2fileslen - 1
        while x < p2fl:
            x += 1
            mvfiles(p2files[x], filenames[5])
    vfiles=glob.glob('*.mp4')
    vfileslen = len(vfiles)
    if vfiles:
        x = -1
        vfl = vfileslen - 1
        while x < vfl:
            x += 1
            mvfiles(vfiles[x], filenames[2])
    v1files=glob.glob('*.mkv')
    v1fileslen = len(v1files)
    if v1files:
        x = -1
        v1fl = v1fileslen - 1
        while x < v1fl:
            x += 1
            mvfiles(v1files[x], filenames[2])