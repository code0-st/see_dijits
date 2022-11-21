import os

label = 8
dir_name = 'data_drawn\\' + str(label)

filenames = os.scandir(dir_name)

for filename in filenames:
    new_filename = filename.path.split('.')[0] + '_' + str(label) + '.' + filename.path.split('.')[1]
    os.rename(filename.path, new_filename)

count = 0
new_filenames = os.scandir(dir_name)
for filename in new_filenames:
    if (filename.path.count("_" + str(label)) > 1):
        count += 1
        new_filename = filename.path.split('.')[0][0:-2] + '.' + filename.path.split('.')[1]
        print(filename.path + " " + new_filename)
        os.rename(filename.path, new_filename)

print("Errors: " + str(count))