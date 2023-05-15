import datetime

import customtkinter as Tk
from PIL import Image
from database_handling import get_user_data
from template_tkinter_elemenets import StandardLabel, StandardDropDown
from helpers import provide_color_scheme


class DashBoardPage(Tk.CTkFrame):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, minsize=250)
        self.grid_rowconfigure(1, minsize=463)
        self.grid_columnconfigure(0, minsize=300)
        self.grid_columnconfigure(1, minsize=520)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['inner_frame_fg_color'], corner_radius=5)

        self.current_userid = user_id
        self.update_top_level = None
        self.user_data = None

        # Main frames
        self.hello_frame = Tk.CTkFrame(self, fg_color=self.color_scheme['menu_color'])
        self.calendar_frame = Tk.CTkFrame(self, fg_color=self.color_scheme['menu_color'])
        self.info_frame = Tk.CTkFrame(self, fg_color=self.color_scheme['menu_color'])

        self.hello_frame.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
        self.calendar_frame.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
        self.info_frame.grid(row=1, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)
        self.info_frame.grid_columnconfigure(6, minsize=90)

        # Calendar Frame
        self.upcoming_label = StandardLabel(self.calendar_frame,
                                            text='Upcoming appointment',
                                            width=50)
        self.upcoming_label.configure(font=(self.color_scheme['text_font'][0], 20))
        self.upcoming_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.doctor_image = Tk.CTkImage(Image.open('images/doctor.png'), size=(64, 64))
        self.doctor_label = Tk.CTkLabel(self.calendar_frame, text='', image=self.doctor_image)
        self.doctor_label.grid(row=1, column=0, padx=10, pady=10, sticky='w', rowspan=2)
        self.doctor_name_label = StandardLabel(self.calendar_frame,
                                               text='Dr. Emilia Peneva',
                                               width=50)
        self.doctor_name_label.configure(font=(self.color_scheme['text_font'][0], 15))
        self.doctor_name_label.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        self.doctor_specialty_label = StandardLabel(self.calendar_frame,
                                                    text='Dentist',
                                                    width=50)
        self.doctor_specialty_label.configure(font=(self.color_scheme['text_font'][0], 13), text_color='blue')
        self.doctor_specialty_label.grid(row=2, column=1, padx=10, columnspan=2, sticky='w')

        self.calendar_image = Tk.CTkImage(Image.open('images/calendar.png'), size=(32, 32))
        self.calendar_image = Tk.CTkLabel(self.calendar_frame, text='', image=self.calendar_image)
        self.calendar_image.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.date_label = StandardLabel(self.calendar_frame,
                                        text='13 Apr 2023',
                                        width=50)
        self.date_label.configure(font=(self.color_scheme['text_font'][0], 13))
        self.date_label.grid(row=3, column=1, padx=10, columnspan=2, sticky='w')

        self.clock_image = Tk.CTkImage(Image.open('images/clock.png'), size=(32, 32))
        self.calendar_image = Tk.CTkLabel(self.calendar_frame, text='', image=self.clock_image)
        self.calendar_image.grid(row=3, column=3, padx=10, pady=10, sticky='w', rowspan=3)

        self.clock_label = StandardLabel(self.calendar_frame,
                                         text='09:00',
                                         width=50)
        self.clock_label.configure(font=(self.color_scheme['text_font'][0], 13))
        self.clock_label.grid(row=3, column=4, padx=10, sticky='w')

        # Hello Frame
        self.full_name_label = StandardLabel(self.hello_frame,
                                             text='',
                                             width=50)
        self.full_name_label.configure(font=(self.color_scheme['text_font'][0], 30))
        self.full_name_label.grid(row=1, column=1,
                                  padx=10, pady=10,
                                  columnspan=2)

        self.lets_track_label = StandardLabel(self.hello_frame,
                                              text="Let's track your health daily!",
                                              width=50,
                                              text_color='#838c8e')
        self.lets_track_label.configure(font=(self.color_scheme['text_font'][0], 13))
        self.lets_track_label.grid(row=2, column=1,
                                   padx=10,
                                   columnspan=2,
                                   sticky='w')

        # Info frame
        self.patient_activities_label = StandardLabel(self.info_frame,
                                                      text='Activities',
                                                      width=50)
        self.patient_activities_label.configure(font=(self.color_scheme['text_font'][0], 30))
        self.patient_activities_label.grid(row=1, column=1,
                                           padx=10, pady=10,
                                           columnspan=2,
                                           sticky='w')

        self.today_label = StandardLabel(self.info_frame,
                                         text="Let's track your health daily!",
                                         width=50,
                                         text_color='#838c8e')
        self.today_label.configure(font=(self.color_scheme['text_font'][0], 13))
        self.today_label.grid(row=2, column=1,
                              padx=10,
                              columnspan=2,
                              sticky='w')

        self.activities_image = Tk.CTkImage(Image.open('images/activities.png'), size=(300, 175))
        self.activities_image = Tk.CTkLabel(self.info_frame, text='', image=self.activities_image)
        self.activities_image.grid(row=3, column=1, padx=10, pady=10, sticky='w', columnspan=2)

        self.month_menu = StandardDropDown(self.info_frame,
                                           values=['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                                   'August', 'September', 'October', 'November', 'December'])
        self.month_menu.grid(row=1, column=7)

        self.progress_image = Tk.CTkImage(Image.open('images/progress.png'), size=(196, 290))
        self.progress_image_label = Tk.CTkLabel(self.info_frame, text='', image=self.progress_image)
        self.progress_image_label.grid(row=2, column=7, padx=10, pady=10, sticky='w', rowspan=3)

    # Receive user data and update the labels on the page
    def update_user_data(self, user_id, userdata=None):
        self.user_data = get_user_data(user_id)
        self.current_userid = user_id
        first_name = self.user_data["first name"]
        last_name = self.user_data["last name"]
        self.full_name_label.configure(text=f'Hi, {first_name} {last_name[0]}.')
        now = datetime.datetime.now()
        date = now.strftime("%d %B %Y")
        self.today_label.configure(text=f'Today, {date}')
