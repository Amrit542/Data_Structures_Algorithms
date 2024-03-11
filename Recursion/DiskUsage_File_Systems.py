import os

def disk_usage(path):
    total = os.path.getsize(path)  # immediate size of single file or folder
    if os.path.isdir(path):
        for singleFileName in os.listdir(path):
            childPath = os.path.join(path, singleFileName)
            total += disk_usage(childPath)

    print('{0:<7}'.format(total), path)
    return total


currentdir = os.getcwd()

print(currentdir)
size_of_currentdir =  disk_usage(currentdir)
print(size_of_currentdir)

