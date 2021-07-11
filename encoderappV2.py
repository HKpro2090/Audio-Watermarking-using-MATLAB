import tkinter as tk
from tkinter import filedialog,Text
import os
import matlab.engine
from datetime import datetime
eng = matlab.engine.start_matlab()

root = tk.Tk()
root.title('Encoder Decoder')
encode = ['','','','']
decode = ['','','']

canvas = tk.Canvas(root,height=400,width=700,bg = 'gray88',bd = 0)
canvas.pack()

#Encoder Frame
frame = tk.Frame(root,bg='gray63')
frame.place(relwidth = 0.35,relheight = 0.093,relx = 0.09,rely = 0.1)

frame1 = tk.Frame(root,bg='gray63')
frame1.place(relwidth = 0.35,relheight = 0.093,relx = 0.09,rely = 0.2)

frame2 = tk.Frame(root,bg='gray63')
frame2.place(relwidth = 0.35,relheight = 0.093,relx = 0.09,rely = 0.4)

frame3 = tk.Frame(root,bg='gray63')
frame3.place(relwidth = 0.35,relheight = 0.093,relx = 0.09,rely = 0.48)

frame4 = tk.Frame(root,bg='gray63')
frame4.place(relwidth = 0.35,relheight = 0.2,relx = 0.09,rely = 0.7)

#Decode Frame
frame5 = tk.Frame(root,bg='gray63')
frame5.place(relwidth = 0.35,relheight = 0.19,relx = 0.55,rely = 0.1)

frame6 = tk.Frame(root,bg='gray63')
frame6.place(relwidth = 0.35,relheight = 0.093,relx = 0.55,rely = 0.4)

frame7 = tk.Frame(root,bg='gray63')
frame7.place(relwidth = 0.35,relheight = 0.093,relx = 0.55,rely = 0.48)

frame8 = tk.Frame(root,bg='gray63')
frame8.place(relwidth = 0.35,relheight = 0.2,relx = 0.55,rely = 0.7)

#Encoder buttons Function
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
    #print(encode)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Started at: ',dt_string)
    ret = eng.encoder(encode[1],encode[0],encode[2],encode[3])
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Ended at: ',dt_string)

#Decoder Button Functions
def files2print():
    label = tk.Label(root,text = ("Audio : "+decode[0]),padx = 5)
    label.pack()

def addaudio2():
    filename2 = filedialog.askopenfilename(initialdir = "C:\\",title = 'Select Audio File',filetypes=(("Wave Audio files","*.wav"),("All Files","*.*")))
    decode[0] = filename2
    files2print()

def rundecoder():
    decode[1] = str(dekey.get())
    decode[2] = str(imname.get())
    #print(decode)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Started at: ',dt_string)
    ret2 = eng.decoder(decode[0],decode[1],decode[2])
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Ended at: ',dt_string)

#Encoder buttons
audiofile = tk.Button(frame,text = 'Open Audio File',bg ='gray63', fg = '#000000',bd = 0,font = 'roboto', padx = 100,pady=6,command = addaudio)
audiofile.pack()
imagefile = tk.Button(frame1,text = 'Open Image File',bg ='gray63', fg = '#000000',bd = 0,font = 'roboto', padx = 100,pady=6,command = addimage)
imagefile.pack()
L1 = tk.Label(frame2, text="Email Id           ",bg = 'gray63',padx = 5)
L1.pack( side = 'left')
emailid = tk.Entry(frame2, bd =3,relief = 'flat',bg = 'gray78')
emailid.pack(side = 'left')
L2 = tk.Label(frame3, text="Save Audio as",bg = 'gray63',padx = 5)
L2.pack( side = 'left')
name = tk.Entry(frame3, bd =3,relief = 'flat',bg = 'gray78')
name.pack(side = 'left')
runapp = tk.Button(frame4,text = 'Encode!',bg ='gray63', fg = '#000000',bd = 0,font = 'roboto', padx = 120,pady=30, command = runencoder)
runapp.pack()

#Decoder Buttons
enaudiofile = tk.Button(frame5,text = 'Open Encoded Audio File',bg ='gray63', fg = '#000000',bd = 0,font = 'roboto', padx = 100,pady=30,command = addaudio2)
enaudiofile.pack()
L3 = tk.Label(frame6, text="Decryption Key",bg = 'gray63',padx = 5)
L3.pack( side = 'left')
dekey = tk.Entry(frame6, bd =3,relief = 'flat',bg = 'gray78')
dekey.pack(side = 'left')
L4 = tk.Label(frame7, text="Save Image as  ",bg = 'gray63',padx = 5)
L4.pack( side = 'left')
imname = tk.Entry(frame7, bd =3,relief = 'flat',bg = 'gray78')
imname.pack(side = 'left')
runapp = tk.Button(frame8,text = 'Decode!',bg ='gray63', fg = '#000000',bd = 0,font = 'roboto', padx = 120,pady=30,command = rundecoder)
runapp.pack()
root.mainloop()
