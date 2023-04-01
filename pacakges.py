import os
import shutil


print(os.getcwd())

total, used, free =shutil.disk_usage("/")
print(f"Total disk is: {total // (2**30)} GB")

print(f"free disk is: {free  // (2**30)}  GB")

print(f"used disk is: {used // (2**30)} GB ")

#fstring

