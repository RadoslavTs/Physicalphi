from database_handling import add_to_calendar, get_calendar_info, get_calendar_today, remove_from_calendar
import customtkinter as Tk
from helpers import get_today, provide_color_scheme
from tkcalendar import Calendar
import datetime
from tkinter import END, Listbox

from template_tkinter_elemenets import StandardButton, StandardEntry


class ScheduleInfo(Tk.CTkFrame):
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

        # Main frames
        self.calendar_frame = Tk.CTkFrame(self, width=5000, height=300)
        self.calendar_frame.rowconfigure(0, minsize=400)
        self.calendar_frame.columnconfigure(0, minsize=810)
        self.calendar_frame.pack(padx=5, pady=5)

        self.selected_date_frame = Tk.CTkFrame(self)

        self.manipulate_calendar_frame = Tk.CTkFrame(self)

        self.manipulate_calendar_frame.pack(
            side='right',
            fill='y',
            padx=5, pady=5)

        self.selected_date_frame.pack(expand=True,
                                      anchor='sw',
                                      side='left',
                                      fill='both',
                                      padx=5, pady=5)
        # self.selected_date_frame.pack_propagate(0)

        # Calendar
        self.events = {}
        self.today = get_today()
        self.calendar = Calendar(self.calendar_frame,
                                 selectmode='day',
                                 year=self.today.year,
                                 month=self.today.month,
                                 width=600, height=400,
                                 background=self.color_scheme['button_color'],
                                 disabledbackground=True,
                                 bordercolor=self.color_scheme['hover_color'],
                                 selectbackground=self.color_scheme['hover_color'],
                                 font=self.color_scheme['text_font'],
                                 text_color=self.color_scheme['button_text_color'])

        for k in self.events.keys():
            date = datetime.datetime.strptime(k, "%Y-%m-%d").date()
            self.calendar.calevent_create(date, self.events[k][0], self.events[k][1])

        self.calendar.tag_config('event', background=self.color_scheme['button_color'])
        self.calendar.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')

        # Today view elements
        self.title_label_selected = Tk.CTkLabel(self.selected_date_frame,
                                                text='Events for the day',
                                                font=(self.color_scheme['text_font'][0], 20),
                                                text_color=self.color_scheme['button_text_color'])
        self.title_label_selected.pack(padx=5, pady=5)
        self.title_label_one = Listbox(self.selected_date_frame, height=200, font=('Nirmala UI', 15),
                                       selectbackground=self.color_scheme['hover_color'],
                                       yscrollcommand=True,
                                       activestyle='none')
        self.title_label_one.pack(padx=5, pady=5, fill='both', side='bottom')

        self.title_label_control = Tk.CTkLabel(self.manipulate_calendar_frame,
                                               text='Add calendar entry',
                                               font=(self.color_scheme['text_font'][0], 20),
                                               pady=10,
                                               text_color=self.color_scheme['button_text_color'])
        self.title_label_control.grid(row=1, column=1)

        self.add_description_entry = StandardEntry(self.manipulate_calendar_frame,
                                                   width=250, height=100,
                                                   placeholder_text='Write your calendar event here')
        self.add_description_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_calendar_entry_button = StandardButton(self.manipulate_calendar_frame,
                                                        text='Add to calendar',
                                                        command=self.add_entry_to_calendar,
                                                        width=190)
        self.add_calendar_entry_button.grid(row=3, column=1)
        self.remove_calendar_entry_button = StandardButton(self.manipulate_calendar_frame,
                                                           text='Remove from calendar',
                                                           command=self.remove_entry_from_calendar,
                                                           width=190)
        self.remove_calendar_entry_button.grid(row=4, column=1, pady=10)

    # function that updates today view based on calendar day selection
    def update_today(self, e):
        day = self.calendar.selection_get()
        data = get_calendar_today(self.user_id, day)
        data_len = len(data)
        if data:
            self.title_label_one.delete(0, END)
            for i in range(data_len):
                data_to_place = f'{i + 1}. {data[i]}'
                self.title_label_one.insert(END, data_to_place)
        else:
            self.title_label_one.delete(0, END)

    # function to populate database with new calendar entries
    def add_entry_to_calendar(self):
        date = self.calendar.selection_get()
        description = self.add_description_entry.get()
        if date and description:
            self.add_description_entry.delete(0, END)
            add_to_calendar(date, description, self.user_id)
            self.calendar.calevent_create(date, description, 'event')
        self.update_today(date)

    def remove_entry_from_calendar(self):
        selection = ''
        try:
            selection = self.title_label_one.selection_get()
        except:
            pass

        if selection:
            description = selection.split('.')[1]
            date = self.calendar.selection_get()
            remove_from_calendar(self.user_id, date, description)
            self.update_today(date)

    # function to update the calendar from the database
    def update_calendar(self):
        events = get_calendar_info(self.user_id)
        for date, value in events.items():
            current_date_converted = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            current_description = value[0]
            placeholder = value[1]
            self.calendar.calevent_create(current_date_converted, current_description, placeholder)

    # function to clear the current entries for initialization purposes
    def update_current_entries(self):
        self.title_label_one.delete(0, END)
