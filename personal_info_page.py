import customtkinter as Tk
from database_handling import update_user_details, update_meas, get_user_data
from helpers import calculateAge, provide_color_scheme
from template_tkinter_elemenets import StandardButton, StandardEntry, StandardDropDown, StandardLabel


class PersonalInfo(Tk.CTkFrame):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, minsize=30)
        self.grid_columnconfigure(0, minsize=30)
        self.pack_propagate(0)
        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(bg_color=self.color_scheme['outer_frame_bg_color'])

        self.user_id = user_id
        self.update_top_level = None
        self.user_data = None

        self.columnconfigure(5, minsize=140)

        # Main frames
        self.info_frame = Tk.CTkFrame(self, fg_color=self.color_scheme['menu_color'], corner_radius=5)
        self.info_frame.rowconfigure(0, minsize=20)
        self.info_frame.columnconfigure(0, minsize=20)
        self.info_frame.pack(expand=True,
                             anchor='nw',
                             side='left',
                             fill='both',
                             padx=5, pady=5)

        self.control_frame = Tk.CTkFrame(self, fg_color=self.color_scheme['menu_color'], corner_radius=5)
        self.control_frame.rowconfigure(0, minsize=25)
        self.control_frame.columnconfigure(0, minsize=25)
        self.control_frame.pack(expand=True,
                                anchor='ne',
                                side='right',
                                fill='both',
                                padx=5, pady=5)

        # Elements
        self.full_name_label = StandardLabel(self.info_frame,
                                             text='',
                                             width=150,
                                             font=(self.color_scheme['text_font'][0], 130))
        self.full_name_label.configure(font=(self.color_scheme['text_font'][0], 30))
        self.full_name_label.grid(row=1, column=1,
                                  padx=10, pady=10,
                                  columnspan=2,
                                  sticky='w')

        self.dob_frame = Tk.CTkFrame(self.info_frame)
        self.dob_frame.grid(row=2, column=1, columnspan=2, pady=5)
        self.dob_label_info = StandardLabel(self.dob_frame,
                                            text='Date of birth',
                                            width=150,
                                            font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.dob_label_info.grid(row=0, column=0,
                                 padx=10, pady=8,
                                 sticky='w')

        self.dob_label = StandardLabel(self.dob_frame,
                                       text='Update your info',
                                       width=150,
                                       font=(self.color_scheme['text_font'][0], 15), anchor='w', justify='left')
        self.dob_label.grid(row=0, column=1,
                            padx=10, pady=8)

        self.sex_frame = Tk.CTkFrame(self.info_frame)
        self.sex_frame.grid(row=3, column=1, columnspan=2, pady=5)
        self.sex_label_info = StandardLabel(self.sex_frame,
                                            text='Sex',
                                            width=150,
                                            font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.sex_label_info.grid(row=0, column=0,
                                 padx=10, pady=10,
                                 sticky='e')

        self.sex_label = StandardLabel(self.sex_frame,
                                       text='Update your info',
                                       width=150, font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.sex_label.grid(row=0, column=1,
                            padx=10, pady=10)

        self.height_frame = Tk.CTkFrame(self.info_frame)
        self.height_frame.grid(row=4, column=1, columnspan=2, pady=5)
        self.height_label_info = StandardLabel(self.height_frame,
                                               text='Height',
                                               width=150,
                                               font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.height_label_info.grid(row=0, column=0,
                                    padx=10, pady=10,
                                    sticky='e')

        self.height_label = StandardLabel(self.height_frame,
                                          text='Update your info',
                                          width=150, font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.height_label.grid(row=0, column=1,
                               padx=10, pady=10)

        self.weight_frame = Tk.CTkFrame(self.info_frame)
        self.weight_frame.grid(row=5, column=1, columnspan=2, pady=5)
        self.weight_label_info = StandardLabel(self.weight_frame,
                                               text='Weight',
                                               width=150,
                                               font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.weight_label_info.grid(row=0, column=0,
                                    padx=10, pady=10,
                                    sticky='e')

        self.weight_label = StandardLabel(self.weight_frame,
                                          text='Add weight measurement',
                                          width=150,
                                          font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.weight_label.grid(row=0, column=1,
                               padx=10, pady=10)

        self.blood_type_frame = Tk.CTkFrame(self.info_frame)
        self.blood_type_frame.grid(row=6, column=1, columnspan=2, pady=5)
        self.bloodtype_label_info = StandardLabel(self.blood_type_frame,
                                                  text='Blood Type',
                                                  width=150,
                                                  font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.bloodtype_label_info.grid(row=0, column=0,
                                       padx=10, pady=10,
                                       sticky='e')

        self.bloodtype_label = StandardLabel(self.blood_type_frame,
                                             text='Update your info',
                                             width=150,
                                             font=(self.color_scheme['text_font'][0], 15), anchor='w')
        self.bloodtype_label.grid(row=0, column=1,
                                  padx=10, pady=10)

        self.update_dob_button = StandardButton(self.control_frame,
                                                text='Update personal info',
                                                width=210,
                                                command=lambda x='dob': self.open_update(x))
        self.update_dob_button.grid(row=1, column=1,
                                    padx=10, pady=10)

        self.add_weight_button = StandardButton(self.control_frame,
                                                text='Add Weight Measurement',
                                                command=lambda x='WEIGHT': self.open_update(x),
                                                width=210)
        self.add_weight_button.grid(row=2, column=1,
                                    padx=10, pady=10)

        self.add_height_button = StandardButton(self.control_frame,
                                                text='Add Height Measurement',
                                                command=lambda x='HEIGHT': self.open_update(x),
                                                width=210)
        self.add_height_button.grid(row=3, column=1,
                                    padx=10, pady=10)

    # Receive user data and update the labels on the page
    def update_user_data(self, user_id, userdata=None):
        if userdata:
            self.user_data = userdata
        else:
            self.user_data = get_user_data(user_id)
        self.user_id = user_id
        first_name = self.user_data["first name"]
        last_name = self.user_data["last name"]
        self.full_name_label.configure(text=f'{first_name}   {last_name}')

        if self.user_data['dob']:
            age = calculateAge(self.user_data['dob'])
            self.dob_label.configure(text=f'{self.user_data["dob"]}\n{age} years old')
        else:
            self.dob_label.configure(text='Update your info')
        if self.user_data['sex']:
            self.sex_label.configure(text=f'{self.user_data["sex"]}')
        else:
            self.sex_label.configure(text='Update your info')
        if self.user_data['weight']:
            self.weight_label.configure(text=f'{int(self.user_data["weight"])} kg.')
        else:
            self.weight_label.configure(text='Update your info')
        if self.user_data['height']:
            self.height_label.configure(text=f"{int(self.user_data['height'])} cm.")
        else:
            self.height_label.configure(text='Update your info')
        if self.user_data['bloodtype']:
            self.bloodtype_label.configure(text=f"{self.user_data['bloodtype']}")
        else:
            self.bloodtype_label.configure(text='Update your info')

    # defines the function to open dialogue window for data entry for updating the personal information
    def open_update(self, text):
        if text == 'dob':
            if self.update_top_level is None or not self.update_top_level.winfo_exists():
                self.update_top_level = TopLevelUpdate(self, text)
                self.update_top_level.title('Update Date of Birth')
                self.update_top_level.grid()
                self.update_top_level.focus()
                self.update_top_level.update_button.configure(command=lambda x=1: self.update_the_buttons(self.user_id))
            else:
                self.update_top_level.destroy()
                self.update_top_level = None
                self.open_update('dob')
        elif text == 'WEIGHT':
            if self.update_top_level is None or not self.update_top_level.winfo_exists():
                self.update_top_level = TopLevelUpdate(self, text)
                self.update_top_level.title('Add weight')
                self.update_top_level.grid()
                self.update_top_level.focus()
                self.update_top_level.update_button.configure()
                self.update_top_level.update_button.configure(command=lambda x='WEIGHT': self.update_measurement(x))
            else:
                self.update_top_level.destroy()
                self.update_top_level = None
                self.open_update('WEIGHT')
        elif text == 'HEIGHT':
            if self.update_top_level is None or not self.update_top_level.winfo_exists():
                self.update_top_level = TopLevelUpdate(self, text)
                self.update_top_level.title('Add height')
                self.update_top_level.grid()
                self.update_top_level.focus()
                self.update_top_level.update_button.configure()
                self.update_top_level.update_button.configure(command=lambda x='HEIGHT': self.update_measurement(x))
            else:
                self.update_top_level.destroy()
                self.update_top_level = None
                self.open_update('HEIGHT')

    # Updates all labels in the personal information page to show the new information
    def update_the_buttons(self, userid):
        date = self.update_top_level.date_menu.get()
        month = self.update_top_level.month_menu.get()
        year = self.update_top_level.year_menu.get()
        sex = self.update_top_level.sex_menu.get()
        bloodtype = self.update_top_level.bloodtype_menu.get()
        full_date = f'{date} {month} {year}'
        age = calculateAge(full_date)
        self.dob_label.configure(text=f'{full_date}\n{age} years old')
        self.sex_label.configure(text=sex)
        self.bloodtype_label.configure(text=bloodtype)
        self.update_top_level.withdraw()
        update_user_details(userid, full_date, sex, bloodtype)

    # function that updates the weight and populates it to the database for statistics
    def update_measurement(self, meas):
        self.update_top_level.withdraw()
        measurement = self.update_top_level.weight_entry.get()
        update_meas(self.user_id, measurement, meas)
        self.user_data = get_user_data(self.user_id)
        self.update_user_data(self.user_id, self.user_data)


# Top level window for weight and info update
class TopLevelUpdate(Tk.CTkToplevel):
    def __init__(self, master, name='', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("500x260+800+500")
        self.resizable(False, False)
        self.color_scheme = provide_color_scheme()
        self.columnconfigure(0, minsize=30)
        self.columnconfigure(3, minsize=50)
        self.rowconfigure(0, minsize=20)
        self.rowconfigure(4, minsize=70)
        self.name = name
        self.deiconify()
        self.update_button = StandardButton(self)
        if self.name == 'dob':
            self.geometry("500x260+800+500")
            # labels
            self.date_label = StandardLabel(self, text='Date')
            self.month_label = StandardLabel(self, text='Month')
            self.year_label = StandardLabel(self, text='Year')
            self.sex_label = StandardLabel(self, text='Sex')
            self.bloodtype_label = StandardLabel(self, text='Blood type')

            # menus
            self.date_menu = StandardDropDown(self,
                                              values=[str(x) for x in range(1, 32)])
            self.month_menu = StandardDropDown(self, values=['January', 'February', 'March', 'April', 'May', 'June',
                                                             'July', 'August', 'September', 'October', 'November',
                                                             'December'])

            self.year_menu = StandardDropDown(self,
                                              values=[str(x) for x in range(1930, 2023)])

            self.sex_menu = StandardDropDown(self, values=['Male', 'Female'])

            self.bloodtype_menu = StandardDropDown(self, values=['A', 'B', 'AB', 'O'])

            # positioning the elements
            self.date_label.grid(row=1, column=1, pady=10)
            self.date_menu.grid(row=1, column=2, padx=5)
            self.month_label.grid(row=2, column=1, pady=10)
            self.month_menu.grid(row=2, column=2, padx=5)
            self.year_label.grid(row=3, column=1, pady=10)
            self.year_menu.grid(row=3, column=2, pady=5)
            self.sex_label.grid(row=1, column=4, pady=10)
            self.sex_menu.grid(row=1, column=5, padx=5)
            self.bloodtype_label.grid(row=2, column=4, padx=5)
            self.bloodtype_menu.grid(row=2, column=5, padx=5)

            self.update_button.configure(text='Update info.')
            self.update_button.grid(row=5, column=2)

        elif self.name == 'WEIGHT':
            self.geometry("250x150+800+500")
            self.weight_label = StandardLabel(self, text='Weight')
            self.weight_entry = StandardEntry(self, placeholder_text='Your weight in kg')
            self.weight_label.grid(row=1, column=1)
            self.weight_entry.grid(row=1, column=2, padx=10)
            self.update_button.configure(text='Add weight')
            self.update_button.grid(row=5, column=2)

        elif self.name == 'HEIGHT':
            self.geometry("250x150+800+500")
            self.weight_label = StandardLabel(self, text='Height')
            self.weight_entry = StandardEntry(self, placeholder_text='Your height in cm')
            self.weight_label.grid(row=1, column=1)
            self.weight_entry.grid(row=1, column=2, padx=10)
            self.update_button.configure(text='Add height')
            self.update_button.grid(row=5, column=2)
