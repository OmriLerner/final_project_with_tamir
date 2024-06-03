from pupil_apriltags import Detector
import cv2
detector = Detector(families="tag36h11")
tag_id = 1



def find_tags(frame):
    """
    Calculate the cumulative pointcloud from the multiple devices
    Parameters:
    -----------
    frames_devices : dict
    	The frames from the different devices
    	keys: str
    		Serial number of the device
    	values: [frame]
    		frame: rs.frame()
    			The frameset obtained over the active pipeline from the realsense device
    """
    
    tags = []
  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    results = detector.detect(gray) 
    
    for tag in results:
        if (tag.decision_margin>10):  
            tags.append(tag)

    return(tags)

def get_best_tag(frame):
    tags = find_tags(frame)
    highest_decision_margin = 0
    chosen_tag = 'no tag'
    
    if len(tags)<=0:
        return 'no tag'
    for tag in tags:
        if tag.tag_id == tag_id and tag.decision_margin>highest_decision_margin:
            highest_decision_margin = tag.decision_margin
            chosen_tag = tag
    return chosen_tag


def draw_tag(frame, tag):
    # getting pixel corners
    (ptA, ptB, ptC, ptD) = tag.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))

    # drawing boundnig box
    cv2.line(frame, ptA, ptB, (0, 255, 0), 1)
    cv2.line(frame, ptB, ptC, (0, 255, 0), 1)
    cv2.line(frame, ptC, ptD, (0, 255, 0), 1)
    cv2.line(frame, ptD, ptA, (0, 255, 0), 1)
    return frame