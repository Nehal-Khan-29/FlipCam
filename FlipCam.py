#Libraries

import cv2
import os
import speech_recognition as sr
import time
import pyttsx3
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox


icon = tk.Tk()
icon.title('FlipCam')
icon.iconbitmap("icon.ico")
image = Image.open("icon.png")
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(icon, image=tk_image)
image_label.pack()
icon.update()
screen_width = icon.winfo_screenwidth()
screen_height = icon.winfo_screenheight()
window_width = 256  
window_height = 226  
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
icon.geometry("+{}+{}".format(x, y))
icon.after(3000, icon.destroy)
icon.mainloop()


#variables

cap=cv2.VideoCapture(0)
folder_path = "FlipCam"
photo_value_path="FlipCam/Photo_value.txt"

#Directory add

directory = os.getcwd()
folder_name = "FlipCam"

if not os.path.exists(os.path.join(directory, folder_name)):
    os.makedirs(os.path.join(directory, folder_name))
    print(f"Folder '{folder_name}' created in '{directory}' directory.")
else:
    print(f"Folder '{folder_name}' already exists in '{directory}' directory.")

#speach
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Photo_value
try:
    with open(photo_value_path) as save:
        Photo_value = int(save.read())
except FileNotFoundError:
    Photo_value = 1

speak("open Flip cam")

#Tkinter page
def func():
    messagebox.showinfo('FlipCam','''
    p - Photo
    t - Timer 10 sec
    f - Flip camera
    e - Exit''')



#Program
run = False
func()    
while not run:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("FlipCam", frame)

    key = cv2.waitKey(1)
    if key== ord("e"):
        engine.setProperty('voice', voices[1].id)
        speak("Close Flip cam")
        break

    elif key== ord("p"):
        image_name = "Photo {}.png".format(Photo_value)
        Photo_value += 1
        with open(photo_value_path,"w") as save:
            save.write(str(Photo_value))
        image_path = os.path.join(folder_path, image_name)
        cv2.imwrite(image_path,frame)
        speak("photo taken")
    
    elif key== ord("t"):
                speak("Taking photo in 10 seconds")
                key = cv2.waitKey(10000)
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)
                image_name = "Photo {}.png".format(Photo_value)
                Photo_value += 1
                with open(photo_value_path,"w") as save:
                    save.write(str(Photo_value))
                image_path = os.path.join(folder_path, image_name)
                cv2.imwrite(image_path,frame)
                speak("Photo taken")
        


    if key== ord("f"):
        speak("flip camera")
        while True:
            ret, frame = cap.read()
            cv2.imshow("FlipCam", frame)

            key = cv2.waitKey(1)
            if key== ord("f"):
                speak("flip camera")
                break

            elif key== ord("p"):
                image_name = "Photo {}.png".format(Photo_value)
                Photo_value += 1
                with open(photo_value_path,"w") as save:
                    save.write(str(Photo_value))
                image_path = os.path.join(folder_path, image_name)
                cv2.imwrite(image_path,frame)
                speak("photo taken")
            
            elif key== ord("t"):
                speak("Taking photo in 10 seconds")
                key = cv2.waitKey(10000)
                ret, frame = cap.read()
                image_name = "Photo {}.png".format(Photo_value)
                Photo_value += 1
                with open(photo_value_path,"w") as save:
                    save.write(str(Photo_value))
                image_path = os.path.join(folder_path, image_name)
                cv2.imwrite(image_path,frame)
                speak("Photo taken")
            
            if key== ord("e"):
                run = True
                engine.setProperty('voice', voices[1].id)
                speak("Close Flip cam")
                break
                
                
cap.release()
cv2.destroyAllWindows()

