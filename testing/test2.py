import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/models')))

########################################################################
## IMPORTS MODULE
########################################################################
from models import bg1, bg2, bg3, bg4, bg5, button1, logo, show_hide_button, clearFrame, button3, product_in_Cart, checkout_Frame, QuantitySelector
from customtkinter import CTk, CTkLabel

class App:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        
        product_in_Cart(self.window).place(x=10, y=10)
if __name__ == "__main__":
    window = CTk()  # Membuat objek window utama
    window.resizable(True, True)
    gui = App(window)  # Membuat objek coba dan passing window utama
    window.mainloop()  # Menjalankan aplikasi
