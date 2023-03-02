# Accept text file and display valid mobile numbers from that file


from sys import *
import re 
import os


def CheckNum(line):
    #print(line)
    match = re.match('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',line)
    #print(match)
    return match
    
    
def ValidNumber(path):
    list = []
    
    if os.path.exists(path):
    
        with open(path,'r') as file:
            line = file.readlines()
            for i in line:
                #print(i)
                Num = CheckNum(i)
                print(Num)
                if(Num == True):
                    print(Num)
                    list.append(Num)
            return list
    else:
        print("Invalid path")
        

def main():
    print("-----Automation Script to display valid mobile numbers from file-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) != 2):
        print("Invalid Arguments")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to display valid mobile numbers")
        exit()
        
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_Name File_Name")
        exit()
        
    
    Arr = ValidNumber(argv[1])
    print(Arr)


if __name__ == "__main__":
    main()