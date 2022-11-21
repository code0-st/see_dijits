import os

dir_name = 'data/training/0'

filenames = os.scandir(dir_name)

for filename in filenames:
    new_filename = filename.path.split('.')[0][0:-2] + '.' + filename.path.split('.')[1]
    os.rename(filename.path, new_filename)
