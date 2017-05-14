from picamera import PiCamera

camera = PiCamera()
camera.capture('/home/pi/Desktop/window.jpg')

from google.cloud import storage #is this pre-build in the pi already? after you get-apt and configure the pi, CS

client = storage.Client() #where does Client come from?, CS

bucket = client.get_bucket('smartwindow-91b1c.appspot.com'), 

imageBlob = bucket.get_blob('window.jpg') 
imageBlob.upload_from_filename(filename='/home/pi/Desktop/window.jpg')
