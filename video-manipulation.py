import cv2
import datetime

video = cv2.VideoCapture("assets/video.avi")

while True:
    ret, frame = video.read()

    if ret == False:
        break

    text = str(datetime.datetime.now())

    frame = cv2.putText(
        frame, text, (10, 20), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
