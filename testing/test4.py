import csv
from customtkinter import CTk, CTkToplevel, CTkFrame, CTkLabel, CTkButton, CTkEntry

class AccountManager:
    def __init__(self):
        """
        Inisialisasi class dengan file CSV berisi data akun.
        """
        self.file_path = r"data\account.csv"
        self.user_data = self.load_user_data()

    def load_user_data(self):
        """
        Membaca file CSV dan mengonversinya menjadi dictionary.
        Key adalah kolom 'Username', value adalah dictionary dengan informasi lainnya.
        """
        user_data = {}
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = row['Username']
                    user_data[username] = {
                        'Password': row['Password'],
                        'Phone_Number': row.get('Phone_Number', ''),
                        'Fullname': row.get('Fullname', ''),
                        'NIK': row.get('nik', '')
                    }
        except FileNotFoundError:
            print(f"File {self.file_path} tidak ditemukan.")
        except KeyError as e:
            print(f"Kolom yang diperlukan tidak ditemukan: {e}")
        return user_data

    def get_user_password(self, username):
        """
        Mendapatkan password pengguna berdasarkan username.
        """
        return self.user_data.get(username, {}).get('Password', None)

class Custom_Forgot_Pass(CTkToplevel):
    def __init__(self, master, account_manager, 
                 title="Lupa Password", 
                 text="Masukkan username Anda untuk melihat password", 
                 width=400, 
                 height=250):
        super().__init__(master)

        # Mengatur ukuran dan posisi jendela
        self.geometry(f"{width}x{height}+500+200")
        self.title(title)
        self.resizable(False, False)

        # Menyimpan referensi ke AccountManager
        self.account_manager = account_manager

        # Frame utama
        self.main_frame = CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Label untuk teks utama
        self.label = CTkLabel(self.main_frame, text=text, wraplength=width - 40, justify="center")
        self.label.pack(pady=(10, 10))

        # Input untuk username
        self.entry_username = CTkEntry(self.main_frame, placeholder_text="Masukkan username Anda")
        self.entry_username.pack(pady=(10, 10))

        # Tombol untuk cek password
        self.button_check = CTkButton(
            self.main_frame, 
            text="Lihat Password", 
            command=self.check_password
        )
        self.button_check.pack(pady=(10, 10))

        # Label untuk menampilkan hasil
        self.result_label = CTkLabel(self.main_frame, text="", justify="center")
        self.result_label.pack(pady=(10, 10))

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

# Contoh penggunaan
if __name__ == "__main__":
    # Inisialisasi file CSV
    file_path = r"data\account.csv"  # Pastikan file ini tersedia di direktori yang sama
    account_manager = AccountManager()

    # Inisialisasi aplikasi utama
    app = CTk()
    app.geometry("500x300")

    def open_forgot_password():
        Custom_Forgot_Pass(app, account_manager)

    main_button = CTkButton(app, text="Lupa Password", command=open_forgot_password)
    main_button.pack(pady=50)

    app.mainloop()
