import cv2
import numpy as np
import mss
import tkinter as tk
import socket
import datetime
import time
import pyautogui
from tkinter import filedialog
from pynput.mouse import Listener


def find_and_display_image(template_image, monitor_region,title,google,email,closegoogle,taptoplay,selectCT,start,closeEvent,Auto,keepticket,monitor_region_t,monitor_region_l,monitor_region_w,monitor_region_h,check_Auto_t,check_Auto_l,check_Auto_w,check_Auto_h,check_ticket_t,check_ticket_l,check_ticket_w,check_ticket_h,):
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
    

    target_color_start, target_color_end = np.array([20, 100, 100]), np.array([30,255,255])
    target_color_white_start, target_color_white_end = np.array([0, 0, 180]), np.array([180, 25, 255])
    with mss.mss() as sct:
        monitor_region = sct.monitors[1]  # Use the primary monitor
        monitor_region = {'top':monitor_region_t, 'left':monitor_region_l, 'width': monitor_region_w, 'height': monitor_region_h}
        check_ticket = {"top": check_ticket_t, "left": check_ticket_l, "width": check_ticket_w, "height": check_ticket_h}
        check_Auto = {"top": check_Auto_t, "left": check_Auto_l, "width": check_Auto_w, "height": check_Auto_h}
        while True:
            
            screen_capturess = np.array(sct.grab(monitor_region))
            screen_capture = cv2.cvtColor(screen_capturess, cv2.COLOR_BGRA2RGB)
            res = cv2.matchTemplate(screen_capture, template_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            threshold = 0.8
            if max_val >= threshold:
                time.sleep(300)
                pyautogui.click(title)
                print(f"Clicked at position {title}")
                time.sleep(5)
                pyautogui.click(google)
                print(f"Clicked at position {google}")
                time.sleep(5)
                pyautogui.click(email)
                print(f"Clicked at position {email}")
                time.sleep(5)
                pyautogui.click(closegoogle)
                print(f"Clicked at position {closegoogle}")
                time.sleep(5)
                pyautogui.click(taptoplay)
                print(f"Clicked at position {taptoplay}")
                time.sleep(5)
                pyautogui.click(selectCT)
                print(f"Clicked at position {selectCT}")
                time.sleep(5)
                pyautogui.click(start)
                print(f"Clicked at position {start}")
                time.sleep(15)
                pyautogui.click(closeEvent)
                print(f"Clicked at position {closeEvent}")
                time.sleep(2)
                top_left = max_loc
                bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
                cv2.rectangle(screen_capture, top_left, bottom_right, (0, 255, 0), 2)
                
                x = 0
                for i in range(30):
                    full_screens = np.array(sct.grab(check_Auto))
                    hsv_full_screens = cv2.cvtColor(full_screens, cv2.COLOR_BGR2HSV)
                    mask_full_screens = cv2.inRange(hsv_full_screens, target_color_white_start, target_color_white_end)
                    if np.any(mask_full_screens):
                        print("ออโต้อยู่แล้ว")
                        x = x + 1
                        break

                if x == 0:
                    pyautogui.click(Auto)
                    print(f"Clicked at position {Auto}")
                   
            

            else:
               
                s = 0 
                r = 0
            for i in range(10):    
                full_screens = np.array(sct.grab(check_Auto))
                full_screen = np.array(sct.grab(check_ticket))
                hsv_full_screen = cv2.cvtColor(full_screen, cv2.COLOR_BGR2HSV)
                mask_full_screen = cv2.inRange(hsv_full_screen, target_color_start, target_color_end)
                r = r + 1   
                cv2.imshow('Auto', full_screens)
                cv2.imshow('ticket', mask_full_screen)
                cv2.imshow('check_error', screen_capturess)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break 
                time.sleep(1)    
                if np.any(mask_full_screen):
                    s = s + 1
            if s >= 10 :
                print("ครบ")
                pyautogui.click(keepticket)
                time.sleep(2)
                pyautogui.click(keepticket)
                    
                
                               
            print("ตรวจ"+str(r)+"รอบ")
            print("เจอ"+str(s)+"รอบ")                        


def start_mouse_listener():
    listener = Listener(on_move=on_move)
    listener.start()
    
def on_move(x, y):
    position_label.config(text=f"Position: {x}, {y}")


def start_program():
    template_image_path = 'sns.png'
    template_image = cv2.imread(template_image_path, cv2.IMREAD_COLOR)
    if template_image is None:
        print(f"Image not found with the path: {template_image_path}")
        return
    template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2RGB)
    monitor_region = {}
    title = (int(title_x.get()), int(title_y.get()))
    google = (int(google_x.get()), int(google_y.get()))
    email = (int(email_x.get()), int(email_y.get()))
    closegoogle = (int(closegoogle_x.get()), int(closegoogle_y.get())) 
    taptoplay= (int(taptoplay_x.get()), int(taptoplay_y.get()))
    selectCT = (int(selectCT_x.get()), int(selectCT_y.get()))
    start = (int(start_x.get()), int(start_y.get()))
    closeEvent = (int(closeEvent_x.get()), int(closeEvent_y.get()))
    Auto = (int(Auto_x.get()), int(Auto_y.get()))
    keepticket = (int(keepticket_x.get()), int(keepticket_y.get()))
    monitor_region_t= int(monitor_region_top.get())
    monitor_region_l= int(monitor_region_left.get())
    monitor_region_w= int(monitor_region_width.get())
    monitor_region_h= int(monitor_region_hight.get())
    check_Auto_t = int(check_Auto_top.get())
    check_Auto_l = int(check_Auto_left.get())
    check_Auto_w = int(check_Auto_width.get())
    check_Auto_h = int(check_Auto_hight.get())
    check_ticket_t = int(check_ticket_top.get())
    check_ticket_l = int(check_ticket_left.get())
    check_ticket_w = int(check_ticket_width.get())
    check_ticket_h = int(check_ticket_hight.get())


    

    find_and_display_image(template_image, monitor_region,title,google,email,closegoogle,taptoplay,selectCT,start,closeEvent,Auto,keepticket,monitor_region_t,monitor_region_l,monitor_region_w,monitor_region_h,check_Auto_t,check_Auto_l,check_Auto_w,check_Auto_h,check_ticket_t,check_ticket_l,check_ticket_w,check_ticket_h,)
    
def stop_program(root):
    root.destroy()
def on_save_button_click():
    data_to_save = f"{title_x.get()} {title_y.get()} {google_x.get()} {google_y.get()} {email_x.get()} {email_y.get()} {closegoogle_x.get()} {closegoogle_y.get()} {taptoplay_x.get()} {taptoplay_y.get()} {selectCT_x.get()} {selectCT_y.get()} {start_x.get()} {start_y.get()} {closeEvent_x.get()} {closeEvent_y.get()} {Auto_x.get()} {Auto_y.get()} {keepticket_x.get()} {keepticket_y.get()} {monitor_region_top.get()} {monitor_region_left.get()} {monitor_region_width.get()} {monitor_region_hight.get() } {check_Auto_top.get()} {check_Auto_left.get()} {check_Auto_width.get()} {check_Auto_hight.get()} {check_ticket_top.get()} {check_ticket_left.get()} {check_ticket_width.get()} {check_ticket_hight.get()}"
    save_data(data_to_save)

def save_data(data_to_save):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(data_to_save)
        print(f"Data saved to {file_path}")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
        print(f"Data loaded from {file_path}")
        data_parts = data.split()
        if len(data_parts) >= 20: 
            title_x.insert(0, data_parts[0])
            title_y.insert(0, data_parts[1])
            google_x.insert(0, data_parts[2])
            google_y.insert(0, data_parts[3])
            email_x.insert(0, data_parts[4])
            email_y.insert(0, data_parts[5])
            closegoogle_x.insert(0, data_parts[6])
            closegoogle_y.insert(0, data_parts[7])
            taptoplay_x.insert(0, data_parts[8])
            taptoplay_y.insert(0, data_parts[9])
            selectCT_x.insert(0, data_parts[10])
            selectCT_y.insert(0, data_parts[11])
            start_x.insert(0, data_parts[12])
            start_y.insert(0, data_parts[13])
            closeEvent_x.insert(0, data_parts[14])
            closeEvent_y.insert(0, data_parts[15])
            Auto_x.insert(0, data_parts[16])
            Auto_y.insert(0, data_parts[17])
            keepticket_x.insert(0, data_parts[18])
            keepticket_y.insert(0, data_parts[19])
            monitor_region_left.insert(0, data_parts[20])
            monitor_region_top.insert(0, data_parts[21])
            monitor_region_width.insert(0, data_parts[22])
            monitor_region_hight.insert(0, data_parts[23])
            check_Auto_top.insert(0, data_parts[24])
            check_Auto_left.insert(0, data_parts[25])
            check_Auto_width.insert(0, data_parts[26])
            check_Auto_hight.insert(0, data_parts[27])
            check_ticket_top.insert(0, data_parts[28])
            check_ticket_left.insert(0, data_parts[29])
            check_ticket_width.insert(0, data_parts[30])
            check_ticket_hight.insert(0, data_parts[31])
        else:
            print("Invalid data format")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x800")
    root.title("Image Finder")

    start_button = tk.Button(root, text="Start", command=start_program)
    start_button.grid(row=1, column=0)

    stop_button = tk.Button(root, text="Stop", command=lambda: stop_program(root))
    stop_button.grid(row=2, column=0)

    save_button = tk.Button(root, text="Save", command=on_save_button_click)
    save_button.grid(row=1, column=1)

    open_file_button = tk.Button(root, text="Open File", command=open_file)
    open_file_button.grid(row=2, column=1)

    start_button = tk.Button(root, text="Check position", command=start_mouse_listener)
    start_button.grid(row=1, column=2)

    position_label = tk.Label(root, text="Position: None")
    position_label.grid(row=1, column=3)

    title_label = tk.Label(root, text="Title Position:")
    title_label.grid(row=3, column= 0, )
    title_x = tk.Entry(root, width=10)
    title_x.grid(row=4, column=0)
    title_y = tk.Entry(root, width=10)
    title_y.grid(row=4, column=1)

    title_label = tk.Label(root, text="Google Position:")
    title_label.grid(row=5, column= 0, )
    google_x = tk.Entry(root, width=10)
    google_x.grid(row=6, column=0)
    google_y = tk.Entry(root, width=10)
    google_y.grid(row=6, column=1)

    title_label = tk.Label(root, text="Email Position:")
    title_label.grid(row=7, column= 0, )
    email_x = tk.Entry(root, width=10)
    email_x.grid(row=8, column=0)
    email_y = tk.Entry(root, width=10)
    email_y.grid(row=8, column=1)

    title_label = tk.Label(root, text="Closegoogle Position:")
    title_label.grid(row=9, column= 0, )
    closegoogle_x = tk.Entry(root, width=10)
    closegoogle_x.grid(row=10, column=0)
    closegoogle_y = tk.Entry(root, width=10)
    closegoogle_y.grid(row=10, column=1)

    title_label = tk.Label(root, text="Taptoplay Position:")
    title_label.grid(row=11, column= 0, )
    taptoplay_x = tk.Entry(root, width=10)
    taptoplay_x.grid(row=12, column=0)
    taptoplay_y = tk.Entry(root, width=10)
    taptoplay_y.grid(row=12, column=1)

    title_label = tk.Label(root, text="SelectCT Position:")
    title_label.grid(row=13, column= 0, )
    selectCT_x = tk.Entry(root, width=10)
    selectCT_x.grid(row=14, column=0)
    selectCT_y = tk.Entry(root, width=10)
    selectCT_y.grid(row=14, column=1)

    title_label = tk.Label(root, text="Start Position:")
    title_label.grid(row=15, column= 0, )
    start_x = tk.Entry(root, width=10)
    start_x.grid(row=16, column=0)
    start_y = tk.Entry(root, width=10)
    start_y.grid(row=16, column=1)

    title_label = tk.Label(root, text="CloseEvent Position:")
    title_label.grid(row=17, column= 0, )
    closeEvent_x = tk.Entry(root, width=10)
    closeEvent_x.grid(row=18, column=0)
    closeEvent_y = tk.Entry(root, width=10)
    closeEvent_y.grid(row=18, column=1)

    title_label = tk.Label(root, text="Auto Position:")
    title_label.grid(row=19, column= 0, )
    Auto_x = tk.Entry(root, width=10)
    Auto_x.grid(row=20, column=0)
    Auto_y = tk.Entry(root, width=10)
    Auto_y.grid(row=20, column=1)

    title_label = tk.Label(root, text="Keepticket Position:")
    title_label.grid(row=21, column= 0, )
    keepticket_x = tk.Entry(root, width=10)
    keepticket_x.grid(row=22, column=0)
    keepticket_y = tk.Entry(root, width=10)
    keepticket_y.grid(row=22, column=1)

    title_label = tk.Label(root, text="ตำแหน่งหน้าต่างเกมเช็คเมื่อหลุด : X,Y,W,H")
    title_label.grid(row=26, column= 0, )
    monitor_region_left = tk.Entry(root, width=10)
    monitor_region_left.grid(row=27, column=0)
    monitor_region_top = tk.Entry(root, width=10)
    monitor_region_top.grid(row=27, column=1)
    monitor_region_width = tk.Entry(root, width=10)
    monitor_region_width.grid(row=27, column=2)
    monitor_region_hight = tk.Entry(root, width=10)
    monitor_region_hight.grid(row=27, column=3)

    title_label = tk.Label(root, text="ตำแหน่งเช็คปุ่มออโต้ : X,Y,W,H")
    title_label.grid(row=28, column= 0, )
    check_Auto_left = tk.Entry(root, width=10)
    check_Auto_left.grid(row=29, column=0)
    check_Auto_top = tk.Entry(root, width=10)
    check_Auto_top.grid(row=29, column=1)
    check_Auto_width = tk.Entry(root, width=10)
    check_Auto_width.grid(row=29, column=2)
    check_Auto_hight = tk.Entry(root, width=10)
    check_Auto_hight.grid(row=29, column=3)

    title_label = tk.Label(root, text="ตำแหน่งเช็คตั๋ว5000 : X,Y,W,H")
    title_label.grid(row=30, column= 0, )
    check_ticket_top = tk.Entry(root, width=10)
    check_ticket_top.grid(row=31, column=1)
    check_ticket_left = tk.Entry(root, width=10)
    check_ticket_left.grid(row=31, column=0)
    check_ticket_width = tk.Entry(root, width=10)
    check_ticket_width.grid(row=31, column=2)
    check_ticket_hight = tk.Entry(root, width=10)
    check_ticket_hight.grid(row=31, column=3)

   


    
    root.mainloop()
