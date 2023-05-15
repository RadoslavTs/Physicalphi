import customtkinter as Tk
from PIL import Image
from tkinter import END
from database_handling import get_user_data
from helpers import calculateAge, provide_color_scheme
from template_tkinter_elemenets import StandardButton, StandardEntry, StandardLabel


class BMICalculator(Tk.CTkFrame):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, minsize=20)
        self.grid_columnconfigure(0)
        self.current_userid = user_id
        # self.pack_propagate(0)
        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(bg_color=self.color_scheme['outer_frame_bg_color'])

        self.calculator_info_text = "BMI is a measurement of a person's leanness or corpulence based on " \
                                    "their height and weight, and is intended to quantify tissue mass. It is widely " \
                                    "used as a general indicator of whether a person has a healthy body weight for " \
                                    "their height. Specifically, the value obtained from the calculation of BMI is " \
                                    "used to categorize whether a person is underweight, normal weight, overweight," \
                                    " or obese depending on what range the value falls between. These ranges of " \
                                    "BMI vary based on factors such as region and age, and are sometimes further " \
                                    "divided into subcategories such as severely underweight or very severely obese." \
                                    " Being overweight or underweight can have significant health effects, so while" \
                                    " BMI is an imperfect measure of healthy body weight, it is a useful indicator" \
                                    " of whether any additional testing or action is required. Refer to the table" \
                                    " below to see the different categories based on BMI that are used by the " \
                                    "calculator."

        self.control_frame = Tk.CTkFrame(self)
        self.control_frame.pack(expand=True,
                                anchor='nw',
                                side='top',
                                fill='x',
                                padx=5, pady=5)
        self.control_frame.columnconfigure(0, minsize=30)
        self.control_frame.columnconfigure(4, minsize=100)
        self.control_frame.rowconfigure(0, minsize=30)
        self.control_frame.columnconfigure(6, minsize=90)

        self.result_frame = Tk.CTkFrame(self)
        self.result_frame.rowconfigure(0, minsize=20)
        self.result_frame.rowconfigure(7, minsize=45)
        self.result_frame.pack(expand=True,
                               anchor='sw',
                               side='bottom',
                               fill='both',
                               padx=5, pady=5)

        # Elements

        self.age_label = StandardLabel(self.control_frame, text='Age:', width=50)
        self.age_label.grid(row=1, column=1, padx=10, pady=10)
        self.age_entry = StandardEntry(self.control_frame, width=200,
                                       placeholder_text="Your age (2-120)")
        self.age_entry.grid(row=1, column=2, padx=10, pady=10, columnspan=2, sticky='w')

        self.gender_label = StandardLabel(self.control_frame, text='Gender')
        self.gender_label.grid(row=2, column=1, pady=10)
        self.gender_male_button = Tk.CTkRadioButton(self.control_frame,
                                                    text='Male',
                                                    width=10,
                                                    command=lambda x='male': self.check_gender(x),
                                                    fg_color=self.color_scheme['button_color'])
        self.gender_male_button.grid(row=2, column=2, pady=10)
        self.gender_female_button = Tk.CTkRadioButton(self.control_frame,
                                                      text='Female',
                                                      command=lambda x='female': self.check_gender(x),
                                                      fg_color=self.color_scheme['button_color'])
        self.gender_female_button.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        self.height_label = StandardLabel(self.control_frame, text='Height:')
        self.height_label.grid(row=3, column=1,
                               padx=10, pady=10)
        self.height_entry = StandardEntry(self.control_frame,
                                          width=200,
                                          placeholder_text='your height in cm')
        self.height_entry.grid(row=3, column=2,
                               padx=10, pady=10,
                               columnspan=2, sticky='w')

        self.weight_label = StandardLabel(self.control_frame, text='Weight:')
        self.weight_label.grid(row=4, column=1,
                               padx=10, pady=10)
        self.weight_entry = StandardEntry(self.control_frame,
                                          width=200,
                                          placeholder_text='your weight in kg')
        self.weight_entry.grid(row=4, column=2,
                               padx=10, pady=10,
                               columnspan=2, sticky='w')

        # Control Buttons
        self.what_is_bmi_button = StandardButton(self.control_frame,
                                                 text='What is BMI',
                                                 width=180,
                                                 command=lambda x='bmi': self.open_info(x))
        self.what_is_bmi_button.grid(row=1, column=5,
                                     pady=10)

        self.bmi_table_button = StandardButton(self.control_frame,
                                               text='BMI Ref. Table',
                                               width=180,
                                               command=lambda x='reference': self.open_info(x))
        self.bmi_table_button.grid(row=2, column=5,
                                   pady=10)

        self.get_personal_data_button = StandardButton(self.control_frame,
                                                       text='Get data from profile',
                                                       width=180,
                                                       command=self.get_personal_data)
        self.get_personal_data_button.grid(row=3, column=5,
                                           pady=10)

        self.calculate_button = StandardButton(self.control_frame,
                                               text="Calculate result",
                                               width=180,
                                               command=self.calculate_bmi)
        self.calculate_button.grid(row=4, column=5,
                                   pady=10)

        self.result_label = StandardLabel(self.result_frame,
                                          width=100, height=10,
                                          text='BMI Result:')
        self.result_label.grid(row=1, column=1,
                               padx=5,
                               columnspan=3, sticky='wes')

        self.progressbar = Tk.CTkProgressBar(self.result_frame, width=600, height=25,
                                             progress_color=self.color_scheme['button_color'],
                                             mode='indeterminate')
        self.progressbar.start()
        self.progressbar.set(0)
        self.progressbar.grid(row=3, column=0,
                              pady=10, padx=15,
                              columnspan=10)

        self.underweight_label = StandardLabel(self.result_frame,
                                               text='Underweight')
        self.underweight_label.grid(row=5, column=1,
                                    sticky='w')

        self.normal_label = StandardLabel(self.result_frame,
                                          text='Normal')
        self.normal_label.grid(row=5, column=3)

        self.overweight_label = StandardLabel(self.result_frame,
                                              text='Overweight')
        self.overweight_label.grid(row=5, column=6)

        self.obesity_label = StandardLabel(self.result_frame,
                                           text='Obesity')
        self.obesity_label.grid(row=5, column=8,
                                sticky='e')

        self.scrollable_description = Tk.CTkFrame(self.result_frame, width=350, height=500)
        self.scrollable_description.pack_propagate(0)
        self.scrollable_description.grid(row=6, column=1,
                                         padx=5,
                                         sticky='s',
                                         columnspan=8)

        self.result_description = StandardLabel(self.scrollable_description,
                                                width=300, height=200,
                                                text='Description of the results:',
                                                compound='center')
        self.result_description.grid(row=0, column=0,
                                     columnspan=3)

        self.top_level_info = None

    # function to open top-level window with info about the calculator
    def open_info(self, info):
        if self.top_level_info is None or not self.top_level_info.winfo_exists():
            if info == 'bmi':
                self.top_level_info = TopLevelInfo()
                self.top_level_info.title('What is BMI')
                self.top_level_info.label.insert('0.0', self.calculator_info_text)
                self.top_level_info.label.pack(padx=20, pady=20)

            elif info == 'reference':
                self.top_level_info = TopLevelInfo('bmi')
                self.top_level_info.title('BMI reference table')
                self.top_level_info.tabview.grid(row=0, column=0, padx=10, pady=10)
            self.top_level_info.focus()
        else:
            self.top_level_info.destroy()
            if info == 'bmi':
                self.open_info('bmi')
            else:
                self.open_info('reference')

    # function to control the gender buttons
    def check_gender(self, button):
        if button == 'female':
            self.gender_male_button.deselect()
        else:
            self.gender_female_button.deselect()

    # function to calculate and update the bmi and progress bar
    def calculate_bmi(self):
        if self.weight_entry.get() and self.height_entry.get() and self.age_entry.get():
            try:
                self.progressbar.stop()
                self.progressbar.configure(mode='determinate')
                bmi = float(self.weight_entry.get()) / ((float(self.height_entry.get()) / 100) ** 2)
                self.result_label.configure(text=f'BMI Result: {bmi:.1f}')
                if 0.04 * (bmi - 15) > 1:
                    progress_bar_scale = 1
                elif 0.04 * (bmi - 15) < 0:
                    progress_bar_scale = 0
                else:
                    progress_bar_scale = 0.04 * (bmi - 15)
                if int(self.age_entry.get()) > 20:
                    self.progressbar.set(progress_bar_scale)
                    healthy_weight_for_the_height_min = 18.5 * ((float(self.height_entry.get()) / 100) ** 2)
                    healthy_weight_for_the_height_max = 25 * ((float(self.height_entry.get()) / 100) ** 2)
                    weight_to_lose = float(self.weight_entry.get()) - healthy_weight_for_the_height_max
                    ponderal_index = float(self.weight_entry.get()) / ((float(self.height_entry.get()) / 100) ** 3)
                    if bmi < 16:
                        self.progressbar.configure(progress_color='red')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Severe Thinness!')
                    elif 16 <= bmi < 17:
                        self.progressbar.configure(progress_color='orange')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Moderate Thinness!')
                    elif 17 <= bmi < 18.5:
                        self.progressbar.configure(progress_color='yellow')
                        self.result_description.configure(text='Mild Thinness')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Mild Thinness!')
                    elif 18.5 <= bmi < 25:
                        self.progressbar.configure(progress_color='green')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Normal!')
                    elif 25 <= bmi < 30:
                        self.progressbar.configure(progress_color='yellow')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Overweight!')
                    elif 30 <= bmi < 35:
                        self.progressbar.configure(progress_color='orange')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Obese Class I')
                    elif 35 <= bmi < 40:
                        self.progressbar.configure(progress_color='orange')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Obese Class II')
                    elif bmi >= 40:
                        self.progressbar.configure(progress_color='red')
                        self.result_label.configure(text=f'BMI Result: {bmi:.1f} - Obese Class III')
                    self.result_description.configure(text=f'Healthy BMI range: 18.5 kg/m2 - 25 kg/m2\nHealthy weight '
                                                           f'for the height: {healthy_weight_for_the_height_min:.1f} '
                                                           f'kgs - {healthy_weight_for_the_height_max:.1f} kgs\n'
                                                           f'{"Lose -" if weight_to_lose >= 0 else "Gain "}'
                                                           f'{weight_to_lose:.1f} kgs to reach a BMI of 25 kg/m2.\n'
                                                           f'BMI Prime: {25 / bmi:.2f}\nPonderal'
                                                           f' Index: {ponderal_index:.1f} kg/m3')
            except ValueError:
                self.result_description.configure(text='Invalid Inputs')
                self.progressbar.configure(mode='indeterminate')
                self.progressbar.start()

        else:
            self.result_description.configure(text='Please fill age, weight and height')
            self.progressbar.set(0)

    # function to clear the entries (navigational purposes)
    def clear_fields(self):
        self.age_entry.delete(0, END)
        self.age_entry.configure(placeholder_text="Your age (2-120)")
        self.weight_entry.delete(0, END)
        self.weight_entry.configure(placeholder_text='your weight in kg')
        self.height_entry.delete(0, END)
        self.height_entry.configure(placeholder_text='your height in cm')
        self.progressbar.configure(mode='indeterminate')
        self.progressbar.configure(progress_color=self.color_scheme['button_color'])
        self.progressbar.start()
        self.gender_female_button.deselect()
        self.gender_male_button.deselect()

    # function to call for the persons data (easier calculation)
    def get_personal_data(self):
        user_data = get_user_data(self.current_userid)
        weight = user_data['weight']
        height = user_data['height']
        dob = user_data['dob']
        sex = user_data['sex']

        if weight:
            self.weight_entry.delete(0, END)
            self.weight_entry.insert(0, weight)
        if height:
            self.height_entry.delete(0, END)
            self.height_entry.insert(0, height)
        if dob:
            self.age_entry.delete(0, END)
            self.age_entry.insert(0, calculateAge(dob))
        if sex:
            if sex == 'Male':
                self.gender_male_button.select()
                self.gender_female_button.deselect()
            else:
                self.gender_female_button.select()
                self.gender_male_button.deselect()


# Top level creation
class TopLevelInfo(Tk.CTkToplevel):
    def __init__(self, name='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400+800+500")
        self.resizable(False, False)
        self.color_scheme = provide_color_scheme()
        self.color_scheme = provide_color_scheme()
        self.frame = Tk.CTkFrame(self,
                                 fg_color=self.color_scheme['inner_frame_bg_color'],
                                 bg_color=self.color_scheme['inner_frame_bg_color'],
                                 width=500, height=400,
                                 border_width=0)
        self.frame.pack()
        self.image_adult = None
        self.image_children = None
        self.name = name
        if self.name:
            self.tabview = Tk.CTkTabview(self.frame, width=500, height=400)
            self.tabview.add("Adults")
            self.tabview.add("Children- age: 2-20")
            self.tabview.configure(segmented_button_selected_color=self.color_scheme['button_color'])
            self.tabview.configure(segmented_button_selected_hover_color=self.color_scheme['hover_color'])
            self.tabview.configure(segmented_button_unselected_hover_color=self.color_scheme['hover_color'])
            self.tabview.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
            self.tabview.configure(bg_color=self.color_scheme['outer_frame_bg_color'])
            self.tabview.configure(text_color=self.color_scheme['button_text_color'])
            if self.name == 'bmi':
                self.image_adult = Tk.CTkImage(Image.open('images/tools/bmi_table.png'),
                                               size=(358, 288))
                self.image_children = Tk.CTkImage(Image.open('images/tools/bmi_table_children.png'),
                                                  size=(358, 161))
                self.image_label_adult = Tk.CTkLabel(self.tabview.tab('Adults'),
                                                     text='',
                                                     image=self.image_adult)
                self.image_label_adult.pack()
                self.image_label_children = Tk.CTkLabel(self.tabview.tab('Children- age: 2-20'),
                                                        text='',
                                                        image=self.image_children)
                self.image_label_children.pack()

        self.label = Tk.CTkTextbox(self.frame,
                                   width=500, height=400,
                                   wrap='word')
