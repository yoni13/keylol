import keyboard  # using module keyboard
import webbrowser
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
            webbrowser.open_new_tab('https://youtu.be/CqWZq1mJJh0?t=11')
        if keyboard.is_pressed('ctrl+i'):
            break
    except:
        pass