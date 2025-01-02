########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui.ui import *
########################################################################

class MainWindow():
    def __init__(self, master):
        self.window = master
        self.window.title("Parking System")
        self.window.geometry("360x640+500+20")  # Ukuran window utama
        self.ui = Tampilan_start(self.window)


if __name__ == "__main__":
    window = CTk()  # Membuat objek window utama
    window.resizable(True, True)
    gui = MainWindow(window)  # Membuat objek Tampilan_start dan passing window utama
    window.mainloop()  # Menjalankan aplikasi
