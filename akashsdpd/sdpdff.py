
# this script captures image with Pi Camera
# performs image recognition using AWS Rekognition Engine
# and then calls AWS Polly Speech Synthesis API to describe the items found in the image

# function to capture image with Pi Camera
def capture_image(image_file):
	import picamera
	camera = picamera.PiCamera()
	camera.vflip = True
	camera.capture(image_file)
	camera.close()

# calling text-to-speech api of aws polly
   
# image recognition code
# takes an image file as input and
# returns the list of items recognized in the image
def image_recognition(image_file):

	# import aws boto3 library
	import boto3
	items = []

	# list of labels to be ignored as stop-words
	# mostly generic words like fruit, vegetable, food etc.
	#stoplist = ['Fruit', 'Produce', 'Plant', 'Vegetable', 'Food']
        itemlist=['Coca' , 'Coca-Cola','oca-Cola' 'pepse', 'popsi']
	# calling aws rekognition api on image-file
	client = boto3.client('rekognition','us-west-2')
	with open(image_file, "rb") as image:
		# object recognition from the image
                result = client.detect_text(Image={'Bytes': image.read()})
                textDetections=result['TextDetections']
               # print result
   # print 'Matching faces'
                RES={'!'}
                print "display contents........"
                for text in textDetections:
                    if(text['DetectedText'][0]=='p'):           
                        #print text['DetectedText']
                        RES.add(text['DetectedText'])
		# processing json output to get image labels
		#for label in result['Labels']:
		#	#if label['Name'] not in stoplist:
		#	items.append(label['Name'])
                #print(RES)
                #print("your bill is: ")
                #bill=(len(RES)-1)*20
                #print(bill)
                print(RES)
	return len(RES)-1

# capture image and identify objects in the image
import cv2
camera = cv2.VideoCapture(0)
import RPi.GPIO as GPIO
#GPIO.cleanup()
from time import sleep
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setwarnings(False)
import qrtools
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
fb = firebase.FirebaseApplication('https://smartv1-a281d.firebaseio.com/', None)
image_file = "before.jpg"
image_file1="after.jpg"
#capture_image(image_file)
qr = qrtools.QR()
qrcdec=fb.get('/hi/email',None)
print "email fetched is : "+qrcdec
print "scan the qrcode ........"
raw_input('Press Enter to capture')
return_value, image = camera.read()
cv2.imwrite('qrcodeq.jpg', image)
qr.decode("qrcodeq.jpg")
if qr.data==qrcdec :#firedata is data retrieved from firebase
    #print "done"
    #GPIO.output(18,GPIO.HIGH)
    print " please wait while processing................"
    #camera = cv2.VideoCapture(0)
    #raw_input('Press Enter to capture')
    #return_value, image = camera.read()
    #cv2.imwrite('first.jpg', image)
    #del(camera)
    items = image_recognition(image_file)
    print(items)
    print "at your service................"
    #camera = cv2.VideoCapture(0)
    #raw_input('Press Enter to capture')
    #return_value, image = camera.read()
    #cv2.imwrite('second.jpg', image)
    #del(camera)
    items1= image_recognition(image_file1)
    print(items1)
    netitems=items-items1
    print(netitems)
    print("your bill is: ")
    bill=(netitems*20)
    print(bill)
    result=fb.put('hi','cost',bill)
    #print result
    print "cost updated is",bill," to murali firebase"
#GPIO.cleanup()
#camera.release()
del(camera)
cv2.destroyAllWindows()
    #print items
    #text = "I found following items in the vmac: " + ", ".join(items)
    #print text
# prepare text utterance for speech-synthesis

