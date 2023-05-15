from tkinter import END
from database_handling import create_new_user
import customtkinter as Tk
from PIL import Image
from template_tkinter_elemenets import StandardButton, StandardEntry

from helpers import provide_color_scheme


class LoginPage(Tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(bg_color=self.color_scheme['outer_frame_bg_color'])
        # add widgets onto the frame...
        self.logo_image = Tk.CTkImage(Image.open("images/logo-sign.png"), size=(260, 147))
        self.logo_image_frame = Tk.CTkLabel(self,
                                            text="",
                                            image=self.logo_image,
                                            compound="center")
        self.logo_image_frame.grid(row=0, column=0,
                                   padx=20, pady=60)

        self.username_entry = StandardEntry(self,
                                            width=200,
                                            placeholder_text="username")
        self.username_entry.grid(row=2, column=0)

        self.password_entry = StandardEntry(self,
                                            width=200,
                                            show="*",
                                            placeholder_text="password")
        self.password_entry.grid(row=3, column=0,
                                 pady=10)

        self.login_button = StandardButton(self,
                                           text="Login",
                                           state='disabled',
                                           width=200)
        self.login_button.grid(row=4, column=0,
                               pady=10)

        self.register_button = StandardButton(self, state='normal',
                                              text="Register",
                                              width=200)
        self.register_button.grid(row=5, column=0,
                                  padx=30, pady=5)

        self.login_info = Tk.CTkLabel(self, text='')
        self.login_info.grid(row=1, column=0,
                             padx=30, pady=(0, 15))

    # function to indicate wrong username or password has been provided
    def wrong_credentials(self):
        self.login_info.configure(text='Invalid credentials!')

    # function to clear all entries (navigational purposes)
    def clear_login_credentials(self):
        self.username_entry.delete(0, END)
        self.username_entry.configure(placeholder_text="username")
        self.password_entry.delete(0, END)
        self.password_entry.configure(placeholder_text="password")
        self.login_info.configure(text='')

    # function to control the state of the buttons
    def check_login(self):
        username, password = self.username_entry.get(), self.password_entry.get()
        if not username or not password:
            self.login_button.configure(state='disabled')
        else:
            self.login_button.configure(state='normal')


# Register page frame
class RegisterPage(Tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.color_scheme = provide_color_scheme()
        # add widgets onto the frame...
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(bg_color=self.color_scheme['outer_frame_bg_color'])

        self.logo_image = Tk.CTkImage(Image.open("images/logo-sign.png"), size=(260, 147))
        self.logo_image_frame = Tk.CTkLabel(self,
                                            text="",
                                            image=self.logo_image,
                                            compound="center")
        self.logo_image_frame.grid(row=0, column=0,
                                   padx=20, pady=60)

        self.username_entry = StandardEntry(self,
                                            width=200,
                                            placeholder_text="username")

        self.username_entry.grid(row=2, column=0)

        self.password_entry = StandardEntry(self,
                                            width=200,
                                            show="*",
                                            placeholder_text="password")
        self.password_entry.grid(row=3, column=0,
                                 pady=10)

        self.first_name_entry = StandardEntry(self,
                                              width=200,
                                              placeholder_text="first name")
        self.first_name_entry.grid(row=4, column=0)

        self.last_name_entry = StandardEntry(self,
                                             width=200,
                                             placeholder_text="last name")
        self.last_name_entry.grid(row=5, column=0,
                                  pady=10)

        self.complete_button = StandardButton(self,
                                              text="Complete registration",
                                              state='normal',
                                              width=200)
        self.complete_button.grid(row=6, column=0,
                                  pady=10)

        self.back_to_login = StandardButton(self,
                                            state='normal',
                                            text="Back to login",
                                            width=200)
        self.back_to_login.grid(row=7, column=0,
                                padx=30, pady=5)

        self.login_info = Tk.CTkLabel(self, text='')
        self.login_info.grid(row=1, column=0,
                             padx=30, pady=(0, 15))

    # function for registration (checking registration input data)
    def register_func(self):
        if create_new_user(self.username_entry.get(), self.password_entry.get(),
                           self.first_name_entry.get(), self.last_name_entry.get()):
            self.clear_register_credentials()
            return True
        else:
            self.login_info.configure(text='user already exists')
            return False

    # function to control the state of the buttons
    def check_register(self):
        username, password, first_name, last_name = self.username_entry.get(), self.password_entry.get(), \
                                                    self.first_name_entry.get(), self.last_name_entry.get
        if not username or not password or not first_name or not last_name:
            self.complete_button.configure(state='disabled')
        else:
            self.complete_button.configure(state='normal')

    # function to clear all entries (navigational purposes)
    def clear_register_credentials(self):
        
        self.username_entry.delete(0, END)
        self.username_entry.configure(placeholder_text="username")
        self.password_entry.delete(0, END)
        self.password_entry.configure(placeholder_text="password")
        self.first_name_entry.delete(0, END)
        self.first_name_entry.configure(placeholder_text="first name")
        self.last_name_entry.delete(0, END)
        self.last_name_entry.configure(placeholder_text="last name")
        self.login_info.configure(text='')
