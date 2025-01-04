import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../widget')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../method')))

########################################################################
## IMPORTS MODULE
########################################################################
from models import bg1, bg2, bg3, bg4, bg5, button1, button2,button3,logo,logo1, heading,heading2, paragraph, entryField, show_hide_button, icon, checkout_Frame, clearFrame, product_in_Cart, product_in_list, Custom_Forgot_Pass, Custom_Topup, Custom_Logout
from widget import ColorCodes,FontVariables, Custom_Frame, Custom_Image, Custom_Button, Custom_scroll_frame, Custom_Messagebox, Custom_Button_Icon
from method import  AccountManager
from models import Checkout
from customtkinter import CTk, CTkToplevel
import csv

class Tampilan_start:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        
        self.main_frame = bg4(self.window)
        self.button_mulai = button1(self.window,"Mulai",ColorCodes().secondary_color, command=lambda: Tampilan_signIn_signUp(self.window)).place(x=35,y=380)
        self.logo = logo(self.window).place(x=100,y=100)
        
class Tampilan_signIn_signUp:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        
        self.main_frame = bg5(self.window)

        self.logo = logo(self.window).place(x=100,y=100)

        self.Selamat_datang = heading(self.window, "Selamat Datang").place(x=20, y=320)
        self.paragraph = paragraph(self.window, "Untuk mengakses semua fitur, mohon daftar (sign up) untuk membuat akun baru. Setelah itu, Anda dapat masuk (sign in) menggunakan kredensial yang telah Anda buat.").place(x=20,y=370)

        self.button_signIn = button1(self.window, "Sign In", ColorCodes().main_color, command=self.show_sign_in).place(x=35, y=500)
        self.button_signUp = button2(self.window, "Sign Up", ColorCodes().main_color, command=self.show_sign_up).place(x=35, y=570)
        
    def show_sign_in(self):
        """Menampilkan tampilan Sign In."""
        clearFrame(self.window)
        Tampilan_signIn(self.window)

    def show_sign_up(self):
        """Menampilkan tampilan Sign Up."""
        clearFrame(self.window)
        Tampilan_signUp(self.window)

class Tampilan_signIn:
    def __init__(self, master):
        self.window = master
        self.window.title("Sign In Page")
        self.window.geometry("360x640+500+20") 
        
        # Background frame
        self.main_frame = bg1(self.window)

        # Logo
        self.logo = logo1(self.window)
        self.logo.place(x=250, y=0)

        # Tombol kembali
        self.previous = icon(self.window, 20, 10, 20, 20,ColorCodes().main_color, r"assets\icon\arrow.png", self.go_back)

        # Heading dan paragraf
        self.sign_in_heading = heading(self.window, "Sign In")
        self.sign_in_heading.place(x=20, y=50)

        self.paragraph = paragraph(self.window, "Silahkan isi formulir di bawah ini untuk masuk")
        self.paragraph.place(x=20, y=100)

        # Input fields
        self.username_entry = entryField(self.window, placeholder="Username", show="")
        self.username_entry.place(x=30, y=250)

        self.password_entry = entryField(self.window, placeholder="Password", show="*")
        self.password_entry.place(x=30, y=300)

        # Tombol show/hide password
        self.show_hide_button = show_hide_button(self.window, target=self.password_entry)
        self.show_hide_button.place(x=255, y=305)

        self.lupa_password = Custom_Button(self.window, text="Lupa Password", height=10,command=self.show_forgot_password, width=100, fg_color=ColorCodes().secondary_color, bg_color=ColorCodes().secondary_color, text_color=ColorCodes().third_color, hover_color = ColorCodes().secondary_color, font=FontVariables().Paragraph1_Custom_Font)
        self.lupa_password.place(x=205, y=340)
        # Tombol sign in
        self.sign_in_button = button1(self.window, "Sign In", ColorCodes().secondary_color, command=self.sign_in)
        self.sign_in_button.place(x=35, y=500)
        
    def go_back(self):
        """Kembali ke tampilan Sign Up."""
        clearFrame(self.window)
        Tampilan_signIn_signUp(self.window)

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        account_manager = AccountManager()
        if account_manager.sign_in(username, password):
            Custom_Messagebox.messagebox("Success", "Login berhasil. Selamat datang, " + username + "!")
            
            # Retrieve user info after successful login
            user_info = account_manager.get_user_info()  # No need to pass username now
            
            Tampilan_account(self.window, user_info)  # Pass user_info to the profile page
        else:
            Custom_Messagebox.messagebox("Error", "Username atau Password salah!")
    
    def show_forgot_password(self):
        """Tampilkan tampilan lupa password."""
        Custom_Forgot_Pass(self.window, AccountManager())

class Tampilan_signUp:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20") 
        self.main_frame = bg1(self.window)

        self.logo = logo1(self.window)
        self.logo.place(x=250, y=0)

        self.previous = icon(self.window, 20, 10, 20, 20, ColorCodes().main_color, r"assets\icon\arrow.png", self.go_back)
        self.Sign_In = heading(self.window, "Sign Up")
        self.Sign_In.place(x=20, y=50)
        self.paragraph = paragraph(self.window, "Silahkan isi formulir di bawah ini untuk daftar")
        self.paragraph.place(x=20, y=100)

        self.fullname = entryField(self.window, "Fullname", "")
        self.fullname.place(x=30, y=200)
        self.phonenumber = entryField(self.window, "Phone Number", "")
        self.phonenumber.place(x=30, y=250)
        self.nik = entryField(self.window, "NIK", "")
        self.nik.place(x=30, y=300)
        self.username = entryField(self.window, "Username", "")
        self.username.place(x=30, y=350)
        self.password_entry = entryField(self.window, placeholder="Password", show="*")
        self.password_entry.place(x=30, y=400)

        self.show_hide_button = show_hide_button(self.window, target=self.password_entry)
        self.show_hide_button.place(x=255, y=405)

        self.button_signUp = button2(self.window, "Sign Up", bg_color=ColorCodes().secondary_color, command=self.sign_up)
        self.button_signUp.place(x=35, y=500)

    def go_back(self):
        """Kembali ke tampilan Sign Up."""
        clearFrame(self.window)
        Tampilan_signIn_signUp(self.window)

    def sign_up(self):
        self.account_manager = AccountManager()
        """Logika untuk proses Sign Up."""
        fullname = self.fullname.get()
        nik = self.nik.get()
        phone_number = self.phonenumber.get()
        username = self.username.get()
        password = self.password_entry.get()

        if self.account_manager.sign_up(username, password, phone_number, fullname, nik):
            Custom_Messagebox.messagebox(title="Success", text="Akun berhasil dibuat!")
            
            # Retrieve user info after successful sign-up
            user_info = self.account_manager.get_user_info(username)  # Get user info using the updated method
            
            # Navigate to the profile page with user info
            clearFrame(self.window)  # Clear the current frame
            Tampilan_account(self.window, user_info)  # Pass user_info to the profile page

class Tampilan_main_menu:
    def __init__(self, master,user_info=None):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")
        self.user_info = user_info
        self.main_frame = bg3(self.window)
        self.account_manager = AccountManager()
        self.isLoggedIn = self.account_manager.load_user_data()
        self.logged_in_users = [username for username, data in self.isLoggedIn.items() if data['IsLoggedIn']]
        self.current_user = self.logged_in_users[0]  # Ambil username pertama yang login
        saldo = self.account_manager.user_data[self.current_user]['Saldo']

        self.logo = logo(self.window)
        self.logo.place(x=100, y=0)

        self.frame1 = Custom_Frame(self.window,fg_color=ColorCodes().main_color,bg_color=ColorCodes().secondary_color,corner_radius=20,height=180,width=300,)
        self.frame1.place(x=30, y=90)

        self.Saldo_label = heading(self.frame1, "Saldo")
        self.Saldo_label.place(x=20, y=30)
        
        self.saldo_display = heading(self.frame1, f"Rp. {saldo:,.2f}")
        self.saldo_display.place(x=20, y=80)

        self.top_up = button3(self.frame1,"Top Up",bg_color=ColorCodes().main_color,image=r"assets\icon\plus-activate.png",command=self.go_topUp,)
        self.top_up.place(x=130, y=120)

        self.home_icon = icon(self.window, 30, 570, 60, 60,ColorCodes().main_color, r"assets\icon\home-activate.png", self.go_home)
        self.cart_icon = icon(self.window, 130, 570, 60, 60,ColorCodes().main_color, r"assets\icon\grocery-store.png", self.go_cart)
        self.account_icon = icon(self.window, 250, 570, 60, 60,ColorCodes().main_color, r"assets\icon\account.png", self.go_account)

        self.Peminjaman = button1(self.window, "Peminjaman", ColorCodes().secondary_color, command=self.go_Peminjaman)
        self.Peminjaman.place(x=35, y=400)
        self.Pengembalian = button2(self.window, "Pengembalian", ColorCodes().secondary_color, command=self.go_Pengembalian)
        self.Pengembalian.place(x=35, y=470)

        self.logout = Custom_Button_Icon(self.window, icon=r"assets\icon\log-out.png", command=self.confirm_logout)
        self.logout.place(x=10,y=10)
        # Buat instance AccountManager
        self.account_manager = AccountManager()
        # Buat instance TopUp
        
    def go_home(self):
        clearFrame(self.window)
        Tampilan_main_menu(self.window, self.user_info)

    def go_cart(self):
        clearFrame(self.window)
        Tampilan_cart(self.window, self.user_info)

    def go_account(self):
        clearFrame(self.window)
        Tampilan_account(self.window, self.user_info)

    def go_Peminjaman(self):
        clearFrame(self.window)
        Tampilan_Peminjaman(self.window, self.user_info)

    def go_Pengembalian(self):
        clearFrame(self.window)
        Tampilan_Pengembalian(self.window)

    def go_topUp(self):
        top_up_window = Custom_Topup(self.window, self.user_info)
        top_up_window.parent_window = self
    def go_logout(self):
        account_manager = AccountManager()
        account_manager.logout()
        Tampilan_signIn(self.window)

    def confirm_logout(self):
        Custom_Logout(self.window, self.go_logout)
        

class Tampilan_cart:
    def __init__(self, master, user_info=None):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")
        self.user_info = user_info
        
        # Initialize cart_items
        self.cart_items = []

        # Background Frame
        self.main_frame = bg3(self.window)

        # Heading
        self.My_Cart = heading(self.window, "My Cart", fg_color=ColorCodes().secondary_color)
        self.My_Cart.grid(row=0, column=0, padx=(20, 10), pady=5)

        # Scroll Frame
        self.scroll_frame = Custom_scroll_frame(self.window, height=320, width=295)
        self.scroll_frame.grid(row=1, column=0, padx=(15, 10), pady=10)

        # Checkout Frame
        self.checkout_frame = checkout_Frame(self.window, self.cart_items, self.user_info)
        self.checkout_frame.grid(row=2, column=0, padx=(10, 10), pady=10)

        # Load cart items
        self.tampilkan_product_cart()

        # Icon navigation
        self.home_icon = icon(self.window, 30, 570, 60, 60, ColorCodes().main_color, r"assets\icon\home.png", self.go_home)
        self.cart_icon = icon(self.window, 130, 570, 60, 60, ColorCodes().main_color, r"assets\icon\grocery-store-activate.png", self.go_cart)
        self.account_icon = icon(self.window, 250, 570, 60, 60, ColorCodes().main_color, r"assets\icon\account.png", self.go_account)

    def tampilkan_product_cart(self):
        """Load and display products in the cart."""
        self.data = r"data\cart.csv"
        account_manager = AccountManager()
        username_logged_in = account_manager.get_logged_in_user()

        if not username_logged_in:
            print("Anda harus login terlebih dahulu.")
            Custom_Messagebox.messagebox("Error", "Anda harus login terlebih dahulu untuk melihat keranjang.")
            return False

        with open(self.data, mode='r', encoding='utf-8') as file:
            # Read the CSV file
            csv_reader = csv.DictReader(file, delimiter=';')

            # Filter products in the cart for the logged-in user
            filtered_products = [
                row for row in csv_reader
                if row['Username'] == username_logged_in
                and row['IsLoggedIn'].strip().lower() == 'true'
                and row['on_cart'].strip().lower() == 'true'
            ]

        # Clear existing cart items
        self.cart_items = []

        # Display filtered products
        for product in filtered_products:
            cart_item = {
                'product_name': product["product_name"],
                'price': float(product["price"]),
                'quantity': int(product["qty"]),
                'link': product["link"],
                'checked': True,  # Default to checked
            }
            self.cart_items.append(cart_item)
            product_widget = product_in_Cart(
                self.scroll_frame,
                name_product=product["product_name"],
                price=product["price"],
                unit=product["qty"],
                image_path=product["link"],
                cart_item=cart_item,
                update_cart_callback=self.update_checkout_frame,  # Pass the callback
            )
            product_widget.pack(padx=(0, 0), pady=10, anchor="w")

        # Update the checkout frame
        self.update_checkout_frame()

    def update_checkout_frame(self):
        """Update the checkout frame with the latest cart data."""
        self.checkout_frame.cart = self.cart_items  # Update the cart in checkout_frame
        self.checkout_frame.value_terpilih.configure(
            text=f"{self.checkout_frame.calculate_total_quantity()} Unit"
        )
        self.checkout_frame.value_harga.configure(
            text=f"Rp. {self.checkout_frame.calculate_total_price():,.2f}"
        )

    def get_cart(self):
        """Return the cart items for checkout."""
        return self.cart_items

    def go_home(self):
        """Navigate to the home screen."""
        clearFrame(self.window)
        Tampilan_main_menu(self.window, self.user_info)

    def go_cart(self):
        """Reload the cart screen."""
        clearFrame(self.window)
        Tampilan_cart(self.window, self.user_info)

    def go_account(self):
        """Navigate to the account screen."""
        clearFrame(self.window)
        Tampilan_account(self.window, self.user_info)

class Tampilan_account():
    def __init__(self, master, user_info=None):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")
        self.user_info = user_info
        self.main_frame = bg3(self.window)
        
        self.profile = Custom_Image(self.window, text="@" +  (self.user_info.get("Username") if self.user_info.get("Username") else "Guest"), width=130, height=130, image=r"assets\icon\photo-profile.png", bg_color=ColorCodes().secondary_color)
        self.profile.grid(row=0, column=0, padx=50, pady=0)
        
        self.frame1 = Custom_Frame(self.window, fg_color=ColorCodes().main_color, bg_color=ColorCodes().secondary_color, corner_radius=20, height=350, width=100)
        self.frame1.grid(row=2, column=0, padx=(25, 10), pady=0)
        
        self.frame1.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        self.frame1.grid_columnconfigure(0, weight=0)
        
        self.account_profile = heading2(master=self.frame1, anchor="center", text="Account Profile")
        self.account_profile.grid(row=0, column=0, padx=5, pady=(10, 0))
        
        self.nik_label = heading2(master=self.frame1, text="NIK")
        self.nik_label.grid(row=1, column=0, padx=5, pady=0)
        self.entry_nik = entryField(self.frame1, state="disabled", placeholder=self.user_info.get("NIK", ""),bg_color=ColorCodes().main_color)
        self.entry_nik.grid(row=2, column=0, padx=5, pady=0)
        
        self.fullname_label = heading2(master=self.frame1, text="Fullname")
        self.fullname_label.grid(row=3, column=0, padx=5, pady=0)
        self.entry_fullname = entryField(self.frame1, state="disabled", placeholder=self.user_info.get("Fullname", ""), bg_color=ColorCodes().main_color)
        self.entry_fullname.grid(row=4, column=0, padx=5, pady=0)
        
        self.phone_number_label = heading2(master=self.frame1, text="Phone Number")
        self.phone_number_label.grid(row=5, column=0, padx=5, pady=0)
        self.entry_phone = entryField(self.frame1,state="disabled",placeholder=self.user_info.get("Phone_Number", ""),bg_color=ColorCodes().main_color,)
        self.entry_phone.grid(row=6, column=0, padx=5, pady=(0, 10))

        self.home_icon = icon(self.window, 30, 570, 60, 60,ColorCodes().main_color, "assets/icon/home.png", self.go_home)
        self.cart_icon = icon(self.window, 130, 570, 60, 60,ColorCodes().main_color, r"assets\icon\grocery-store.png", self.go_cart)
        self.account_icon = icon(self.window, 250, 570, 60, 60,ColorCodes().main_color, r"assets\icon\account-activate.png", self.go_account)
        
    def go_home(self):
        clearFrame(self.window)
        Tampilan_main_menu(self.window, self.user_info)
    
    def go_cart(self):
        clearFrame(self.window)
        Tampilan_cart(self.window, self.user_info)

    def go_account(self):
        clearFrame(self.window)
        Tampilan_account(self.window, self.user_info)
    
class Tampilan_Peminjaman:
    def __init__(self, master, user_info= None):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")
        self.user_info = user_info

        self.main_frame= bg2(self.window)

        self.previous = icon(self.window, 20, 10,20,20,ColorCodes().main_color, r"assets\icon\arrow.png", self.go_back)
        # Heading
        self.Peminjaman = heading(self.window, "Peminjaman", fg_color=ColorCodes().main_color)
        self.Peminjaman.grid(row=0, column=0, padx=(70, 10), pady=0)

        # Scroll Frame
        self.scroll_frame = Custom_scroll_frame(self.window, height=450)
        self.scroll_frame.grid(row=1, column=0,padx=(0, 20), pady=90)

        self.tampilkan_product()

    def tampilkan_product(self):
        account_manager = AccountManager()
        username_logged_in = account_manager.get_logged_in_user()
        print(username_logged_in)
        self.data = r"data\product.csv"
        with open(self.data, mode='r') as file:
            # Membaca file CSV
            csv_reader = csv.reader(file, delimiter=';')
            header = next(csv_reader)  # Ambil header
            data_dict = [dict(zip(header, row)) for row in csv_reader]  # Parse data ke dictionary

        # Menampilkan produk di dalam scroll_frame
        for product in data_dict:
            product_number = int(product["number"])  # Ambil nomor produk

            # Fungsi unik untuk tombol Add to Cart
            def add_to_cart_function(prod_num=product_number):  # Gunakan default argumen untuk binding
                AccountManager().add_to_cart(prod_num)
            # Menampilkan produk di dalam scroll_frame
            self.product = product_in_list(self.scroll_frame, product["product_name"],f"Rp. {product["price"]}" , product["status"], product["qty"], product["link"],  add_to_cart_function=add_to_cart_function)
            self.product.pack(padx=(0,10), pady=5,anchor="w")

    def go_back(self):
        clearFrame(self.window)
        Tampilan_main_menu(self.window)
    
    
class Tampilan_Pengembalian:
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")

        self.main_frame= bg2(self.window)
    
        self.previous = icon(self.window, 20, 10,20,20,ColorCodes().main_color, r"assets\icon\arrow.png", self.go_back)
        
    def go_back(self):
        clearFrame(self.window)
        Tampilan_main_menu(self.window)


class Top_level_topUp(CTkToplevel):
    def __init__(self, master):
        self.window = master
        self.window.title("Icon Inside Button")
        self.window.geometry("360x640+500+20")
        
        self.main_frame = bg1(self.window)
