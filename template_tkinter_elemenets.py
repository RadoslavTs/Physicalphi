import customtkinter as Tk


from helpers import provide_color_scheme


class StandardButton(Tk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['button_color'],
                       text_color=self.color_scheme['button_text_color'],
                       hover_color=self.color_scheme['hover_color'],
                       corner_radius=self.color_scheme['corner_radius'],
                       text_color_disabled=self.color_scheme['button_disabled_color_text'],
                       font=self.color_scheme['text_font'])


class CalculatorButton(Tk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['button_color'],
                       text_color=self.color_scheme['button_text_color'],
                       hover_color=self.color_scheme['hover_color'],
                       corner_radius=self.color_scheme['corner_radius'],
                       text_color_disabled=self.color_scheme['button_disabled_color_text'],
                       font=self.color_scheme['text_font'],
                       width=190)


class StandardEntry(Tk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['entry_color'],
                       text_color=self.color_scheme['button_text_color'],
                       corner_radius=self.color_scheme['corner_radius'],
                       placeholder_text_color=self.color_scheme['entry_placeholder_color'],
                       font=self.color_scheme['text_font'])


class StandardDropDown(Tk.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(button_color=self.color_scheme['button_color'],
                       fg_color=self.color_scheme['entry_color'],
                       text_color=self.color_scheme['button_text_color'],
                       corner_radius=self.color_scheme['corner_radius'],
                       button_hover_color=self.color_scheme['hover_color'],
                       dropdown_hover_color=self.color_scheme['hover_color'],
                       dropdown_text_color=self.color_scheme['button_text_color'],
                       font=self.color_scheme['text_font'],
                       dropdown_font=self.color_scheme['text_font'])


class StandardLabel(Tk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(text_color=self.color_scheme['button_text_color'],
                       font=self.color_scheme['text_font'])
