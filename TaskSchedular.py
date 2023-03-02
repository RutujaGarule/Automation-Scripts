import schedule
import time
import datetime

def Fun_Minute():
    print("Current time is :")
    print(datetime.datetime.now())
    print("Schedular executes after Minute")
    
def Fun_Hour():
    print("Current time is :")
    print(datetime.datetime.now())
    print("Schedular executes after Hour")
    
def Fun_Day():
    print("Current time is :")
    print(datetime.datetime.now())
    print("Schedular executes after Day")
    
def Fun_Afternoon():
    print("Current time is :")
    print(datetime.datetime.now())
    print("Schedular executes at 12")
    
def main():
    print("---------Automation Script---------")
    print("Python Job Schedular")
    print(datetime.datetime.now())
    
    schedule.every(1).minutes.do(Fun_Minute)
    
    schedule.every().hour.do(Fun_Hour)
    
    schedule.every().day.at("00:00").do(Fun_Day)
    
    schedule.every().sunday.do(Fun_Day)
    
    schedule.every().saturday.at("18:30").do(Fun_Day)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
    
    