
import os
from sys import *
import urllib.request
import re
import webbrowser


def is_conected():
    try:
        urllib.request.urlopen('https://www.google.co.in/',timeout = 1)
        return True
        
    except exception as E:
        return False
   
def Find(url):
    match = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',url)
    #print(match)
    return match

def OpenUrl(path):
    if os.path.exists(path):
        file = open(path,'r')
        lines = file.readlines()
        for line in lines:
            url = Find(line)
            #print(url)
            for str in url:
                webbrowser.open_new_tab(str)
    else:
        print("Invalid path")
           

def main():
    print("-----Automation Script to open URL in the file-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) != 2):
        print("Insufficient Arguments")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to open URL in browser from file")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_Name File_Name")
        exit()
    
    try:
        conected = is_conected()
        
        if conected:
            OpenUrl(argv[1])
        else:
            print("Unable to connect with internet")
    except Exception as E:
        print("Error : ",E)


if __name__ == "__main__":
    main()