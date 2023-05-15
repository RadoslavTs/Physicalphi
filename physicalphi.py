import customtkinter as Tk
from login_page import LoginPage, RegisterPage
from dashboard_menu import DashBoardMenu
from PIL import Image
from database_handling import check_login, create_db, get_user_id
from helpers import provide_color_scheme

Tk.set_appearance_mode("light")


class App(Tk.CTk):
    WIDTH = 900
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Physicalphi - your personal physician")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.rowconfigure(0)
        self.columnconfigure(0)
        self.iconbitmap('images/logo.ico')
        self.bg_image = Tk.CTkImage(Image.open('images/bg_gradient.jpg'), size=(self.WIDTH, self.HEIGHT))
        self.bg_image_label = Tk.CTkLabel(self, text='', image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        self.current_username = None
        self.current_user_id = None
        self.color_scheme = provide_color_scheme()

        # Create Login Frame
        self.login_frame = LoginPage(self,
                                     width=300, height=600,
                                     border_width=0)
        self.login_frame.register_button.configure(command=lambda x='register': self.select_frame_by_name(x))
        self.login_frame.login_button.configure(
            command=lambda x=1: self.login_func(self.login_frame.username_entry.get(),
                                                self.login_frame.password_entry.get()))

        # Create Registration Frame
        self.register_frame = RegisterPage(self,
                                           width=300, height=600,
                                           border_width=0)
        self.register_frame.complete_button.configure(command=lambda x=1: self.register_func())
        self.register_frame.back_to_login.configure(command=lambda x='login': self.select_frame_by_name(x))

        # Create main page when logged
        self.dashboard_frame = DashBoardMenu(self, self.current_user_id,
                                             corner_radius=0,
                                             width=200)
        self.dashboard_frame.logoff_button.configure(command=lambda x='login': self.select_frame_by_name(x))

        self.select_frame_by_name("login")
        create_db()

    def select_frame_by_name(self, name, user_id=None):
        if name == 'login':
            self.login_frame.check_login()
            self.login_frame.grid(row=0, column=0, sticky='ns')
        else:
            self.login_frame.grid_forget()
        if name == 'logged_main':
            self.login_frame.clear_login_credentials()
            self.dashboard_frame.get_user_data(user_id)
            self.dashboard_frame.grid(row=0, column=0,
                                      sticky='nswe')
            self.dashboard_frame.pick_category('dashboard_page')
        else:
            self.dashboard_frame.grid_forget()
            self.dashboard_frame.dashboard_page.grid_forget()
        if name == 'register':
            self.register_frame.clear_register_credentials()
            self.register_frame.check_register()
            user_entry = self.login_frame.username_entry.get()
            pass_entry = self.login_frame.password_entry.get()
            if user_entry:
                self.register_frame.username_entry.insert(0, user_entry)
            if pass_entry:
                self.register_frame.password_entry.insert(0, pass_entry)
            self.login_frame.clear_login_credentials()
            self.register_frame.grid(row=0, column=0,
                                     sticky='ns')


        else:
            self.register_frame.grid_forget()

    def login_func(self, username, password):
        self.current_username = self.login_frame.username_entry.get()
        if check_login(username, password):
            self.current_user_id = get_user_id(username)
            self.dashboard_frame.current_userid = self.current_user_id
            return self.select_frame_by_name('logged_main', self.current_user_id)
        else:
            self.login_frame.wrong_credentials()

    def register_func(self):
        self.current_username = self.register_frame.username_entry.get()
        if self.register_frame.register_func():
            self.current_user_id = get_user_id(self.current_username)
            return self.select_frame_by_name('logged_main', self.current_user_id)

    def button_bindings(self, e):
        self.login_frame.check_login()
        self.register_frame.check_register()
