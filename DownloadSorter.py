import glob
import os

path = '/home/ayaan/Downloads/' # The Path To Your Downloads Here

os.path.join(path)

def mvfiles(filename, foldername):
    os.system('mv "' + filename + '" ' + foldername)


def move_files(extension, type):
    files = glob.glob(path + extension)
    print(files)
    for row in files:
        mvfiles(row, path + type)


Extensions = [['*.wav', 'Music'], ['*.mp3', 'Music'], ['*.sh', 'Applications'], ['*.zip', 'Compressed'],
              ['*.rar', 'Compressed'], ['*.7z', 'Compressed'], ['*.txt', 'Documents'], ['*.apk', 'Applications'],
              ['*.exe', 'Applications'], ['*.jpeg', 'Photos'], ['*.jpg', 'Photos'], ['*.png', 'Photos'],
              ['*.mp4', 'Videos'], ['*.mkv', 'Videos'], ['*.3gp','Videos']]

while True:
    for row in Extensions:
        move_files(row[0],row[1])
