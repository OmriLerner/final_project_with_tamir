import arduino
import time
import apriltag
import cv2


# board = pyfirmata.Arduino('COM6')
# it = pyfirmata.util.Iterator(board)
# it.start()

arduino.servo('COM6', 9, 0)

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        print('no frame')
        continue

    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)

    tag = apriltag.get_best_tag(frame)
    print(tag.center)
    if(tag != 'no tag'):
        frame = apriltag.draw_tag(frame, tag)
    # Visualise the results
    cv2.imshow('stream', frame)
    if cv2.waitKey(1) == ord('q'):break
