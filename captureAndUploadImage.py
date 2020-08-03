import cv2
import dropbox
import time 
import random
start_time=time.time()
def takeSnapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snap shot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadImage(img_name):
  access_token='VpRF50lN7rAAAAAAAAAAIlfzA2AiNaZJvIvYJyiWM_ltLBVcfB2Io78RylXH12-4'
  file=img_counter
  file_from=file
  file_to='/newFolderTo/'+(img_name)
  dbx=dropbox.Dropbox(access_token)
  with open (file_from,'rb') as f:
      dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
      print("file_uploaded")
def main():
    while(True):
        if((time.time()-start_time) >= 3):
            name=takeSnapShot()
            upload_file(name)
main()                                 