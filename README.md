findzippedfiles
=======

This program will find files inside zip archives and inform the user in what archive that specific file is.

Requirements:

 - Python 3.6 (tested)

Usage:

 1. place in the directory where archives are located
 2. run findzippedfiles.py in command-line or Python IDLE environment

Changelog:

* 0.3 (2018/09/25): Error handling in findFile(), program will tell user when it can't access an archive without crashing
* 0.2 (2018/09/25): Don't run findFile() if the file list is empty
* 0.11 (2018/09/25): Restructuring of code and more readable format
* 0.1 (2018/09/24): Main logic
