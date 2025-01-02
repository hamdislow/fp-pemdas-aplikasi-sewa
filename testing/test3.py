import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/method')))

########################################################################
## IMPORTS MODULE
########################################################################
from models import bg1, bg2, bg3, bg4, bg5, button1, entryField, Custom_Forgot_Pass, product_in_list, Tampilan_Invoice
from method import AccountManager
from customtkinter import CTk, CTkLabel

class App:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        
        manager = AccountManager()

        # Login sebagai pengguna
        manager.login("adip")

        # Tambahkan produk ke keranjang (berdasarkan nomor produk)
        manager.add_to_cart(1)  # Menambahkan produk nomor 1
        manager.add_to_cart(2)  # Menambahkan produk nomor 2
if __name__ == "__main__":
    window = CTk()  # Membuat objek window utama
    window.resizable(True, True)
    gui = App(window)  # Membuat objek App dan passing window utama
    window.mainloop()  # Menjalankan aplikasi