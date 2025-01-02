########################################################################
## IMPORTS MODULE
########################################################################
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkToplevel, CTkEntry, CTkFont, CTkImage, CTkScrollableFrame
from PIL import Image, ImageTk

################################################################################
## COLOR CODES VARIABLE
################################################################################
class ColorCodes:
    def __init__(self):
        self.main_color = "#fc9803"
        self.secondary_color = "#ffffff"
        self.third_color = "#000000"

################################################################################
## FONT VARIABLES
################################################################################
class FontVariables:
    _instance = None  # Menyimpan instance tunggal

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):  # Cegah inisialisasi ulang
            font_size1 = 32
            font_size2 = 26
            font_size3 = 18
            font_size4 = 12
            font_size5 = 10

            self.Heading1_Custom_Font = CTkFont(family="Roboto Condensed", size=font_size1, weight="bold")
            self.Heading2_Custom_Font = CTkFont(family="Poppins", size=font_size3, weight="bold")
            self.Paragraph1_Custom_Font = CTkFont(family="Poppins",size=font_size4, weight="normal")
            self.Paragraph2_Custom_Font = CTkFont(family="Poppins",size=font_size4,weight="bold")
            self.Paragraph3_Custom_Font = CTkFont(family="Poppins",size=font_size5,weight="bold")
            self.Button_Custom_Font = CTkFont(family="Poppins", size=font_size2, weight="bold")
            self.initialized = True  # Tandai bahwa inisialisasi selesai

################################################################################
## WIDGET  -  WIDGET
################################################################################

class Custom_Frame(CTkFrame):
    def __init__(self, master=None, width=360, height=400, corner_radius=15, bg_color=ColorCodes().main_color ,
                fg_color=ColorCodes().secondary_color, border_color=ColorCodes().secondary_color,border_width=0,
                **kwargs):
        super().__init__(master,border_color=border_color,border_width=border_width,width=width, height=height,
                        corner_radius=corner_radius,bg_color=bg_color, fg_color=fg_color, **kwargs)

        self.configure(fg_color=fg_color,corner_radius=corner_radius,width=width,height=height,border_color=border_color,
                        border_width=border_width)
class Default_Frame(CTkFrame):
    def __init__(self, master=None, width=360, height=640, fg_color=ColorCodes().main_color, **kwargs):
        super().__init__(master,width=width,height=height, fg_color=fg_color, **kwargs)

        self.configure(fg_color=fg_color)

class Custom_Button(CTkButton):
    def __init__(self, master=None, text="Mulai",width=288,height=50,bg_color=ColorCodes().main_color,fg_color=ColorCodes().third_color, 
                font=None,text_color="white", corner_radius=20, hover_color=ColorCodes().main_color, border_width=None, 
                border_color=ColorCodes().third_color,
                **kwargs):
        #Gunakan font default jika tidak diberikan
        border_width = border_width if border_width is not None else 0
        font = font or FontVariables().Button_Custom_Font
        
        super().__init__(master,border_color=border_color,border_width=border_width,text=text,font=font,
                        fg_color=fg_color, bg_color=bg_color,text_color=text_color,corner_radius=corner_radius,hover_color=hover_color,
                        width=width,height=height,**kwargs)

        self.configure(text=text,fg_color=fg_color,border_width = border_width,bg_color=bg_color,
                        border_color=border_color,text_color=text_color,font=font,corner_radius=corner_radius,hover_color=hover_color,width=width)

class Custom_Button_Icon(CTkButton):
    def __init__(self, master=None,text="", icon=None,icon_size=(20, 20), width=10,height=10,command=None,
                hover_color=ColorCodes().secondary_color,bg_color=ColorCodes().secondary_color,fg_color=ColorCodes().secondary_color,
                text_color="white",**kwargs):
        
        image = None
        if icon:
            try:
                img = Image.open(icon)
                img = img.resize(icon_size)
                image = CTkImage(dark_image=img, size=icon_size)
            except Exception as e:
                print(f"Error loading icon: {e}")

        super().__init__(master,text=text,image=image,width=width,height=height,command=command,
                        fg_color=fg_color,hover_color=hover_color,bg_color=bg_color,text_color=text_color,
                        **kwargs)

class Custom_Image(CTkLabel):
    def __init__(self, 
                master=None,
                image=None,
                width=300,
                height=200,
                corner_radius=0,
                text="",
                compound="top",
                font=None,
                text_color=ColorCodes().third_color,
                padx=10,
                pady=10, 
                **kwargs):
        font = font or FontVariables().Heading2_Custom_Font
        # Menginisialisasi widget CTkLabel
        super().__init__(master,
                        corner_radius=corner_radius,
                        text_color=text_color, 
                        padx=padx, 
                        pady=pady,
                        **kwargs)

        # Menentukan gambar (dapat berasal dari URL atau file lokal)
        if image:
            # Jika gambar adalah path file lokal
            try:
                self.image_data = Image.open(image)
            except Exception as e:
                print(f"Error loading image from path: {e}")
                self.image_data = None

            if self.image_data:
                # Menyesuaikan ukuran gambar berdasarkan parameter width dan height
                self.image_data = self.image_data.resize((int(width / 1), int(height / 1)))

                # Mengonversi gambar ke format yang bisa digunakan oleh tkinter
                self.image_tk = ImageTk.PhotoImage(self.image_data)

                # Menampilkan gambar dan teks pada label
                self.configure(image=self.image_tk, compound=compound)
            else:
                print("No valid image found.")

        # Mengonfigurasi properti lainnya seperti padding dan ukuran
        self.configure(
            corner_radius=corner_radius,
            padx=padx,
            pady=pady,
            text=text,
            font= font
        )

class Custom_Text(CTkLabel):
    def __init__(self,
                master=None, 
                text="Default Label Text",
                width=500,
                height=40,
                font=None,
                text_color=ColorCodes().third_color,
                anchor="w",
                justify="left",
                padx=10, 
                pady=10,
                **kwargs):
        font = font or FontVariables().Heading1_Custom_Font
        super().__init__(master,
                        font=font,
                        text=text,
                        width=width,
                        height=height,
                        **kwargs)

        # Mengatur properti default
        self.configure(
            text_color=text_color,        # Mengatur warna teks
            anchor=anchor,                # Mengatur perataan teks
            justify=justify,              # Mengatur perataan multiline
            padx=padx,                    # Padding horizontal
            pady=pady,                    # Padding vertikal
            width = width
        )
        # Menambahkan wraplength agar teks membungkus jika melebihi lebar
        self.configure(wraplength=width)


class Custom_Entry(CTkEntry):
    def __init__(self, 
                master=None, 
                placeholder_text="Masukkan teks...", 
                width=300, 
                height=40, 
                bg_color="#ffffff",
                fg_color=ColorCodes().secondary_color, 
                text_color=ColorCodes().third_color,
                font=None,
                corner_radius=20,
                border_color=ColorCodes().main_color,
                border_width=2,
                show="",
                **kwargs):
        
        font = font or FontVariables().Paragraph1_Custom_Font
        super().__init__(master,
                        width=width,
                        show=show,
                        height=height,
                        **kwargs)
        
        # Mengonfigurasi properti entry
        self.configure(
            placeholder_text=placeholder_text,  # Placeholder default
            fg_color=fg_color,                  # Warna latar belakang
            bg_color=bg_color,                  # Warna latar belakang widget
            text_color=text_color,              # Warna teks
            font=font,                          # Font teks
            show=show,
            corner_radius=corner_radius,        # Radius sudut
            border_color=border_color,          # Warna border
            border_width=border_width,          # Ketebalan border
        )

class Custom_scroll_frame(CTkScrollableFrame):
    def __init__(self,
                master=None,
                width=280,
                height=100,
                bg_color="#ffffff",
                corner_radius= 20,
                border_color=ColorCodes().main_color,
                fg_color=ColorCodes().main_color,
                scrollbar_fg_color=ColorCodes().main_color,
                border_width=4,
                scrollbar_button_color= ColorCodes().third_color,
                scrollbar_button_hover_color = ColorCodes().secondary_color,
                **kwargs):
        
        super().__init__(master, 
                        width=width,
                        border_width =border_width,
                        height=height,
                        scrollbar_button_color = scrollbar_button_color,
                        scrollbar_button_hover_color = scrollbar_button_hover_color,
                        **kwargs)
        
        # Mengonfigurasi properti entry
        self.configure(
            scrollbar_fg_color =scrollbar_fg_color,
            fg_color=fg_color,                  # Warna latar belakang
            bg_color=bg_color,                  # Warna latar belakang widget
            height=height,
            width=width,
            corner_radius=corner_radius,        # Radius sudut
            border_color=border_color,          # Warna border
            border_width=border_width,          # Ketebalan border
        )

class Custom_Messagebox:
    @staticmethod
    def messagebox(title='CustomTKinterMessagebox!', 
                   text='Messagebox is working!', 
                   button_text='OK', 
                   size='320x150+520+300',
                   top=True):
        message_box = CTkToplevel()
        message_box.geometry(size)
        message_box.title(title)
        message_box.resizable(False, False)
        message_box.attributes('-toolwindow', True, '-topmost', top)
        message_box.grab_set()

        l1 = CTkLabel(message_box, text=text)
        l1.pack(pady=30)

        colored_frame = CTkFrame(message_box, height=1)
        colored_frame.pack(side="bottom", fill="x")

        b1 = CTkButton(colored_frame, text=button_text, command=message_box.destroy)
        b1.pack(pady=15)

class Custom_TopLevel(CTkToplevel):
    def __init__(self,master,fg_color = ColorCodes().secondary_color):
        super().__init__(master, fg_color=fg_color)
        self.title("Top Up")
        self.geometry("300x200")
        self.resizable(False,False)

