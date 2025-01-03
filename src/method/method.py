import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../widget')))

import csv
from widget import Custom_Messagebox
from datetime import datetime 

class AccountManager:
    def __init__(self):
        self.account_file = r"data\account.csv"
        self.history_file = r"data\topup_history.csv"  # File untuk riwayat top-up
        self.product_file = r"data\product.csv"
        self.cart_file = r"data\cart.csv"
        self.user_data = self.load_user_data()
        self.current_user = None  # Menyimpan pengguna yang sedang login
        self.username = None
        self.nik = None
        self.phone_number = None
        self.fullname = None

    def load_user_data(self):
        user_data = {}
        try:
            with open(self.account_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = row['Username']
                    user_data[username] = {
                        'Password': row['Password'],
                        'Phone_Number': row.get('Phone_Number', ''),
                        'Saldo': float(row.get('Saldo', 0)),  # Pastikan saldo dimuat sebagai float
                        'Fullname': row.get('Fullname', ''),
                        'NIK': row.get('NIK', ''),
                        'IsLoggedIn': row.get('IsLoggedIn', 'False') == 'True',  # Konversi ke boolean
                    }
        except FileNotFoundError:
            print(f"File {self.account_file} tidak ditemukan.")
        return user_data

    def update_login_status(self, username=None, is_logged_in=False):
        """
        Memperbarui status login pengguna di file CSV.
        Jika username adalah None, semua pengguna akan di-set ke False.
        """
        updated_rows = []
        for user, data in self.user_data.items():
            if user == username:
                data['IsLoggedIn'] = is_logged_in  # Update pengguna yang dimaksud
            else:
                data['IsLoggedIn'] = False  # Set pengguna lain ke False
            updated_rows.append({
                "Username": user,
                "Password": data['Password'],
                "Phone_Number": data['Phone_Number'],
                "Saldo": data['Saldo'],
                "Fullname": data['Fullname'],
                "NIK": data['NIK'],
                "IsLoggedIn": str(data['IsLoggedIn']),
            })

        # Tulis ulang data ke file CSV
        with open(self.account_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Username", "Password", "Phone_Number", "Saldo", "Fullname", "NIK", "IsLoggedIn"])
            writer.writeheader()
            writer.writerows(updated_rows)
    
    def update_cart_login_status(self, username=None, is_logged_in=False):
        """
        Memperbarui status 'IsLoggedIn' di file cart.csv sesuai dengan username yang diberikan.
        Jika username adalah None, semua status 'IsLoggedIn' akan di-set ke False.
        """
        updated_rows = []
        # Buka file CSV dengan pemisah ';'
        with open(self.cart_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')  # Tentukan pemisah ';'
            rows = list(reader)

        # Update baris yang sesuai dengan username
        for row in rows:
            if row['Username'] == username:
                row['IsLoggedIn'] = 'TRUE' if is_logged_in else 'FALSE'  # Ubah menjadi TRUE jika login
            else:
                row['IsLoggedIn'] = 'FALSE'  # Set pengguna lain ke FALSE
            updated_rows.append(row)

        # Tulis kembali data yang sudah diperbarui ke file CSV
        with open(self.cart_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Username", "number", "product_name", "price", "qty", "link", "on_cart", "IsLoggedIn"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')  # Tentukan pemisah ';'
            writer.writeheader()
            writer.writerows(updated_rows)

    def sign_in(self, username, password):
        """Metode untuk memverifikasi dan login pengguna."""
        user = self.user_data.get(username)
        if user and user['Password'] == password:
            # Update status login di file CSV
            self.update_login_status(username, is_logged_in=True)
            self.update_cart_login_status(username, is_logged_in=True)
            # Tandai pengguna ini sebagai aktif di runtime
            self.current_user = username
            self.user_data[username]['IsLoggedIn'] = True  # Update data login pengguna
            print(f"Login berhasil. Selamat datang, {username}!")
            return True
        print("Login gagal. Username atau password salah.")
        return False

    def sign_up(self, username, password, fullname, phone_number, nik):
        """
        Fungsi untuk mendaftarkan pengguna baru.
        """
        # Validasi input
        if username in self.user_data:
            Custom_Messagebox.messagebox("Error", "username sudah digunakan coba gunakan yang lain")
            return False

        if not username or not password or not fullname or not phone_number or not nik:
            Custom_Messagebox.messagebox("Error", "Semua kolom harus terisi")
            return False

        if len(password) < 6:
            Custom_Messagebox.messagebox("Error", "Password Harus Terdiri dari 6 karakter")
            return False

        if not nik.isdigit() or len(nik) != 16:
            Custom_Messagebox.messagebox("Error", "NIK harus terdiri dari 16 digit angka")
            return False

        # Tambahkan pengguna baru ke data runtime
        self.user_data[username] = {
            'Password': password,
            'Phone_Number': phone_number,
            'Saldo': 0.0,
            'Fullname': fullname,
            'NIK': nik,
            'IsLoggedIn': False,
        }

        # Simpan ke file CSV
        new_user = {
            "Username": username,
            "Password": password,
            "Phone_Number": phone_number,
            "Saldo": 0.0,
            "Fullname": fullname,
            "NIK": nik,
            "IsLoggedIn": 'False',
        }
        with open(self.account_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Username", "Password", "Phone_Number", "Saldo", "Fullname", "NIK", "IsLoggedIn"])
            if file.tell() == 0:  # Jika file kosong, tulis header
                writer.writeheader()
            writer.writerow(new_user)

        print(f"Registrasi berhasil. Selamat datang, {fullname}!")
        return True

    def logout(self):
        # Set semua IsLoggedIn menjadi False
        for username in self.user_data:
            self.user_data[username]['IsLoggedIn'] = False

        # Tulis ulang ke file account.csv
        with open(self.account_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Username", "Password", "Phone_Number", "Saldo", "Fullname", "NIK", "IsLoggedIn"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for username, data in self.user_data.items():
                writer.writerow({
                    "Username": username,
                    "Password": data['Password'],
                    "Phone_Number": data['Phone_Number'],
                    "Saldo": data['Saldo'],
                    "Fullname": data['Fullname'],
                    "NIK": data['NIK'],
                    "IsLoggedIn": str(data['IsLoggedIn']),
                })
        
            # Set semua IsLoggedIn di cart.csv menjadi False
        updated_cart = []
        try:
            with open(self.cart_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    row['IsLoggedIn'] = 'FALSE'  # Ubah IsLoggedIn menjadi FALSE
                    updated_cart.append(row)
        except FileNotFoundError:
            print(f"File {self.cart_file} tidak ditemukan.")

        # Tulis ulang ke file cart.csv
        with open(self.cart_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Username", "number", "product_name", "price", "qty", "link", "on_cart", "IsLoggedIn"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(updated_cart)
            # Clear current_user
        print("Semua pengguna telah logout.")
        self.current_user = None

    def top_up(self, amount):
        self.isLoggedIn = self.load_user_data()
        self.logged_in_users = [username for username, data in self.isLoggedIn.items() if data['IsLoggedIn']]

        if not self.logged_in_users:
            print("Anda harus login terlebih dahulu.")
            return False

        self.current_user = self.logged_in_users[0]  # Ambil pengguna pertama yang login

        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Jumlah top-up harus berupa angka positif.")
            return False

        # Akses data saldo pengguna yang sedang login
        current_saldo = self.user_data[self.current_user]['Saldo']
        new_saldo = current_saldo + amount

        # Perbarui saldo di runtime
        self.user_data[self.current_user]['Saldo'] = new_saldo

        # Perbarui saldo di file CSV
        self.update_saldo(self.current_user, new_saldo)

        # Simpan riwayat top-up
        self.save_topup_history(self.current_user, current_saldo, new_saldo, amount, 'Topup')  # Pastikan semua parameter dimasukkan)

        print(f"Top up berhasil. Saldo baru: {new_saldo}")
        return True

    def update_saldo(self, username, new_saldo):
        self.user_data[username]['Saldo'] = new_saldo  # Update saldo di runtime
        self.update_login_status(username, is_logged_in=True)  # Pastikan status login tetap True
        print(f"Saldo pengguna {username} berhasil diperbarui.")

    def save_topup_history(self, username,saldo_awal, amount,saldo_akhir, type_transaksi):
        # Fungsi untuk menyimpan riwayat top-up ke file CSV
        timestamp = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
        with open(self.history_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Jika file kosong, tulis header
                writer.writerow(["Username", "Saldo_awal", "Saldo_akhir", "Amount", "Type", "Timestamp"])
            writer.writerow([username, saldo_awal, saldo_akhir, amount, type_transaksi, timestamp])
        print(f"Riwayat top-up untuk {username} berhasil disimpan.")

    def get_user_info(self):
        if self.current_user:
            return {
                "Username": self.username,
                "NIK": self.nik,
                "Phone_Number": self.phone_number,
                "Fullname": self.fullname
            }
        print("Tidak ada pengguna yang sedang login.")
        return None
    
    def get_user_password(self, username):
        """
        Mengambil password pengguna berdasarkan username.
        """
        user = self.user_data.get(username)
        if user:
            return user['Password']
        print("Username tidak ditemukan.")
        return None
    
    def get_user_balance(self, username):
        """Mendapatkan saldo pengguna berdasarkan username."""
        user = self.user_data.get(username)
        if user:
            return user['Saldo']
        return 0  # Jika pengguna tidak ditemukan, kembalikan saldo 0
    
    def login(self, username):
        """Set pengguna yang sedang login."""
        self.current_user = username
        print(f"Login berhasil sebagai {username}")

    def get_logged_in_user(self):
        for username, data in self.user_data.items():
            if data['IsLoggedIn']:
                return username
        return None

    def add_to_cart(self, product_number):
        # Ambil username yang sedang login
        username_logged_in = self.get_logged_in_user()
        
        if not username_logged_in:
            print("Anda harus login terlebih dahulu.")
            return False

        print(f"Menambahkan produk dengan nomor {product_number} untuk user {username_logged_in}")

        product_found = False
        selected_product = None

        try:
            with open(self.product_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                print("Header CSV:", reader.fieldnames)

                for row in reader:
                    print("Row:", row)
                    if row['number'] == str(product_number):
                        product_found = True
                        # Hanya pilih kolom yang diperlukan (tanpa status)
                        selected_product = {
                            "number": row["number"],
                            "product_name": row["product_name"],
                            "price": row["price"],
                            "qty": row["qty"],
                            "link": row["link"],
                            "Username": username_logged_in,  # Tambahkan username yang sedang login
                            "on_cart": "TRUE",
                            "IsLoggedIn": "TRUE",  # Tandai bahwa data ini milik user yang login
                        }
                        print("Produk ditemukan:", selected_product)
                        break
        except FileNotFoundError:
            print(f"File {self.product_file} tidak ditemukan.")
            return False

        if not product_found:
            print(f"Produk dengan nomor {product_number} tidak ditemukan.")
            return False

        # Tambahkan produk ke cart.csv
        try:
            with open(self.cart_file, mode='a', encoding='utf-8', newline='') as file:
                fieldnames = ['Username', 'number', 'product_name', 'price', 'qty', 'link', 'on_cart', 'IsLoggedIn']
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

                if file.tell() == 0:  # Tambahkan header jika file kosong
                    writer.writeheader()

                writer.writerow(selected_product)
                print(f"Produk {selected_product['product_name']} berhasil ditambahkan ke keranjang.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menulis ke cart.csv: {e}")
            return False

        return True

class list_product:
    def __init__(self):
        self.file_path = r"data\product.csv"
        self.groupped_data = []

        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';')
            headers = next(reader)  
            for row in reader:
                row_data = dict(zip(headers, row))
                self.groupped_data.append(row_data)
