import keyboard  # using module keyboard
import webbrowser,time
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", 1)
root.withdraw()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('ctrl+y'):  # if key 'q' is pressed 
            messagebox.showwarning('awa', '陳佑軒你要幫她們加一首歌嗎?')
        if keyboard.is_pressed('ctrl+o'):  # if key 'q' is pressed 
            messagebox.showwarning('awa', '放學不是在跳')
        if keyboard.is_pressed('ctrl+n'):
            webbrowser.open('https://youtu.be/CqWZq1mJJh0?t=11')
            time.sleep(1)
        if keyboard.is_pressed('ctrl+r'):
            webbrowser.open('https://youtu.be/t9N5Msr_Ftg')
            time.sleep(1)
        if keyboard.is_pressed('ctrl+i'):
            break
        time.sleep(0.00001)
    except:
        pass