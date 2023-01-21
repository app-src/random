import pyrebase
import cv2
import imutils
config = {
  'apiKey': "AIzaSyAuQi_iaTmUayHlLifjiWaq7soIUPBMe8c",
  'authDomain': "livpol-bc457.firebaseapp.com",
  'databaseURL': "https://livpol-bc457-default-rtdb.firebaseio.com",
  'projectId': "livpol-bc457",
  'storageBucket': "livpol-bc457.appspot.com",
  'messagingSenderId': "972140073745",
  'appId': "1:972140073745:web:444869ba96d9d08aa832b0"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# data = {"Name":"ASHIsh"}
# db.child("users").push(data)


# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

# while(True):
#     # reading the frame
#     ret, frame = cap.read()
#     # displaying the frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         # breaking the loop if the user types q
#         # note that the video window must be highlighted!
#         break

# cap.release()
cv2.destroyAllWindows()
# the following is necessary on the mac,
# maybe not on other platforms:
cv2.waitKey(1)

while cap.isOpened():
	# Reading the video stream
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image,
							width=min(400, image.shape[1]))

		# Detecting all the regions
		# in the Image that has a
		# pedestrians inside it
		(regions, _) = hog.detectMultiScale(image,
											winStride=(4, 4),
											padding=(4, 4),
											scale=1.05)

		# Drawing the regions in the
		i=0
		for (x, y, w, h) in regions:
			i += 1            
			cv2.rectangle(image, (x, y),
						(x + w, y + h),
						(0, 0, 255), 2)

# 		print(i)
		cv2.imshow("Image", image)
# 		text = "TutorialsPoint"
		org = (50,50)
		font = cv2.FONT_HERSHEY_SIMPLEX
		fontScale = 1
		color = (255, 0, 0)
		thickness = 2
		image = cv2.putText(image, " "+str(i), org, font, 
				fontScale, color, thickness, cv2.LINE_AA)
		data = {"Name":str(i)}
		db.child("people").set(data)        
		cv2.imshow("Image", image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()
