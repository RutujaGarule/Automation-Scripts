
import os
from sys import *


def Directory_Watcher(Dir_Name):
    print("Inside directory watcher method")
    print("name of input directory : ",Dir_Name)
    
    for foldername,subfolder,Filenams in os.walk(Dir_Name):
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf )
        for fnames in Filenams:
            print("File inside folder "+foldername+" is "+fnames+ "having size ",os.path.getsize(fnames))
        print(" ")

def main():
    print("Directory Watcher Application")
    
    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()
    
    
    if(argv[1] == "-h"):
        print("This script will travel the directory and display name of all the entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_Name")
        exit()
        
    Directory_Watcher(argv[1])


if __name__ == "__main__":
    main()