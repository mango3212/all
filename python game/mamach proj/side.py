import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,max_num_hands=1,min_detection_confidence=0.5,min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

def is_clicked(p,t):
    if t >= p:
        return True
    else:
        return False

def get_finger_pos():
    run  = True
    while run:
        success, img = cap.read()
        img = cv2.flip(img,1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        
        if results.multi_hand_landmarks:
            pfinger = results.multi_hand_landmarks[0].landmark[8]
            tfinger = results.multi_hand_landmarks[0].landmark[4]
            tfingerX = tfinger.x
            pfingerX = pfinger.x
            pfingerY = pfinger.y
            return pfingerX,pfingerY, tfingerX
            




        cv2.waitKey(1)
