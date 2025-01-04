import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../widget')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../method')))
########################################################################
## IMPORTS MODULE
########################################################################
from widget import FontVariables, Custom_Frame, Custom_Button, Default_Frame, ColorCodes, Custom_Image, Custom_Text, Custom_Button_Icon, Custom_Entry, Custom_TopLevel, Custom_scroll_frame
from customtkinter import CTkImage, CTkFrame,CTkButton,CTkLabel, IntVar, CTkCheckBox, CTkToplevel
import uuid  # Import for generating a unique transaction ID
from method import AccountManager
from datetime import datetime
from widget import Custom_Messagebox
from PIL import Image
import csv

class bg1:
    def __init__(self, master):
        self.window = master
        self.main_frame = Default_Frame(self.window).place(x=0, y =0)
        Custom_Frame(self.main_frame, height=550).place(x=0, y=160)

class bg2:
    def __init__(self, master):
        self.window = master
        self.main_frame = Default_Frame(self.window).place(x=0, y =0)
        Custom_Frame(self.main_frame, height=570).place(x=0, y=90)

class bg3:
    def __init__(self, master):
        self.window = master
        self.main_frame = Default_Frame(self.window).place(x=0, y =0)
        Custom_Frame(self.main_frame, height=670, corner_radius=60).place(x=0, y=-100)

class bg4:
    def __init__(self, master):
        self.window = master
        self.main_frame = Default_Frame(self.window, fg_color=ColorCodes().secondary_color).place(x=0, y =0)
        Custom_Frame(self.main_frame, height=150, width=150, fg_color=ColorCodes().main_color, bg_color=ColorCodes().secondary_color, corner_radius=150).place(x=270, y=-50)
        Custom_Frame(self.main_frame, height=250, width=250, fg_color=ColorCodes().main_color, bg_color=ColorCodes().secondary_color, corner_radius=250).place(x=-130, y=450)

class bg5:
    def __init__(self, master):
        self.window = master
        self.main_frame = Default_Frame(self.window, fg_color=ColorCodes().secondary_color).place(x=0, y =0)
        Custom_Frame(self.main_frame, height=150, width=360, fg_color=ColorCodes().main_color, bg_color=ColorCodes().secondary_color, corner_radius=25).place(x=0, y=-120)
        Custom_Frame(self.main_frame, height=420, width=360, fg_color=ColorCodes().main_color, bg_color=ColorCodes().secondary_color, corner_radius=25).place(x=0, y=300)

class button1(Custom_Button):
    def __init__(self, master, text,bg_color, command):
        super().__init__(master=master, text=text, text_color=ColorCodes().secondary_color, fg_color=ColorCodes().third_color, bg_color= bg_color, command=command)

class button2(Custom_Button):
    def __init__(self, master, text, bg_color, command):
        super().__init__(master=master, text=text, border_width=2, text_color=ColorCodes().third_color, border_color=ColorCodes().third_color, fg_color=ColorCodes().secondary_color, bg_color= bg_color, command=command)

class button3(Custom_Button):
    def __init__(self, master, text,bg_color,image, command):

        self.image_path = image
        self.image = CTkImage(Image.open(self.image_path), size=(20, 20))
        
        super().__init__(master=master, text=text, compound="right",image=self.image,text_color=ColorCodes().secondary_color, width=160,fg_color=ColorCodes().third_color, font=FontVariables().Heading2_Custom_Font, hover_color=ColorCodes().third_color,bg_color= bg_color,command=command)

class logo(Custom_Frame):
    def __init__(self, master, fg_color=ColorCodes().secondary_color, width=150, height=90, **kwargs):
        super().__init__(master,fg_color=fg_color, width=width,height=height,**kwargs)
        self.configure(corner_radius=10,bg_color=ColorCodes().secondary_color)

        # Terpilih Total
        self.sudo = Custom_Text(self, text="SUDO",text_color=ColorCodes().third_color, font=("Poppins", 36))
        self.sudo.place(x=20,y=0)
        self.super_roda = Custom_Text(self, text="Super Roda",justify="center",text_color=ColorCodes().third_color, font=("Poppins", 24))
        self.super_roda.place(x=5,y=45)
        self.frame1= Custom_Frame(self,bg_color=ColorCodes().secondary_color,fg_color=ColorCodes().main_color,width=20,height=20,corner_radius= 20)
        self.frame1.place(x=100, y=14)

class logo1(Custom_Frame):
    def __init__(self, master, fg_color=ColorCodes().main_color, width=75, height=55, **kwargs):
        super().__init__(master,fg_color=fg_color, width=width,height=height,**kwargs)
        self.configure(corner_radius=10,bg_color=ColorCodes().main_color)

        # Terpilih Total
        self.sudo = Custom_Text(self, text="SUDO",text_color=ColorCodes().third_color, font=("Poppins", 18))
        self.sudo.place(x=10,y=0)
        self.super_roda = Custom_Text(self, text="Super Roda",justify="center",text_color=ColorCodes().third_color, font=("Poppins", 12))
        self.super_roda.place(x=5,y=25)
        self.frame1= Custom_Frame(self,bg_color=ColorCodes().main_color,fg_color=ColorCodes().secondary_color,width=10,height=10,corner_radius= 20)
        self.frame1.place(x=50, y=7)


class heading(Custom_Text):
    def __init__(self, master, text, fg_color=ColorCodes().main_color):
        super().__init__(master=master, text=text, width=300, font=FontVariables().Heading1_Custom_Font, fg_color=ColorCodes().main_color)

        self.configure(
            fg_color=fg_color
        )
class heading2(Custom_Text):
    def __init__(self, master, text, anchor="w"):
        super().__init__(master=master, text=text, width=300, font=FontVariables().Heading2_Custom_Font, text_color=ColorCodes().third_color)

        self.configure(anchor=anchor)
class paragraph(Custom_Text):
    def __init__(self, master, text, anchor="w", width=315,height=20):
        super().__init__(master=master, text=text, anchor="w", width=315, height=30,font=FontVariables().Paragraph1_Custom_Font, fg_color=ColorCodes().main_color)

        self.configure(anchor=anchor, width=width, height=height)

class show_hide_button(Custom_Button):
    def __init__(self, master, target):
        self.window = master
        self.entry_widget = target

        # Ikon untuk show dan hide
        self.hidden_icon_path = r"assets\icon\hidden.png"
        self.eye_icon_path = r"assets\icon\eye.png"

        self.hidden_icon = CTkImage(Image.open(self.hidden_icon_path), size=(20, 20))
        self.eye_icon = CTkImage(Image.open(self.eye_icon_path), size=(20, 20))

        super().__init__(
            master=self.window,
            text="",  # Tidak ada teks di tombol
            bg_color=ColorCodes().secondary_color,
            fg_color=ColorCodes().secondary_color,
            hover_color=ColorCodes().secondary_color,
            image=self.hidden_icon,  # Gunakan ikon tersembunyi sebagai default
            command=self.toggle_password_visibility,  # Fungsi untuk show/hide password
            width=5,  # Lebar tombol
            height=5,  # Tinggi tombol
        )

    def toggle_password_visibility(self):
        """Fungsi untuk mengubah mode password pada entry_widget."""
        if self.entry_widget.cget("show") == "*":  # Jika password disembunyikan
            self.entry_widget.configure(show="")  # Perlihatkan password
            self.configure(image=self.eye_icon)  # Ganti ikon menjadi mata terbuka
        else:  # Jika password terlihat
            self.entry_widget.configure(show="*")  # Sembunyikan password
            self.configure(image=self.hidden_icon)  # Ganti ikon menjadi mata tertutup

class entryField(Custom_Entry):
    def __init__(self, master, placeholder="", show="",bg_color=ColorCodes().secondary_color, state="normal"):
        self.window = master
        
        # Inisialisasi elemen entry dengan state default 'normal'
        super().__init__(
            self.window,
            placeholder_text=placeholder,
            show=show,
        )
        
        # Mengatur state setelah entry diinisialisasi
        self.configure(state=state, bg_color=bg_color)

class icon(Custom_Button_Icon):
    def __init__(self, master,x,y,panjang,lebar,bg_color,link, command):
        self.window = master
        self.link_icon = link        
        self.Button = Custom_Button_Icon(self.window,text="",bg_color = bg_color, fg_color=ColorCodes().main_color,icon=self.link_icon,command=command, hover_color=ColorCodes().main_color, icon_size=(panjang, lebar),font=FontVariables().Heading2_Custom_Font).place(x=x, y=y)

class checkout_Frame(CTkFrame):
    def __init__(self, master, cart, user_info, **kwargs):
        super().__init__(master, **kwargs)
        self.cart = cart  # Store the cart data
        self.user_info = user_info  # Store user information
        self.configure(corner_radius=10, border_color=ColorCodes().main_color, fg_color=ColorCodes().secondary_color, width=300, bg_color=ColorCodes().secondary_color, border_width=2)

        # Total Units
        self.label_terpilih = CTkLabel(self, text="Terpilih Total:", text_color=ColorCodes().third_color, font=FontVariables().Paragraph1_Custom_Font)
        self.label_terpilih.grid(row=0, column=0, padx=(10, 5), pady=(5, 2), sticky="w")

        self.value_terpilih = CTkLabel(self, text=f"{self.calculate_total_quantity()} Unit", text_color=ColorCodes().third_color, font=FontVariables().Paragraph1_Custom_Font)
        self.value_terpilih.grid(row=1, column=0, padx=(10, 5), pady=(2, 5), sticky="w")

        # Total Price
        self.label_harga = CTkLabel(self, text="Total Harga:", text_color=ColorCodes().third_color, font=FontVariables().Paragraph1_Custom_Font)
        self.label_harga.grid(row=0, column=1, padx=(10, 5), pady=(5, 2), sticky="w")

        self.value_harga = CTkLabel(self, text=f"Rp. {self.calculate_total_price():,.2f}", text_color=ColorCodes().third_color, font=FontVariables().Paragraph1_Custom_Font)
        self.value_harga.grid(row=1, column=1, padx=(10, 5), pady=(2, 5), sticky="w")

        # Checkout Button
        self.button_checkout = CTkButton(
            self, text="Check Out", width=80, fg_color=ColorCodes().main_color, hover_color=ColorCodes().main_color, text_color=ColorCodes().third_color, font=FontVariables().Paragraph2_Custom_Font, command=self.checkout
        )
        self.button_checkout.grid(row=0, column=2, rowspan=2, padx=(10, 10), pady=(5, 5), sticky="e")

    def calculate_total_price(self):
        """Calculate the total price of checked items in the cart."""
        total_price = sum(item['price'] * item['quantity'] for item in self.cart if item['checked'])
        return total_price

    def calculate_total_quantity(self):
        """Calculate the total quantity of checked items in the cart."""
        total_quantity = sum(item['quantity'] for item in self.cart if item['checked'])
        return total_quantity

    def checkout(self):
        """Handle the checkout process."""
        checked_items = [item for item in self.cart if item['checked']]
        if not checked_items:
            Custom_Messagebox.messagebox("Error", "No items selected for checkout!")
            return

        # Proceed with checkout for checked items
        payment_info = {"method": "saldo"}  # Example payment info
        checkout = Checkout(checked_items, self.user_info)
        try:
            invoice = checkout.checkout(payment_info)
            Custom_Messagebox.messagebox("Success", "Checkout successful! Invoice saved.")
        except Exception as e:
            Custom_Messagebox.messagebox("Error", str(e))


class product_in_Cart(CTkFrame):
    def __init__(self, master,name_product,unit,price, image_path,**kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(corner_radius=20, border_color=ColorCodes().secondary_color, fg_color=ColorCodes().secondary_color,height=200,bg_color=ColorCodes().main_color, border_width=2)

        self.image_product = Custom_Image(self,image=image_path, width=100, height=80)
        self.image_product.grid(row=0, column=0, rowspan=2, padx=(20, 10), pady=(10, 10))
        self.chk_box = CTkCheckBox(self,checkbox_width=20, checkbox_height=20,width=20, text="", hover_color=ColorCodes().main_color, fg_color=ColorCodes().main_color, checkmark_color=ColorCodes().third_color,border_color=ColorCodes().third_color)
        self.chk_box.place(x=10,y=5)
        
        self.label_product = CTkLabel(self, text=name_product,text_color=ColorCodes().third_color, width=130,wraplength=130, justify="left",anchor="w", font=("Arial",9,"bold"))
        self.label_product.grid(row=0, column=1, padx=(0, 20), pady=(5, 0), sticky="w")
        self.frame_desc = CTkFrame(self, border_color=ColorCodes().secondary_color, fg_color=ColorCodes().secondary_color, width=300, height=60,bg_color=ColorCodes().secondary_color)
        self.frame_desc.grid(row=1, column=1, padx=(0,20), pady=0, sticky="w")

        self.frame_desc.grid_columnconfigure((0,1,2,3), weight=0)
        self.frame_desc.grid_columnconfigure((0,1), weight=0)

        self.unit = CTkLabel(self.frame_desc,text= unit,text_color=ColorCodes().third_color,font=FontVariables().Paragraph1_Custom_Font)
        self.unit.grid(row=0, column=0,columnspan=2,padx=(0,2), pady=0, sticky="w")
        self.harga = CTkLabel(self.frame_desc,anchor="w", text= price,text_color=ColorCodes().third_color,font=FontVariables().Paragraph2_Custom_Font)
        self.harga.grid(row=1, column=0, columnspan=2,padx=0, pady=0)
        self.qty = QuantitySelector(self.frame_desc)
        self.qty.grid(row=0, column=2,columnspan=2,padx=(0,0),pady=0, sticky="w")

class product_in_list(CTkFrame):
    def __init__(self, master, product_name, price, status, qty, image_path,add_to_cart_function, **kwargs):
        super().__init__(master=master, **kwargs)
        self.data = r"data\product.csv"
        self.configure(corner_radius=20, border_color=ColorCodes().secondary_color, fg_color=ColorCodes().secondary_color,height=200, bg_color=ColorCodes().main_color, border_width=2)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.image_product = Custom_Image(self,image=image_path, width=80, height=64)
        self.image_product.grid(row=0, column=0, rowspan=3, padx=(20, 10), pady=(10, 10))
        self.button = Custom_Button(self, compound="left", text="Add to Cart", width=10, height=20, bg_color=ColorCodes().secondary_color,font=FontVariables().Paragraph3_Custom_Font, command=add_to_cart_function)
        self.button.grid(row=3, column=0, padx=0, pady=(0,10))
        
        self.label_product = CTkLabel(self,text=product_name,text_color=ColorCodes().third_color,width=150,wraplength=140,justify="left",anchor="w",font=FontVariables().Paragraph1_Custom_Font)
        self.label_product.grid(row=0, column=1, padx=(0, 20), pady=(0, 0), sticky="w")

        self.frame_desc = CTkFrame(self, border_color=ColorCodes().secondary_color, fg_color=ColorCodes().secondary_color, width=300, height=60,bg_color=ColorCodes().secondary_color)
        self.frame_desc.grid(row=1, column=1, rowspan=3, padx=(0,20), pady=0, sticky="nw")

        self.frame_desc.grid_columnconfigure((0,1,2,3), weight=0)
        self.frame_desc.grid_rowconfigure((0,1), weight=0)

        self.status = CTkLabel(self.frame_desc, anchor="w", justify="left",text= status, width=30,text_color=ColorCodes().third_color,font=FontVariables().Paragraph1_Custom_Font)
        self.status.grid(row=0, column=0, columnspan=2,padx=(0, 10), pady=0)
        self.unit = CTkLabel(self.frame_desc,text= qty,anchor="e",text_color=ColorCodes().third_color, font=FontVariables().Paragraph1_Custom_Font)
        self.unit.grid(row=0, column=2,columnspan=2,padx=0, pady=0)

        self.harga= CTkLabel(self.frame_desc,anchor="center", text= price, text_color=ColorCodes().third_color,font=FontVariables().Paragraph2_Custom_Font)
        self.harga.grid(row=1, column=0, columnspan=2, padx=(0,10))
    
    
class QuantitySelector(CTkFrame):
    def __init__(self, master, icon_increase=None, icon_decrease=None,fg_color=ColorCodes().secondary_color, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=fg_color, width=50)
        self.quantity = IntVar(value=1)

        def increase():
            self.quantity.set(self.quantity.get() + 1)

        def decrease():
            if self.quantity.get() > 1:
                self.quantity.set(self.quantity.get() - 1)

        # Decrease Button
        self.decrease_button = Custom_Button_Icon(self,icon=r"assets\icon\minus.png",width=10, height=10, command=decrease,fg_color=ColorCodes().secondary_color,
                                                    bg_color= ColorCodes().secondary_color,text_color="white",hover_color=ColorCodes().secondary_color)
        self.decrease_button.grid(row=0, column=0, padx=(0,1), sticky="w")

        # Label to Display Quantity
        self.quantity_label = CTkLabel(self, textvariable=self.quantity,fg_color=ColorCodes().secondary_color, text_color=ColorCodes().third_color,font=FontVariables().Paragraph2_Custom_Font)
        self.quantity_label.grid(row=0, column=1, padx=5)

        # Increase Button
        self.increase_button = Custom_Button_Icon(self,icon=r"assets\icon\plus.png",width=10, height=10, command=increase, 
                                                    fg_color=ColorCodes().secondary_color,bg_color= ColorCodes().secondary_color,
                                                    text_color="white", hover_color=ColorCodes().secondary_color)
        self.increase_button.grid(row=0, column=2, padx=(1,0))

class Custom_Forgot_Pass(CTkToplevel):
    def __init__(self, master, account_manager, title="Lupa Password",fg_color=ColorCodes().main_color, 
                width=400, height=250):
        super().__init__(master, fg_color=fg_color)

        # Mengatur ukuran dan posisi jendela
        self.geometry(f"{width}x{height}+500+200")
        self.title(title)
        self.resizable(False, False)

        # Menyimpan referensi ke AccountManager
        self.account_manager = account_manager

        # Frame utama
        self.main_frame = CTkFrame(self, fg_color=ColorCodes().secondary_color,corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Label untuk teks utama
        self.label = CTkLabel(self.main_frame, font=FontVariables().Heading2_Custom_Font, text="Masukkan username Anda", wraplength=width - 40, text_color=ColorCodes().third_color, justify="center")
        self.label.pack(pady=(10, 10))

        # Input untuk username
        self.entry_username = Custom_Entry(self.main_frame, placeholder_text="Masukkan username Anda")
        self.entry_username.pack(pady=(10, 10))

        # Tombol untuk cek password
        self.button_check = Custom_Button(self.main_frame, width=40,height=20,bg_color = ColorCodes().secondary_color,
                                        font=FontVariables().Paragraph2_Custom_Font,text="Lihat Password",command=self.check_password)
        self.button_check.pack(pady=(10, 10))

        # Label untuk menampilkan hasil
        self.result_label = CTkLabel(self.main_frame, text="",text_color=ColorCodes().third_color,font=FontVariables().Paragraph2_Custom_Font, justify="center")
        self.result_label.pack(pady=(10, 10))
        # Menahan fokus di messagebox
        self.grab_set()

    def check_password(self):
        """
        Cek apakah username valid dan tampilkan password.
        """
        username = self.entry_username.get()
        password = self.account_manager.get_user_password(username)
        if password:
            self.result_label.configure(text=f"Password Anda: {password}")
        else:
            self.result_label.configure(text="Username tidak ditemukan!")

class Custom_Topup(CTkToplevel):
    def __init__(self, master,user_info, title="Top Up", fg_color=ColorCodes().main_color, 
                width=400, height=250):
        super().__init__(master, fg_color=fg_color)
        # Mengatur ukuran dan posisi jendela
        self.user_info = user_info
        self.geometry(f"{width}x{height}+500+300")
        self.title(title)
        self.resizable(False, False)
        self.account_manager = AccountManager()
        self.logged_in = False

        # Frame utama
        self.main_frame = CTkFrame(self, fg_color=ColorCodes().secondary_color, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Label untuk teks utama
        self.label = CTkLabel(
            self.main_frame,
            font=FontVariables().Heading2_Custom_Font,
            text="Masukkan jumlah top-up",
            wraplength=width - 40,
            text_color=ColorCodes().third_color,
            justify="center",
        )
        self.label.pack(pady=(10, 10))

        # Input untuk jumlah top-up
        self.entry_amount = Custom_Entry(self.main_frame, placeholder_text="Jumlah Top-Up")
        self.entry_amount.pack(pady=(10, 10))
        # Tombol untuk melakukan top-up
        self.button_topup = Custom_Button(
            self.main_frame,
            width=40,
            height=20,
            bg_color=ColorCodes().secondary_color,
            font=FontVariables().Paragraph2_Custom_Font,
            text="Top Up",
            command=lambda: self.process_top_up(),  # Gunakan metode lokal
        )
        self.button_topup.pack(pady=(10, 10))

        # Label status untuk menampilkan hasil
        self.status_label = CTkLabel(
            self.main_frame,
            font=FontVariables().Paragraph2_Custom_Font,
            text="",
            text_color="green",
            justify="center",
        )
        self.status_label.pack(pady=(10, 10))

        # Menahan fokus di messagebox
        self.grab_set()

    def process_top_up(self):
        """Proses top-up dengan validasi input."""
        self.account_manager = AccountManager()
        self.isLoggedIn = self.account_manager.load_user_data()

        self.logged_in_users = [username for username, data in self.isLoggedIn.items() if data['IsLoggedIn']]
        
        username = self.user_info.get("Username", "")
        self.balance = self.account_manager.get_user_balance(username)

        if self.logged_in_users:  # Pastikan ada pengguna yang login
            self.current_user = self.logged_in_users[0]  # Ambil username pertama yang login
            
            try:
                amount = float(self.entry_amount.get())
                if amount <= 0:
                    self.status_label.configure(text="Masukkan jumlah positif.", text_color="red")
                    return

                # Proses top-up
                if self.account_manager.top_up(amount):
                    saldo = self.account_manager.user_data[self.current_user]['Saldo']
                    self.status_label.configure(text=f"Top-up berhasil! Saldo: {saldo}", text_color="green")
                    
                    # Update saldo di Tampilan_main_menu
                    if self.user_info:
                        self.user_info['Saldo'] = saldo  # Update saldo di user_info
                    
                    # Memperbarui saldo di Tampilan_main_menu
                    self.parent_window.saldo_display.configure(
                        text=f"Rp. {saldo:,.2f}"
                    )
                else:
                    self.status_label.configure(text="Top-up gagal. Coba lagi.", text_color="red")
            except ValueError:
                self.status_label.configure(text="Input tidak valid.", text_color="red")
        else:
            self.status_label.configure(text="Anda belum login.", text_color="red")

class Custom_Logout(CTkToplevel):
    def __init__(self, master, on_confirm=None, title="Konfirmasi Logout",fg_color=ColorCodes().main_color, width=300, height=150):
        super().__init__(master, fg_color=fg_color)
        self.on_confirm = on_confirm  # Callback untuk logout
        self.geometry(f"{width}x{height}+{master.winfo_x() + 0}+{master.winfo_y() + 290}")
        self.title(title)
        self.overrideredirect(True)
        self.resizable(False, False)

        # Frame utama
        self.main_frame = CTkFrame(self, corner_radius=10,fg_color=ColorCodes().secondary_color)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Label teks konfirmasi
        self.label = CTkLabel(self.main_frame,text="Apakah Anda yakin ingin menutup aplikasi?",font=("Arial", 14), text_color=ColorCodes().third_color,justify="center",wraplength=width - 40)
        self.label.pack(pady=(10, 20))

        # Tombol "Yakin" untuk logout
        self.button_confirm = CTkButton(self.main_frame,text="Ya",command=self.confirm_logout,fg_color="red",hover_color="#ff6666")
        self.button_confirm.pack(side="left", padx=10, expand=True)

        self.button_cancel = CTkButton(self.main_frame,text="Tidak",command=self.cancel_logout,fg_color="green",hover_color="#66cc66")
        self.button_cancel.pack(side="right", padx=10, expand=True)

        # Menahan fokus di frame ini
        self.grab_set()

    def confirm_logout(self):
        self.on_confirm()  # Jalankan callback fungsi logout
        self.master.destroy()

    def cancel_logout(self):
        self.destroy()

class Tampilan_Invoice():
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        self.bg = bg2(self.window)

        self.custom_frame = Custom_scroll_frame(self.window)
        self.custom_frame.place(x=20, y= 120)

        self.custom_text = heading(self.custom_frame, text="Halo")
        self.custom_text.pack(padx=100,pady=0)

        Invoice().pack()

class Invoice (CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10, fg_color="orange", height=100, width=400)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Label Produk
        self.label_product = CTkLabel(self, 
                                          text="Polygon Sepeda MTB\nDual Suspensi Rayz 2", 
                                          font=("Arial", 14, "bold"), 
                                          text_color="black", 
                                          justify="left", 
                                          anchor="w")
        self.label_product.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="w")

        # Label Unit
        self.label_unit = CTkLabel(self, 
                                       text="1 Unit", 
                                       font=("Arial", 12), 
                                       text_color="black", 
                                       justify="left", 
                                       anchor="w")
        self.label_unit.grid(row=1, column=0, padx=(10, 0), pady=(0, 10), sticky="w")

        # Label Harga
        self.label_harga = CTkLabel(self, 
                                        text="Harga 20.000", 
                                        font=("Arial", 12), 
                                        text_color="black", 
                                        anchor="e")
        self.label_harga.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="e")

        # Label Total
        self.label_total = CTkLabel(self, 
                                        text="Total 20.000", 
                                        font=("Arial", 12, "bold"), 
                                        text_color="black", 
                                        anchor="e")
        self.label_total.grid(row=1, column=3, padx=10, pady=(0, 10), sticky="e")



class clearFrame():
    def __init__(self,master):
        self.window = master
        for widget in self.window.winfo_children():
            widget.destroy()

class Invoice:
    def __init__(self, user_info, cart):
        self.user_info = user_info
        self.cart = cart
        self.total_amount = self.calculate_total()
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_id = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4()}"
        self.booking_code = self.generate_booking_code()
        self.total_accumulation = 0  # Track the total accumulation for this transaction

    def calculate_total(self):
        """Calculate the total quantity of items in the cart."""
        return sum(item['quantity'] for item in self.cart)
    
    def calculate_total_cost(self):
        """Calculate the total cost of items in the cart."""
        return sum(item['price'] * item['quantity'] for item in self.cart)

    def generate_booking_code(self):
        """Generate a random booking code (can be alphanumeric)."""
        return f"BOOK-{int(datetime.now().timestamp())}"  # Example format

    def to_dict(self):
        """Convert the invoice data into a dictionary for saving as JSON."""
        items = []
        total_accumulation = 0

        for item in self.cart:
            total_price = item['price'] * item['quantity']
            total_accumulation += total_price
            items.append({
                "number": self.cart.index(item) + 1,
                "product_name": item['product_name'],
                "price": item['price'],
                "amount": item['quantity'],
                "total_price": total_price
            })

        return {
            "id_transaction": self.transaction_id,
            "user_info": {
                "username": self.user_info['Username'],
                "fullname": self.user_info['Fullname'],
                "NIK": self.user_info['NIK'],
                "phone_number": self.user_info['Phone_Number']
            },
            "items": items,
            "total_amount": self.total_amount,
            "total_accumulation": total_accumulation,
            "code_booking": self.booking_code,
            "timestamp": self.timestamp
        }

    def save_to_json(self):
        """Save the invoice to a JSON file."""
        json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/invoices.json"))

        # Ensure the directory exists
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

        # Read existing data if the file already exists
        existing_data = []
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []  # If the file is empty or corrupted

        # Add the current invoice data
        existing_data.append(self.to_dict())

        # Save the updated data back to the file
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)

        print(f"Invoice saved")

class Checkout:
    def __init__(self, cart, user_info):
        self.cart = cart
        self.user_info = user_info
        self.account_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/account.csv"))

    def process_payment(self):
        total_cost = sum(item['price'] * item['quantity'] for item in self.cart)

        # Load user data from account.csv
        user_data = {}
        try:
            with open(self.account_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = row['Username']
                    user_data[username] = row
        except FileNotFoundError:
            raise Exception(f"Account data file not found at: {self.account_file}")

        # Check if the user has enough balance (Saldo)
        username = self.user_info['Username']
        if username not in user_data:
            raise Exception("User not found.")

        user_saldo = float(user_data[username]['Saldo'])  # Current user balance
        if user_saldo < total_cost:
            print(f"Payment failed: Insufficient funds. Required: {total_cost}, Available: {user_saldo}")
            return False

        # Deduct the total cost from the user's balance
        user_data[username]['Saldo'] = str(user_saldo - total_cost)

        # Update the account.csv file with the new balance
        self.update_account_data(user_data)

        print(f"Payment successful. New balance: {user_data[username]['Saldo']}")
        return True

    def update_account_data(self, user_data):
        # Write updated user data back to account.csv
        with open(self.account_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Username', 'Password', 'Phone_Number', 'Saldo', 'Fullname', 'NIK', 'IsLoggedIn']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user, data in user_data.items():
                writer.writerow(data)

    def checkout(self, payment_info=None):  
        if self.process_payment():
            # If payment is successful, create and save the invoice
            invoice = Invoice(self.user_info, self.cart)
            invoice.save_to_json()
            print("Checkout completed successfully. Invoice saved.")
            return invoice
        else:
            # If payment fails, raise an exception
            raise Exception("Payment failed due to insufficient funds.")
        

class product_in_Cart(CTkFrame):
    def __init__(self, master, name_product, unit, price, image_path, cart_item, update_cart_callback, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(
            corner_radius=20,
            border_color=ColorCodes().secondary_color,
            fg_color=ColorCodes().secondary_color,
            height=200,
            bg_color=ColorCodes().main_color,
            border_width=2,
        )

        self.cart_item = cart_item
        self.update_cart_callback = update_cart_callback  # Callback to update the UI
        self.is_checked = IntVar(value=1)  # Checkbox state (1 = checked, 0 = unchecked)

        # Product Image
        self.image_product = Custom_Image(self, image=image_path, width=100, height=80)
        self.image_product.grid(row=0, column=0, rowspan=2, padx=(20, 10), pady=(10, 10))

        # Check Box
        self.chk_box = CTkCheckBox(
            self,
            checkbox_width=20,
            checkbox_height=20,
            width=20,
            text="",
            variable=self.is_checked,
            command=self.toggle_checkbox,  # Call when checkbox is toggled
            hover_color=ColorCodes().main_color,
            fg_color=ColorCodes().main_color,
            checkmark_color=ColorCodes().third_color,
            border_color=ColorCodes().third_color,
        )
        self.chk_box.place(x=10, y=5)

        # Product Name
        self.label_product = CTkLabel(
            self,
            text=name_product,
            text_color=ColorCodes().third_color,
            width=130,
            wraplength=130,
            justify="left",
            anchor="w",
            font=("Arial", 9, "bold"),
        )
        self.label_product.grid(row=0, column=1, padx=(0, 20), pady=(5, 0), sticky="w")

        # Quantity Selector
        self.quantity_selector = QuantitySelector(
            self,
            fg_color=ColorCodes().secondary_color,
        )
        self.quantity_selector.quantity.set(unit)  # Set the initial quantity
        self.quantity_selector.quantity.trace(
            "w", lambda *args: self.update_quantity(self.quantity_selector.quantity.get())
        )  # Trace quantity changes
        self.quantity_selector.grid(row=1, column=1, padx=(0, 20), pady=(5, 0), sticky="w")

        # Price Label
        self.price_label = CTkLabel(
            self,
            anchor="w",
            text=f"Rp. {price}",
            text_color=ColorCodes().third_color,
            font=FontVariables().Paragraph2_Custom_Font,
        )
        self.price_label.grid(row=2, column=1, padx=0, pady=0)

        # Delete Button
        self.delete_button = Custom_Button_Icon(
            self,

            icon= os.path.abspath(os.path.join(os.path.dirname(__file__),"../../assets/icon/delete-button.png")),  # Path to your delete icon
            width=10,
            height=10,
            command=self.delete_item,  # Call the delete method
            fg_color=ColorCodes().secondary_color,
            bg_color=ColorCodes().secondary_color,
            text_color="white",
            hover_color=ColorCodes().main_color,
        )
        self.delete_button.grid(row=2, column=2, padx=(10, 0), sticky="e")

    def toggle_checkbox(self):
        """Toggle the checked state of this product."""
        self.cart_item["checked"] = bool(self.is_checked.get())  # Update cart item state
        self.update_cart_callback()  # Trigger UI update

    def update_quantity(self, new_quantity):
        """Update the quantity of the cart item."""
        self.cart_item["quantity"] = new_quantity
        self.update_cart_callback()  # Call the callback to refresh the UI

    def delete_item(self):
        """Delete this product from the cart."""
        self.delete_callback(self.cart_item)  # Call the delete callback