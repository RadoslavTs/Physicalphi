import customtkinter as Tk
from PIL import Image
from database_handling import get_user_names, get_user_data
from calendar_page import ScheduleInfo
from template_tkinter_elemenets import StandardButton, StandardLabel
from tools_page import ToolsPage
from personal_info_page import PersonalInfo
from statistics_page import StatisticsPage
from dashboard_page import DashBoardPage
from helpers import get_today, provide_color_scheme


class DashBoardMenu(Tk.CTkFrame):
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)
        self.pack_propagate(0)
        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(bg_color=self.color_scheme['outer_frame_bg_color'])

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.bg_image = Tk.CTkImage(Image.open('images/bg_gradient.jpg'), size=(self.WIDTH, self.HEIGHT))
        self.bg_image_label = Tk.CTkLabel(self, text='', image=self.bg_image)
        self.bg_image_label.place(x=0, y=0)
        self.dash_frame = Tk.CTkFrame(self,
                                      fg_color=self.color_scheme['menu_color'],
                                      bg_color=self.color_scheme['menu_color'],
                                      width=300, height=600,
                                      border_width=0)
        self.dash_frame.grid(row=0, column=0,
                             sticky="nsew")
        self.dash_frame.grid_rowconfigure(6, weight=1)

        self.user_image = Tk.CTkImage(Image.open("images/user_icon.png"),
                                      size=(30, 30))
        self.dashboard_image = Tk.CTkImage(Image.open("images/menu/pie-chart.png"),
                                           size=(20, 20))
        self.schedule_image = Tk.CTkImage(Image.open("images/menu/calendar.png"),
                                          size=(20, 20))
        self.personal_info_image = Tk.CTkImage(Image.open("images/menu/personal_info.png"),
                                               size=(20, 20))
        self.statistics_image = Tk.CTkImage(Image.open("images/menu/statistics.png"),
                                            size=(20, 20))
        self.tools_image = Tk.CTkImage(Image.open("images/menu/tools.png"),
                                       size=(20, 20))
        self.logout_image = Tk.CTkImage(Image.open("images/menu/logout.png"),
                                        size=(20, 20))

        self.current_userid = user_id
        self.user_data = None
        self.full_name = ''

        self.user_image_frame = Tk.CTkLabel(self.dash_frame,
                                            text="",
                                            image=self.user_image,
                                            compound="center")
        self.user_image_frame.grid(row=0, column=0,
                                   padx=10, pady=10)
        self.user_image_label = StandardLabel(self.dash_frame,
                                              text=self.full_name)
        self.user_image_label.grid(row=0, column=1,
                                   padx=5)

        self.dashboard_button = StandardButton(self.dash_frame,
                                               text="Dashboard",
                                               image=self.dashboard_image,
                                               anchor='w',
                                               command=lambda x='dashboard_page': self.pick_category(x),
                                               width=180)
        self.dashboard_button.grid(row=1, column=0,
                                   padx=20, pady=10,
                                   columnspan=2)
        self.schedule_button = StandardButton(self.dash_frame,
                                              text="Schedule",
                                              image=self.schedule_image,
                                              anchor='w',
                                              command=lambda x='schedule': self.pick_category(x),
                                              width=180)
        self.schedule_button.grid(row=2, column=0,
                                  padx=20, pady=10,
                                  columnspan=2)
        self.personal_info_button = StandardButton(self.dash_frame,
                                                   text="Personal Info",
                                                   image=self.personal_info_image,
                                                   anchor='w',
                                                   command=lambda x='personal_info': self.pick_category(x),
                                                   width=180)
        self.personal_info_button.grid(row=3, column=0,
                                       padx=20, pady=10,
                                       columnspan=2)
        self.statistics_button = StandardButton(self.dash_frame,
                                                text="Statistics",
                                                image=self.statistics_image,
                                                anchor='w',
                                                command=lambda x='statistics': self.pick_category(x),
                                                width=180)
        self.statistics_button.grid(row=4, column=0,
                                    padx=20, pady=10,
                                    columnspan=2)
        self.tools_button = StandardButton(self.dash_frame,
                                           text="Tools",
                                           image=self.tools_image,
                                           anchor='w',
                                           command=lambda x='tools': self.pick_category(x),
                                           width=180)
        self.tools_button.grid(row=5, column=0,
                               padx=20, pady=10,
                               columnspan=2)
        self.logoff_button = StandardButton(self.dash_frame,
                                            text="Log off",
                                            image=self.logout_image,
                                            anchor='w',
                                            width=180)
        self.logoff_button.grid(row=8, column=0,
                                padx=20, pady=10,
                                columnspan=2)

        # Tools page
        self.tools_frame = ToolsPage(self, self.current_userid, border_width=1, border_color=self.color_scheme['hover_color'])
        self.tools_frame.bmi_calculator_button.configure(
            command=lambda x='bmi': self.tools_frame.select_calculator_by_name(x, self.current_userid))

        # Personal info page
        self.personal_info_frame = PersonalInfo(self, self.current_userid, border_width=1, border_color=self.color_scheme['hover_color'])

        # Statistics page
        self.statistics_frame = StatisticsPage(self, self.current_userid, border_width=1, border_color=self.color_scheme['hover_color'])

        # Schedule page
        self.schedule_frame = ScheduleInfo(self, self.current_userid, border_width=1, border_color=self.color_scheme['hover_color'])

        # Dashboard page
        self.dashboard_page = DashBoardPage(self, self.current_userid, border_width=1, border_color=self.color_scheme['hover_color'])

    # function to get the users personal data
    def get_user_data(self, user_id):
        self.current_userid = user_id
        self.full_name = get_user_names(user_id)
        self.user_image_label.configure(text=self.full_name)

    # function to control what button has been clicked and call the necessary pages
    def pick_category(self, name):
        if not self.user_data:
            self.user_data = get_user_data(self.current_userid)
        if name == 'tools':
            self.tools_frame.select_calculator_by_name('tools', self.current_userid)
            self.tools_frame.current_username = self.current_userid
            self.tools_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            self.tools_button.configure(fg_color=self.color_scheme['hover_color'])
            self.tools_button.configure(text_color='white')
        else:
            self.tools_frame.grid_forget()
            self.tools_button.configure(fg_color=self.color_scheme['button_color'])
            self.tools_button.configure(text_color=self.color_scheme['button_text_color'])

        if name == 'personal_info':
            self.personal_info_frame.user_data = self.user_data
            self.personal_info_frame.update_user_data(self.current_userid)
            self.personal_info_frame.grid(row=0, column=1,
                                          sticky="nsew",
                                          padx=10, pady=10)
            self.personal_info_button.configure(fg_color=self.color_scheme['hover_color'])
            self.personal_info_button.configure(text_color='white')
        else:
            self.personal_info_frame.grid_forget()
            self.personal_info_button.configure(fg_color=self.color_scheme['button_color'])
            self.personal_info_button.configure(text_color=self.color_scheme['button_text_color'])
        if name == 'statistics':
            self.statistics_frame.user_id = self.current_userid
            self.statistics_frame.update_user_data(self.current_userid, 'WEIGHT')
            self.statistics_frame.grid(row=0, column=1,
                                       sticky="nsew",
                                       padx=10, pady=10)
            self.statistics_button.configure(fg_color=self.color_scheme['hover_color'])
            self.statistics_button.configure(text_color='white')
        else:
            self.statistics_frame.grid_forget()
            self.statistics_button.configure(fg_color=self.color_scheme['button_color'])
            self.statistics_button.configure(text_color=self.color_scheme['button_text_color'])
        if name == 'schedule':
            self.schedule_frame.user_id = self.current_userid
            self.schedule_frame.update_calendar()
            self.schedule_frame.calendar.selection_set(get_today())
            self.schedule_frame.update_current_entries()
            self.schedule_frame.update_today(self.current_userid)
            self.schedule_frame.grid(row=0, column=1,
                                     sticky="nsew",
                                     padx=10, pady=10)
            self.schedule_button.configure(fg_color=self.color_scheme['hover_color'])
            self.schedule_button.configure(text_color='white')
        else:
            self.schedule_frame.grid_forget()
            self.schedule_button.configure(fg_color=self.color_scheme['button_color'])
            self.schedule_button.configure(text_color=self.color_scheme['button_text_color'])
        if name == 'dashboard_page':
            self.dashboard_page.user_data = self.user_data
            self.dashboard_page.update_user_data(self.current_userid, self.user_data)
            self.dashboard_page.grid(row=0, column=1,
                                     sticky="nsew",
                                     padx=10, pady=10)
            self.dashboard_button.configure(fg_color=self.color_scheme['hover_color'])
            self.dashboard_button.configure(text_color='white')
        else:
            self.dashboard_page.grid_forget()
            self.dashboard_button.configure(fg_color=self.color_scheme['button_color'])
            self.dashboard_button.configure(text_color=self.color_scheme['button_text_color'])

    # function to clear the frames
    def forget_all_frames(self):
        self.tools_frame.grid_forget()
        self.personal_info_frame.grid_forget()
        self.schedule_frame.grid_forget()
