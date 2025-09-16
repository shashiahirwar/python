import shutil

total, used, free = shutil.disk_usage("/")
if free / total < 0.3:
    print("Disk space low!")
else:
    print("enough memeory available")
