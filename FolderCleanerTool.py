# Script to clean given folder and categorize files.
# All files not modified in last X days will be moved.
# All files will be stored under sub folders, grouped by file type.
# Folder names are extensions in upper case.

import os
import glob
import datetime as d
import time

extensions = []
now = d.datetime.now()
newFoldersCount = 0
x = 14

# Main folder path - change if needed
folderPath = f"C:\\Users\{os.getlogin()}\Downloads\*"

# get files from folder
files = glob.glob(folderPath) 
files = [f for f in files if os.path.isfile(f)] # get only files, no folders
files = [f for f in files if abs(now-d.datetime.fromtimestamp(os.path.getmtime(f))).days > x] # get files not modified in last X days only

filesToMoveCount = len(files)

# get all unique extensions
for file in files:
    ext = file.split(".")[-1].upper()
    if ext not in extensions:
        extensions.append(ext)

# create folders based on extensions
for each in extensions:
    newFolderPath = folderPath[:len(folderPath)-1:] + each
    try:
        os.mkdir(newFolderPath)
        newFoldersCount +=1
    except OSError as error:
        print(error)

# get all subfolders from folder
folders = glob.glob(folderPath)
folders = [f for f in folders if os.path.isfile(f) is False] # get only folders
existingFoldersCount = len(folders)

# move each file to particular folder
for file in files:
    ext = file.split(".")[-1].upper()
    for folder in folders:
        if ext in folder:
            filename = file.split("\\")[-1]
            os.replace(file,f"{folder}\\{filename}")

# execution time
end = d.datetime.now()
print(f"\nExecution time: {abs(now-end)}")

# done message
print(f"\n{filesToMoveCount} files moved across {existingFoldersCount} existing folders. \nNew folders created this run: {newFoldersCount}.\n")

time.sleep(5)
