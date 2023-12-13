from gc import disable
from tkinter import *
from tkinter import messagebox
from turtle import left
from customtkinter import *
from referencing import Anchor
import socket
from PIL import Image, ImageTk 
import os,sys,re
import time
import threading
import json
import pickle

#--------Fonction--------#

#Serveur
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connection():
    print("Connecting")
    PorT = sidebar_entry_port.get()
    try:
        int_port = int(PorT)
    except:
        return
    host, port = (str(sidebar_entry_address.get()),int_port)

    try:
        socket.connect((host, port))
        receive_thread = threading.Thread(target=receive_messages, args=(socket,))
        receive_thread.start()
        print("Connect")

        data = f"{sidebar_entry_username.get()}"
        data = data.encode("utf8")
        socket.sendall(data)
        
        
    except:
        print("connection serveur failed")

def receive_messages(socket):
    while True:
        try:
            data = socket.recv(1024)
            message = pickle.loads(data)
            try:
                if message['afficher'] == True:
                    print(message['data'])
                    textbox_jeu.configure(state="normal")
                    textbox_jeu.insert(END, f"{message['data']}\n")
                    textbox_jeu.configure(state="disable")
            except:
                try:
                    if message['serveur']:
                        pass
                except:
                    pass
        except socket.error as e:
            print(f"Erreur lors de la réception du message: {str(e)}")





#jestion bouton
        
def on_button_click_carte(button_text):
    for i in range(len(a)):
        if str(a[i]) == button_text:
            image = Image.open(os.path.join(script_dir, "assets/cartes/dos.jpg"))
            image.thumbnail((60,200))
            photo = ImageTk.PhotoImage(image)
            b[i].configure(state="disabled", command=None, image=photo)
            break
    data = str(button_text)
    data = data.encode("utf8")
    socket.sendall(data)


def on_button_click(button_text):
    
    data = str(button_text)
    data = data.encode("utf8")
    socket.sendall(data)




#Widgets

def side_bar():
    global sidebar_entry_address,sidebar_entry_port,sidebar_entry_username,sidebar_button_Valider
    
    sidebar_frame = CTkFrame(fenetre, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

    sidebar_frame.grid_rowconfigure(5, weight=1)
    logo_label = CTkLabel(sidebar_frame, text="Tarrot", font=CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    sidebar_entry_address = CTkEntry(sidebar_frame, placeholder_text="address")
    sidebar_entry_address.grid(row=2, column=0, padx=20, pady=10)

    sidebar_entry_port = CTkEntry(sidebar_frame, placeholder_text="port")
    sidebar_entry_port.grid(row=3, column=0, padx=20, pady=10)

    sidebar_entry_username = CTkEntry(sidebar_frame, placeholder_text="username")
    sidebar_entry_username.grid(row=1, column=0, padx=20, pady=10)

    sidebar_button_Valider = CTkButton(sidebar_frame, text="Valider", command=connection)
    sidebar_button_Valider.grid(row=4, column=0, padx=20, pady=10)

    appearance_mode_label = CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))

    appearance_mode_optionemenu = CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"], command=change_appearance_mode_event)
    appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))

    scaling_label = CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))

    scaling_optionemenu = CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=change_scaling_event)
    scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))
    
    appearance_mode_optionemenu.set("Dark")
    scaling_optionemenu.set("100%")
    
    return

def carte_wid(list= ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","a24"]):
    a,b=[],[]
    cmpt = 1 
    for i in list:
        a.append(i)
        image = Image.open(os.path.join(script_dir, "assets/cartes/petit.jpg"))
        image.thumbnail((60,200))
        photo = ImageTk.PhotoImage(image)
        i = CTkButton(carte, image = photo, text = "",width=0,command=lambda t=i: on_button_click_carte(t))#,height=0)
        b.append(i)
        if cmpt <= 8:
            if cmpt == 8:
                i.grid(row=1, column=cmpt, padx=(20, 20), pady=(20, 0), sticky="nsew")
            else: 
                i.grid(row=1, column=cmpt, padx=(20, 0), pady=(20, 0), sticky="nsew")
        else:
            if cmpt <= 16:
                if cmpt == 16:
                    i.grid(row=2, column=cmpt-8, padx=(20, 20), pady=(20, 0), sticky="nsew")
                else: 
                    i.grid(row=2, column=cmpt-8, padx=(20, 0), pady=(20, 0), sticky="nsew")
            else:      
                if cmpt == 24:
                    i.grid(row=3, column=cmpt-16, padx=(20, 20), pady=(20, 20), sticky="nsew")
                else:
                    i.grid(row=3, column=cmpt-16, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        cmpt += 1
    return a,b




def change_appearance_mode_event(new_appearance_mode: str):
    set_appearance_mode(new_appearance_mode)

def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

#Initialisation

def initialize():
    global script_dir
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    fenetre.iconbitmap(os.path.join(script_dir, "assets/logo/logo.ico"))
    image = PhotoImage(file=os.path.join(script_dir, "assets/logo/logo.png"))
    fenetre.iconphoto(False, image)


#-----------Main-----------#

set_appearance_mode("dark")
fenetre = CTk()
fenetre.geometry("1280x720")
fenetre.title("Tarrot")

#menubar()
initialize()

# configure grid layout (4x4)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure((2, 3), weight=0)
fenetre.grid_rowconfigure((0, 1), weight=1)

# create sidebar frame with widgets
side_bar()


# create textbox
textbox_jeu = CTkTextbox(fenetre, width=250, state="disable")
textbox_jeu.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

# create tabview
tabview = CTkTabview(fenetre, width=250)
tabview.grid(row=0, column=12, padx=(20, 20), pady=(20, 0), sticky="nsew")
tabview.add("Tchat")
tabview.add("Serveur")

textbox_serv = CTkTextbox(tabview.tab("Serveur"),height=150, state="disable")
textbox_serv.grid(row=0, column=0, padx=(20, 20), pady=(0, 20), sticky="nsew")
entry_serv = CTkEntry(tabview.tab("Serveur"))
entry_serv.grid(row=2, column=0, padx=(20, 20), pady=(0, 20), sticky="nsew")


#créé les boutons
carte = CTkFrame(fenetre, width=250)
carte.grid(row=1, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

global a,b
a,b = carte_wid()


tab_mune_option = CTkTabview(fenetre, width=250)
tab_mune_option.grid(row=1, column=12, padx=(20, 20), pady=(20, 20), sticky="nsew")
tab_mune_option.add("Jeux")
tab_mune_option.add("Option ")

global tab_mune_option_Jeux_btPret
tab_mune_option_Jeux_btPret = CTkButton(tab_mune_option.tab("Jeux"), text="Prêt", command=lambda t="pret": on_button_click(t))
tab_mune_option_Jeux_btPret.grid(row=0, column=0, padx=50, pady=(10, 10))



fenetre.mainloop() 
