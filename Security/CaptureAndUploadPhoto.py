from os import name
from capture_and_uploadImage import take_snapshot
import cv2
import dropbox
import time
import random

startTime = time.time()

def snapshotting():
    number = random.randint(0,100)

    vedioCaptureObj = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vedioCaptureObj.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        startTime = time.time()
        result = False
    return img_name
    print("snapshot taken")
    vedioCaptureObj.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "LYxypD1pJMkAAAAAAAAAAcVRIUvAWhNSSzCvC_0m3uHZT2qwU9qFiDS_6bGZXrdN"
    file = img_name
    file_from = file
    file_to = "/AKM74339/Security/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - startTime) >= 5):
            name = take_snapshot()
            upload_file(name)

main()