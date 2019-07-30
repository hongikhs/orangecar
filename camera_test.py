import cv2

c = cv2.VideoCapture(0)
c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = c.read()
        
    cv2.imshow('camera', frame)
    
    k = cv2.waitKey(5)
    
    if k == ord('q'):
        break
    if k > 0:
        print(k)
