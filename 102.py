import os
import shutil
#print(dir(os))
#os.getcwd("Desktop")
#os.mkdir("102")
path = "C102_assets-main"
print("before copying files:")
print(os.listdir(path))
source = "C102_assets-main/feather.jfif"
destination = "C102_assets-main/copyfeather.jfif"
shutil.copy(source,destination)
print("after copying file:")
print(os.listdir(path))