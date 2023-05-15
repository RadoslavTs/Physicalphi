from abc import ABC
import customtkinter as Tk
from PIL import Image

from helpers import provide_color_scheme
from template_tkinter_elemenets import CalculatorButton
from tools_calcs.bmi_calculator import BMICalculator


class ToolsPage(Tk.CTkFrame):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)

        self.color_scheme = provide_color_scheme()
        self.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.configure(border_width=1)
        self.configure(border_color=self.color_scheme['hover_color'])
        self.rowconfigure(0, minsize=2)
        self.columnconfigure(0, minsize=2)
        self.pad_x = 8
        self.pad_y = 10
        self.current_userid = user_id

        # tabview creation
        self.tabview = Tk.CTkTabview(self, fg_color=self.color_scheme['outer_frame_fg_color'])
        # self.tabview.grid(row=1, column=1, sticky='nswe')


        self.tabview.add("Fitness")
        self.tabview.add("Pregnancy")
        self.tabview.add("Other")
        self.tabview.configure(segmented_button_selected_color=self.color_scheme['button_color'])
        self.tabview.configure(segmented_button_selected_hover_color=self.color_scheme['hover_color'])
        self.tabview.configure(segmented_button_unselected_hover_color=self.color_scheme['hover_color'])
        self.tabview.configure(fg_color=self.color_scheme['outer_frame_fg_color'])
        self.tabview.configure(bg_color=self.color_scheme['outer_frame_bg_color'])
        self.tabview.configure(text_color=self.color_scheme['button_text_color'])

        # BMI button
        self.bmi_image = Tk.CTkImage(Image.open("images/tools/bmi.png"), size=(40, 40))
        self.bmi_calculator_button = CalculatorButton(self.tabview.tab('Fitness'), text="BMI",
                                                      image=self.bmi_image,
                                                      command=lambda x='bmi':
                                                      self.select_calculator_by_name(x, self.current_userid))
        self.bmi_calculator_button.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y)

        # Calorie calculator button
        self.calorie_calculator_image = Tk.CTkImage(Image.open("images/tools/calories-calculator.png"), size=(40, 40))
        self.calorie_calculator_button = CalculatorButton(self.tabview.tab('Fitness'), text="Calories",
                                                          image=self.calorie_calculator_image)
        self.calorie_calculator_button.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y)

        # Body Fat Calculator
        self.body_fat_calculator_image = Tk.CTkImage(Image.open("images/tools/body-fat.png"), size=(40, 40))
        self.body_fat_calculator_button = CalculatorButton(self.tabview.tab('Fitness'), text="Body Fat",
                                                           image=self.body_fat_calculator_image)
        self.body_fat_calculator_button.grid(row=0, column=2, padx=self.pad_x, pady=self.pad_y)

        # BMR Calculator
        self.bmr_calculator_image = Tk.CTkImage(Image.open("images/tools/fat.png"), size=(40, 40))
        self.bmr_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                      text="BMR",
                                                      image=self.bmr_calculator_image)
        self.bmr_calculator_button.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y)

        # Ideal Weight Calculator
        self.ideal_weight_calculator_image = Tk.CTkImage(Image.open("images/tools/weight-loss.png"), size=(40, 40))
        self.ideal_weight_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                               text="Ideal Weight",
                                                               image=self.ideal_weight_calculator_image)
        self.ideal_weight_calculator_button.grid(row=1, column=1, padx=self.pad_x, pady=self.pad_y)

        # Army Body Fat Calculator
        self.army_body_calculator_image = Tk.CTkImage(Image.open("images/tools/commander.png"), size=(40, 40))
        self.army_body_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                            text="Army Body Fat",
                                                            image=self.army_body_calculator_image)
        self.army_body_calculator_button.grid(row=1, column=2, padx=self.pad_x, pady=self.pad_y)

        # Lean Body Mass Calculator
        self.lean_body_calculator_image = Tk.CTkImage(Image.open("images/tools/arm.png"), size=(40, 40))
        self.lean_body_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                            text="LBM",
                                                            image=self.lean_body_calculator_image)
        self.lean_body_calculator_button.grid(row=2, column=0, padx=self.pad_x, pady=self.pad_y)

        # Healthy Weight Calculator
        self.healthy_weight_calculator_image = Tk.CTkImage(Image.open("images/tools/balanced-diet.png"), size=(40, 40))
        self.healthy_weight_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                                 text="Healthy Weight",
                                                                 image=self.healthy_weight_calculator_image)
        self.healthy_weight_calculator_button.grid(row=2, column=1, padx=self.pad_x, pady=self.pad_y)

        # Calories Burned Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/calories.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Fitness'),
                                                                  text="Cal. Burned",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=2, column=2, padx=self.pad_x, pady=self.pad_y)

        # Pregnancy Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/pregnancy.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Pregnancy'),
                                                                  text="Pregnancy",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y)

        # Pregnancy Gain Weight Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/gain-weight.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Pregnancy'),
                                                                  text="Gained Weight",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y)

        # Pregnancy Conception Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/conception.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Pregnancy'),
                                                                  text="Conception",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=2, padx=self.pad_x, pady=self.pad_y)

        # Due date Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/ovulation.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Pregnancy'),
                                                                  text="Ovulation",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=1, column=1, padx=self.pad_x, pady=self.pad_y)

        # Period Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/sanitary-pad.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Pregnancy'),
                                                                  text="Period",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y)

        # Nutrient Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/nutrition.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="Macro Nutrient",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y)

        # Carbohydrate Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/carbohydrates.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="Carbohydrate",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y)

        # Protein Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/protein.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="Protein",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=0, column=2, padx=self.pad_x, pady=self.pad_y)

        # Fat Intake Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/fats.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="Fat Intake",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y)

        # TDEE Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/tdee.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="TDEE",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=1, column=1, padx=self.pad_x, pady=self.pad_y)

        # GFR Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/membrane.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="GFR",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=1, column=2, padx=self.pad_x, pady=self.pad_y)

        # Body Type Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/body-variant.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="Body Type",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=2, column=0, padx=self.pad_x, pady=self.pad_y)

        # Body Surface Area Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/area-chart.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="BSA",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=2, column=1, padx=self.pad_x, pady=self.pad_y)

        # Blood Alcohol Concentration (BAC) Calculator
        self.calories_burned_calculator_image = Tk.CTkImage(Image.open("images/tools/drunk.png"), size=(40, 40))
        self.calories_burned_calculator_button = CalculatorButton(self.tabview.tab('Other'),
                                                                  text="BAC",
                                                                  image=self.calories_burned_calculator_image)
        self.calories_burned_calculator_button.grid(row=2, column=2, padx=self.pad_x, pady=self.pad_y)

        self.bmi_calculator_frame = BMICalculator(self, self.current_userid)

    # function to call the necessary calculator when an icon is selected
    def select_calculator_by_name(self, name, userid):
        if name == 'bmi':
            self.tabview.grid_forget()
            self.bmi_calculator_frame.clear_fields()
            self.bmi_calculator_frame.current_userid = userid
            self.bmi_calculator_frame.calculate_bmi()
            self.bmi_calculator_frame.grid(row=0, column=0)
        else:
            self.tabview.grid_forget()
        if name == 'tools':
            self.bmi_calculator_frame.grid_forget()
            self.bmi_calculator_frame.clear_fields()
            self.tabview.grid(row=1, column=1)
