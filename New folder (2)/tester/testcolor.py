import time
import cv2
import numpy as np
import mss
import pyautogui

target_color_start = np.array([20, 100, 100])
target_color_end = np.array([30,255,255])
keepticket = (202, 67)
check_ticket = {"top": 55, "left": 200, "width": 10, "height": 10}
with mss.mss() as sct:
    while True:
        s = 0 
        r = 0
        for i in range(10):
            full_screen = np.array(sct.grab(check_ticket))
            hsv_full_screen = cv2.cvtColor(full_screen, cv2.COLOR_BGR2HSV)
            mask_full_screen = cv2.inRange(hsv_full_screen, target_color_start, target_color_end)
            r = r + 1 
            time.sleep(1)
            if np.any(mask_full_screen):
                s = s + 1
                
            cv2.imshow('ticket', mask_full_screen)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            
        if s >= 10 :
                print("ครบ")
                pyautogui.click(keepticket)
                time.sleep(2)
                pyautogui.click(keepticket)            
        print("ตรวจ"+str(r)+"รอบ")
        print("เจอ"+str(s)+"รอบ")