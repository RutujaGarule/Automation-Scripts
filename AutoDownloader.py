
from sys import *
import os
import requests
from urllib.parse import urlparse


def is_downloadable(url):
    h = requests.head(url,allow_redirects = True)
    header = h.headers
    content_type = header.get('content_type')
    
    if 'text' in content_type.lower():
        return False
    
    if 'html' in content_type.lower():
        return False
        
    return True
    
    
def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)
    

def Download(url):
    allowed = is_downloadable(url)

    if allowed:
        try:
            res = requests.get(url,allow_redirects = True)
            
            filename = get_filename_from_cd(url)
            fd = open(filename,'wb')
            
            for buffer in res.iter_content(1024):
                fd.write(buffer)
                
            fd.close()
            return True
        except Exception as E:
            return False
            
    else:
        return False
    


def main():
    print("-----Automation Script for downloading files-----")
    print("Application Name : ",argv[0])
    
    if(len(argv) == 2):
        
        if((argv[1] == "-h") or (argv[1] == "-H")):
            print("This script is used to download file")
            exit()
            
        if((argv[1] == "-u") or (argv[1] == "-U")):
            print("Usage : Application_Name")
            exit()
            
    
    url = 'https://unsplash.com/s/photos/mahadev'
    result = Download(url)
        
    if result:
        print("File successfully downloaded")
    else:
        print("Failed to download")
            
    
if __name__ == "__main__":
    main()