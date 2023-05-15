from abc import ABC
import customtkinter as Tk
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from database_handling import get_user_statistics
from helpers import provide_color_scheme


class StatisticsPage(Tk.CTkFrame, ABC):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(border_width=1, border_color=self.color_scheme['hover_color'])
        self.user_id = user_id
        self.user_data = None
        self.pack_propagate(0)

        self.tabview = Tk.CTkTabview(self, width=675, height=580)
        self.tabview.pack(padx=5, pady=5)
        self.tabview.add("Weight")
        self.tabview.add("BMI")
        self.tabview.add("Body Fat")
        self.tabview.add("Lean Body Mass")
        self.tabview.configure(segmented_button_selected_color=self.color_scheme['button_color'])
        self.tabview.configure(segmented_button_selected_hover_color=self.color_scheme['hover_color'])
        self.tabview.configure(segmented_button_unselected_hover_color=self.color_scheme['hover_color'])
        self.tabview.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.tabview.configure(bg_color=self.color_scheme['outer_frame_bg_color'])
        self.tabview.configure(text_color=self.color_scheme['button_text_color'])

        self.weight_figure_frame = Tk.CTkFrame(self.tabview.tab('Weight'), width=200, height=200)
        self.weight_figure_frame.pack()
        self.bmi_figure_frame = Tk.CTkFrame(self.tabview.tab('BMI'), width=200, height=200)
        self.bmi_figure_frame.grid(row=0, column=0, sticky='swe')
        self.body_fat_figure_frame = Tk.CTkFrame(self.tabview.tab('Body Fat'), width=200, height=200)
        self.body_fat_figure_frame.grid(row=0, column=0, sticky='swe')
        self.lean_body_mass_figure_frame = Tk.CTkFrame(self.tabview.tab('Lean Body Mass'), width=200, height=200)
        self.lean_body_mass_figure_frame.grid(row=0, column=0, sticky='swe')

        # weight graph
        self.fig_weight = Figure(figsize=(9.3, 6.2), dpi=100)
        self.fig_weight.suptitle('Weight measurements')
        self.fig_weight.set_facecolor(self.color_scheme['outer_frame_bg_color'])
        self.canvas_weight = FigureCanvasTkAgg(self.fig_weight, master=self.weight_figure_frame)
        self.canvas_weight.draw()
        self.canvas_weight.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar_weight = NavigationToolbar2Tk(self.canvas_weight, self.weight_figure_frame)
        self.toolbar_weight.update()
        self.canvas_weight.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # bmi graph
        self.fig_bmi = Figure(figsize=(8.5, 6.2), dpi=100)
        self.fig_bmi.suptitle('BMI measurements')
        self.fig_bmi.set_facecolor(self.color_scheme['button_color'])
        self.canvas_bmi = FigureCanvasTkAgg(self.fig_bmi, master=self.bmi_figure_frame)
        self.canvas_bmi.draw()
        self.canvas_bmi.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar_bmi = NavigationToolbar2Tk(self.canvas_bmi, self.bmi_figure_frame)
        self.toolbar_bmi.update()
        self.canvas_bmi.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # body fat graph
        self.fig_body_fat = Figure(figsize=(8.5, 6.2), dpi=100)
        self.fig_body_fat.suptitle('BMI measurements')
        self.fig_body_fat.set_facecolor(self.color_scheme['button_color'])
        self.canvas_body_fat = FigureCanvasTkAgg(self.fig_body_fat, master=self.body_fat_figure_frame)
        self.canvas_body_fat.draw()
        self.canvas_body_fat.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar_bmi = NavigationToolbar2Tk(self.canvas_body_fat, self.body_fat_figure_frame)
        self.toolbar_bmi.update()
        self.canvas_body_fat.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # lean body mass graph
        self.fig_lean_body_mass = Figure(figsize=(8.5, 6.2), dpi=100)
        self.fig_lean_body_mass.suptitle('BMI measurements')
        self.fig_lean_body_mass.set_facecolor(self.color_scheme['button_color'])
        self.canvas_lean_body_mass = FigureCanvasTkAgg(self.fig_lean_body_mass, master=self.lean_body_mass_figure_frame)
        self.canvas_lean_body_mass.draw()
        self.canvas_lean_body_mass.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar_bmi = NavigationToolbar2Tk(self.canvas_lean_body_mass, self.lean_body_mass_figure_frame)
        self.toolbar_bmi.update()
        self.canvas_lean_body_mass.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    # function to update the data from the user database
    def update_user_data(self, userdata, measurement_type):
        self.user_data = userdata
        data = get_user_statistics(self.user_id, measurement_type)
        data_entries = [x[0] for x in data]
        data_dates = [x[1] for x in data]
        self.plot_the_data(data_entries, data_dates)

    # function to plot the gathered data
    def plot_the_data(self, data, dates):
        self.fig_weight.add_subplot(111).plot(dates, data)
        self.fig_weight.supxlabel('Date (YYYY-MM-DD)')
        self.fig_weight.supylabel('Weight (kg)')
        self.canvas_weight.draw()
        self.toolbar_weight.update()
