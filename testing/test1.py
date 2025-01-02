import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/widget')))

########################################################################
## IMPORTS MODULE
########################################################################
from widget import FontVariables, Custom_Frame, Default_Frame, Custom_Text, Custom_Button, ColorCodes, Custom_Entry, Custom_Button_Icon, Custom_scroll_frame, Custom_TopLevel
from customtkinter import CTk, CTkLabel

class App:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        
        self.Button = Custom_Button(self.window, command=self.topup_window)
        self.Button.place(x=100, y=50)
    
    def topup_window(self):
        self.topup_window = Custom_TopLevel(self.window)



if __name__ == "__main__":
    window = CTk()  # Membuat objek window utama
    # system = CTk()
    window.resizable(True, True)
    gui = App(window)  # Membuat objek coba dan passing window utama
    window.mainloop()  # Menjalankan aplikasi
