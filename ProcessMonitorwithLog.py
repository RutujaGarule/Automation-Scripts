import psutil
import os
import time
from sys import*

def ProcessDisplay(log_dir):
    listprocess = []
   
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
          
    separator = "-" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024 *1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
            
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
            
    for element in listprocess:
        f.write("%s\n"%element)
    
def main():
    print("--------Python Automation Script-------")
    print("Process Monitor with Log")
    print("This script will accept directory name from user and create log file in that directory which contains information of all running processes")
    
    print("Application name :" +argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid Number of arguments")
        exit()
        
    if(argv[1] =="-h") or (argv[1] == "-H"):
        print("This script is used to log record of running processes")
        exit()
        
    if(argv[1] =="-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()
        
    try:
        ProcessDisplay(argv[1])
        
    except ValueError:
        print("Error : Invalid datatype of input")
        
    except Exception:
        print("Error :Invalid input")
        
if __name__ == "__main__":
    main()