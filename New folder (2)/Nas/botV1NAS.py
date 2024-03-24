import cv2
import numpy as np
import mss
import tkinter as tk
import socket
import datetime
import time
import pyautogui

def find_and_display_image(template_image, monitor_region):
    ip_address = socket.gethostbyname(socket.gethostname())
    current_date = datetime.datetime.now()
    expiration_date = datetime.datetime(2025, 2, 14)
    if current_date > expiration_date:
        print("โปรแกรมหมดอายุการใช้งาน")
        return
    authorized_ips = ['26.183.0.195']
    if ip_address not in authorized_ips:
        print("โปรแกรมนี้ไม่ได้รับอนุญาตให้ทำงานบนเครื่องนี้")
        return
    if template_image is None:
        raise ValueError("Template image not found or cannot be opened.")
    template_height, template_width = template_image.shape[:2]

    click_position_title = (479, 345) 
    click_position_google = (476, 215) 
    click_position_email = (893, 1000)
    click_position_closegoogle = (1779, 21) 
    click_position_taptoplay = (482, 341)
    click_position_selectCT = (813, 180)
    click_position_start = (836, 488)
    click_position_closeEvent = (841, 82)
    click_position_Auto = (928, 382)
    click_position_keepticket = (199, 66)

    target_color_start, target_color_end = np.array([28,120,85]), np.array([30, 255, 255])
    target_color_white_start, target_color_white_end = np.array([0, 0, 180]), np.array([180, 25, 255])
    with mss.mss() as sct:
        monitor_region = sct.monitors[1]  # Use the primary monitor
        monitor_region = {'top': 0, 'left':0, 'width': 958, 'height': 510}
        monitor = {"top": 51, "left": 190, "width": 15, "height": 15}
        monitors = {"top": 366, "left": 915, "width": 30, "height": 13}
        while True:
              

            screen_captures = np.array(sct.grab(monitor_region))
            screen_capture = cv2.cvtColor(screen_captures, cv2.COLOR_BGRA2RGB)
            res = cv2.matchTemplate(screen_capture, template_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            threshold = 0.8
            if max_val >= threshold:
                pyautogui.click(click_position_title)
                print(f"Clicked at position {click_position_title}")
                time.sleep(5)
                pyautogui.click(click_position_google)
                print(f"Clicked at position {click_position_google}")
                time.sleep(5)
                pyautogui.click(click_position_email)
                print(f"Clicked at position {click_position_email}")
                time.sleep(5)
                pyautogui.click(click_position_closegoogle)
                print(f"Clicked at position {click_position_closegoogle}")
                time.sleep(5)
                pyautogui.click(click_position_taptoplay)
                print(f"Clicked at position {click_position_taptoplay}")
                time.sleep(5)
                pyautogui.click(click_position_selectCT)
                print(f"Clicked at position {click_position_selectCT}")
                time.sleep(5)
                pyautogui.click(click_position_start)
                print(f"Clicked at position {click_position_start}")
                time.sleep(15)
                pyautogui.click(click_position_closeEvent)
                print(f"Clicked at position {click_position_closeEvent}")
                time.sleep(2)
                top_left = max_loc
                bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
                cv2.rectangle(screen_capture, top_left, bottom_right, (0, 255, 0), 2)
                
                x = 0
                for i in range(30):
                    full_screens = np.array(sct.grab(monitors))
                    hsv_full_screens = cv2.cvtColor(full_screens, cv2.COLOR_BGR2HSV)
                    mask_full_screens = cv2.inRange(hsv_full_screens, target_color_white_start, target_color_white_end)
                    if np.any(mask_full_screens):
                        print("ออโต้อยู่แล้ว")
                        x = x + 1
                        break

                if x == 0:
                    pyautogui.click(click_position_Auto)
                    print(f"Clicked at position {click_position_Auto}")
                

            else:
                
                        print("Loading")
                        full_screen = np.array(sct.grab(monitor))
                        hsv_full_screen = cv2.cvtColor(full_screen, cv2.COLOR_BGR2HSV)
                        mask_full_screen = cv2.inRange(hsv_full_screen, target_color_start, target_color_end)
                        cv2.imshow('Mask', mask_full_screen)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if np.any(mask_full_screen):
                            print("ครบแล้ว")
                            pyautogui.click(click_position_keepticket)
                            print(f"Clicked at position {click_position_keepticket}")
                
                             

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

def start_program():
    template_image_path = 'sns.png'
    template_image = cv2.imread(template_image_path, cv2.IMREAD_COLOR)
    if template_image is None:
        print(f"Image not found with the path: {template_image_path}")
        return
    template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2RGB)
    monitor_region = {}
    find_and_display_image(template_image, monitor_region)
def stop_program(root):
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Finder")

    start_button = tk.Button(root, text="Start", command=start_program)
    start_button.pack()

    stop_button = tk.Button(root, text="Stop", command=lambda: stop_program(root))
    stop_button.pack()

    root.mainloop()