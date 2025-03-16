import datetime
import winsound
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
db_info = os.getenv("DB_INFO")

mongo_client = pymongo.MongoClient(db_info)

db = mongo_client['alaram']
collection = db['schedules']

def Alarm():
    print("""
          1.set the schedules
          2.list of schedules
          3.total numbers of schedules
          4.Help guide
          """)
    a = input("Enter the Number: ")
    if a == "":
         print("Enter the Number!")
    if a == "2":
        documents = collection.find()
        for index,document in enumerate(documents):
            hour = document.get('hour', 'N/A')
            minutes = document.get('minutes', 'N/A')
            seconds = document.get('seconds', 'N/A')
            print(f"{index}. {hour} Hour, {minutes}Minute, {seconds}Second")
        mongo_client.close()

    if a == "3":
            total_documents = collection.count_documents({})
            print("Total number of Alaram Schedules:", total_documents)
            mongo_client.close()
            
    if a == "4":
        print("""
              Welcome to Simple Alarm System. Command line help

                    1 -> Set an alarm schedule. Schedules are stored in a data base.
                    2 -> List of schedules from data base.
                    3 -> Show the total number of schedules.
                    4 -> Help guide.
               
              Thanks for Reading.
               """)
            
    hour = input("Enter the hour(0,23): ")
    minutes = input("Enter the minutes(0,59): ")
    seconds = input("Enter the seconds(0,59): ")
    if a == "1":
        data = {"hour": hour, "minutes": minutes, "seconds": seconds}
        collection.insert_one(data)
        mongo_client.close()

        
    while True:
            time = datetime.datetime.now()
            timeformat = time.strftime("%H:%M:%S")
            if hour == "" or minutes =="" or seconds == "":
                print("Enter the time!")
                break
            if timeformat == f"{hour}:{minutes}:{seconds}":
                print(f"Alaram Time - {hour}:{minutes}:{seconds}")
                winsound.Beep(1000, 1000)
                choice = input("Enter 1 for continue | 0 for break:")
                if choice == "1":
                    Alarm()
                else:
                    break
                break
            print(timeformat)
Alarm()