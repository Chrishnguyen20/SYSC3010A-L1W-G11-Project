from pathlib import Path
import pyrebase
import RPi.GPIO as GPIO
#import time
#from datetime import datetime

# Firebase Config
api_key = "AIzaSyBWMHPeUjEqT_P6g_jrxlKC431pr2xkTaU"
project_id = "sysc3010-project"
database_url = "https://sysc3010-project-default-rtdb.firebaseio.com/"

config = {
"apiKey": api_key,
"authDomain": "{}.firebaseapp.com".format(project_id),
"databaseURL": database_url,
"storageBucket": "{}.appspot.com".format(project_id)
}

# Firebase Storage Setup
firebase = pyrebase.initialize_app(config)
sr = firebase.storage()

def send_video_to_firebase_storage():
    name = str(Path().resolve().parent) + "/recordings/video2.h264"
    sr.child("video_recordings").child("video2.h264").put(name)
    print(name, "sent to Firebase Storage")
    
if __name__ == "__main__":
    send_video_to_firebase_storage()