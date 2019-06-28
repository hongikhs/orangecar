import cv2

c = cv2.VideoCapture(0)
c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    _,full_image = c.read()
        
    cv2.imshow('frame',full_image)
    
    k = cv2.waitKey(5)
    if k == ord('q'):  #'q' key to stop program
        break
    if k > 0:
	      print(k)
