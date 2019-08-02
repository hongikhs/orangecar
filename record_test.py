import datetime
import cv2

c = cv2.VideoCapture(0)
c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
fourcc = cv2.VideoWriter_fourcc(*'h264')
record = False

while True:
    #if(c.get(cv2.CAP_PROP_POS_FRAMES) == c.get(cv2.CAP_PROP_FRAME_COUNT)):
    #    c.open("/Image/Star.mp4")

    ret, frame = c.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == ord('q'):
        break
    elif key == ord('c'):
        print("capture")
        cv2.imwrite("./" + str(now) + ".png", frame)
    elif key == ord('r'):
        print("record")
        record = True
        video = cv2.VideoWriter("./" + str(now) + ".mp4", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == ord('s'):
        print("stop")
        record = False
        video.release()
        
    if record == True:
        print("recording..")
        video.write(frame)

c.release()
cv2.destroyAllWindows()
