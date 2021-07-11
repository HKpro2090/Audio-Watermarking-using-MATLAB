import tkinter as tk
from tkinter import filedialog, Text
import os
#import matlab.engine
from datetime import datetime
#eng = matlab.engine.start_matlab()
root = tk.Tk()
encode = ['','','','']
decode = ['','']

uicolour = '#708090'

canvas = tk.Canvas(root,height=400,width=700,bg = '#181818')
canvas.pack()

#Encoder Frame
frame = tk.Frame(root,bg='#404040')
frame.place(relwidth = 0.4,relheight = 0.5,relx = 0.09,rely = 0.1)

frame3 = tk.Frame(root,bg='#404040')
frame3.place(relwidth = 0.4,relheight = 0.2,relx = 0.09,rely = 0.7)

frame6 = tk.Frame(root,bg='#404040')
frame6.place(relwidth = 0.4,relheight = 0.1,relx = 0.09,rely = 0.6)


#Decoder Frame
frame2 = tk.Frame(root,bg='#404040')
frame2.place(relwidth = 0.35,relheight = 0.2,relx = 0.6,rely = 0.2)

frame4 = tk.Frame(root,bg='#404040')
frame4.place(relwidth = 0.35,relheight = 0.1,relx = 0.6,rely = 0.1)

frame5 = tk.Frame(root,bg='#404040')
frame5.place(relwidth = 0.35,relheight = 0.2,relx = 0.6,rely = 0.7)

#Encoder Functions
def filesprint():
    label = tk.Label(root,text = ("Audio : "+encode[0]),padx = 5)
    label.pack()
    label1 = tk.Label(root,text = ("Image : "+encode[1]),padx = 5)
    label1.pack()

def addaudio():
    filename = filedialog.askopenfilename(initialdir = "C:\\",title = 'Select Audio File',filetypes=(("Wave Audio files","*.wav"),("All Files","*.*")))
    encode[0] = filename

  
def addimage():
    filename = filedialog.askopenfilename(initialdir = "C:\\",title = 'Select Image File',filetypes=(("Png Image File","*.png"),("All Files","*.*")))
    encode[1] = filename
    filesprint()


def runencoder():
    encode[2] = str(emailid.get())
    encode[3] = str(name.get())
    print(encode)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Started at: ',dt_string)
    #ret = eng.encoder(encode[1],encode[0],encode[2],encode[3])
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Ended at: ',dt_string)

#Decoder Functions
def files2print():
    label = tk.Label(root,text = ("Audio : "+decode[0]),bg = '#404040',padx = 5)
    label.pack()

def addaudio2():
    filename2 = filedialog.askopenfilename(initialdir = "C:\\",title = 'Select Audio File',filetypes=(("Wave Audio files","*.wav"),("All Files","*.*")))
    decode[0] = filename2
    files2print()

def rundecoder():
    decode[1] = str(dekey.get())
    #print(decode)
    now = datetime.now()
    print('Started at: ',now)
    #ret2 = eng.decoder(decode[0],decode[1])
    now = datetime.now()
    print('Ended at: ',now)

#Encoder Frame Buttons
audiofile = tk.Button(frame,text = 'Open Audio File',bg='#404040',bd = 0,font = 'calibri', padx = 100,pady=5,command = addaudio)
audiofile.pack()
imagefile = tk.Button(frame,text = 'Open Image File',bg='#404040',bd = 0,font = 'calibri',padx = 100,pady= 5, command = addimage)
imagefile.pack()
L1 = tk.Label(frame, text="Email Id",bg = '#404040',padx = 5)
L1.pack( side = 'left')
emailid = tk.Entry(frame, bd =3)
emailid.pack(side = 'left')
runapp = tk.Button(frame3,text = 'Encode!',bg='#404040',bd = 0,font = 'calibri', padx = 120,pady=30,command = runencoder)
runapp.pack()




#Decoder Frame Buttons
enaudiofile = tk.Button(frame2,text = 'Open Encoded Audio File',bg='#404040',bd = 0,font = 'calibri', padx = 100,pady=30,command = addaudio2)
enaudiofile.pack()
runapp = tk.Button(frame5,text = 'Decode!',bg='#404040',bd = 0,font = 'calibri', padx = 100,pady=30,command = rundecoder)
runapp.pack()

L2 = tk.Label(frame4, text="Decrypt Key",bg = '#404040',padx = 5)
L2.pack( side = 'left')
dekey = tk.Entry(frame4, bd =3)
dekey.pack(side = 'left')

L3 = tk.Label(frame6, text="Save as",bg = '#404040',padx = 5)
L3.pack( side = 'left')
name = tk.Entry(frame6, bd =3)
name.pack(side = 'left')

root.mainloop()
