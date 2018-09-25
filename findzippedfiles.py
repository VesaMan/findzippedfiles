#!/usr/bin/env python
"""
findzippedfiles.py, by Vesa Mäntysaari - 2018/09/25
This program will find files inside zip archives and inform the user in what archive that specific file is.
"""
import os
import glob
import zipfile

def findFile(list):
    for file in list:
        try:    # error handling for zip file operations
            with zipfile.ZipFile(file) as archive:
                for filename in archive.namelist(): # go through list of files inside archive
                    if not os.path.isdir(filename): # if filename is not a directory then continue
                        if ".mp4" in filename:  # if filename has specific string in it -> print archive and the filename
                            print (file+" -> "+filename)
        except IOError as e:    # push IOError message to variable 'e' and then print it
                print (e)

def main(v):
    print (v)
    files = glob.glob("*.zip")
    if not files: #if list is empty
        print("Current directory doesn't contain any files with the specified extension\nStopping findzippedfiles")
    if files: #if list has data
        findFile(files)

if __name__ == "__main__":
    version = "findzippedfiles v. 0.3\n-----------------------\n"
    main(version)
