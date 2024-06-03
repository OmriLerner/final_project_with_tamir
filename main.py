import arduino
import time
import apriltag
import cv2
import camera_utils

# board = pyfirmata.Arduino('COM6')
# it = pyfirmata.util.Iterator(board)
# it.start()
vertical_angle = 10
Horizontal_angle = 0

vertical_servo = arduino.servo(9, vertical_angle)
Horizontal_servo = arduino.servo(10, Horizontal_angle)
time.sleep(3)
# Horizontal_servo.rotate(int(20))


cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        print('no frame')
        continue
    
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # frame = cv2.flip(frame, 0)
    # frame = cv2.flip(frame, 1)

    tag = apriltag.get_best_tag(frame)
    # time.sleep(5)
    # time.sleep(5)
    print(tag.center)
    if(tag != 'no tag'):
        frame = apriltag.draw_tag(frame, tag)

        
        vertical_angle = vertical_servo.read_servo() + camera_utils.get_angle(tag.center, move_factor=0.1)[1]
        Horizontal_angle = Horizontal_servo.read_servo() + camera_utils.get_angle(tag.center, move_factor=-0.04)[0]

        print('read: ' + str(vertical_servo.read_servo()))
        print(frame.shape)
        # motor.clockwise()
        # time.sleep(5)
        # motor.counterclockwise()
        # time.sleep(5)
        try:
            vertical_servo.rotate(vertical_angle)
        except Exception:
            print('too high')
        try:
            print(Horizontal_angle)
            Horizontal_servo.rotate(int(Horizontal_angle))
        except Exception as e:
            print(e)
            print('too high')
        # time.sleep(0.05)
    # Visualise the results
    cv2.imshow('stream', frame)
    if cv2.waitKey(1) == ord('q'):break
