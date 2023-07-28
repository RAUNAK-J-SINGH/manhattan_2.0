import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
from helper_import import code_text_to_speech
import pyttsx3
import os


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')

# def speaknow():
#     text = text_area.get(1.0,tk.END)
#     gender = gender_combobox.get()
#     speed = speed_combobox.get()
#     voices = engine.getProperty('Voices')

#     def setVoice():
#         if (gender == 'Male'):
#             engine.setProperty('voice', voices[0].id)
#             engine.say(text)
#             engine.runAndWait()
#         else:
#             engine.setProperty('voice', voices[1].id)
#             engine.say(text)
#             engine.runAndWait()
    
#     if(text):
#         if(speed == "Fast"):
#             engine.setProperty('rate',250)
#             setVoice()
#         elif (speed == "Normal"):
#             engine.setProperty('rate',150)
#             setVoice()
#         else:
#             engine.setProperty('rate',60)
#             setVoice()

# def download():
#     print()


    

def GUI(user_speech):
    root = tk.Tk()
    root.title("TEXT TO SPEECH")
    root.geometry("900x450+150+125")
    root.resizable(True,True)
    root.config(bg="#305065")

    image_icon = tk.PhotoImage(file="icon1.png")
    root.iconphoto(False,image_icon)

    #top frame
    top_frame = tk.Frame(root, bg="white",width=900, height=100)
    top_frame.place(x=0,y=0)

    # logo = tk.PhotoImage(file="icon1.png")
    # tk.Label(top_frame,image=logo,bg="white").place(x=10,y=5)
    tk.Label(top_frame,text="Text to Speech", font="arial 20 bold",bg="white",fg="black").place(x=325,y=30)

    #text area
    text_input= tk.Text(root,font="Robote 20", bg ="white",relief="groove",wrap="word", state='disabled')
    text_input = tk.Entry(root)
    text_input.insert(0,user_speech)
    text_input.config(state="disabled")
    text_input.place(x=10,y=150,width=500,height=100)

    text_output = tk.Text(root,font="Robote 20", bg ="white",relief="groove",wrap="word")
    after_computation = "Hello i m working"
    text_output = tk.Entry(root)
    text_output.insert(0,after_computation)
    text_output.place(x=10,y=300,width=500,height=100)
    
    def speek_after_computation():
        
        code_text_to_speech(after_computation)

    tk.Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
    tk.Label(root,text="Speed",font="arial 15 bold",bg="#305065",fg="white").place(x=780,y=160)

    tk.Label(root,text="Input",font="arial 15 bold",bg="#305065",fg="white").place(x=60,y=110)
    tk.Label(root,text="Output",font="arial 15 bold",bg="#305065",fg="white").place(x=50,y=260)


    gender_combobox = Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
    gender_combobox.place(x=550,y=200)
    gender_combobox.set('Male')


    speed_combobox = Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",width=10)
    speed_combobox.place(x=750,y=200)
    speed_combobox.set('Normal')


    # imageicon = tk.PhotoImage(file="icon1.png")
    btn = tk.Button(root,text="Speak",width=10,font="arial 14 bold",command=speek_after_computation).place(x=550,y=280)

    btn = tk.Button(root,text="Retry",width=10,font="arial 14 bold").place(x=750,y=280)

    btn = tk.Button(root,text="Submit",width=27,font="arial 14 bold").place(x=550,y=350)


    root.mainloop()
    