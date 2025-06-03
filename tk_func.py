from planet import planet_dict, Planet

# Set-up of the parent class
class PageElements:
    def __init__(self, root, canvas, solar_bg, tk, planet_instance, controller):
        self.root = root
        self.canvas = canvas
        self.tk = tk
        self.solar_bg = solar_bg
        self.planet = planet_instance
        self.controller = controller

# The Quiz class: the second page of the app
class Quiz(PageElements):
    def __init__(self, root, canvas, solar_bg, tk, planet_instance, controller):
        super().__init__(root, canvas, solar_bg, tk, planet_instance, controller)        
        self.user_answer = self.tk.StringVar() # place-holder of the user input

    # Initiating the small quiz
    def init_quiz(self):
        self.controller.reset_screen(self.canvas, self.solar_bg)
        self.quiz_text_id = self.canvas.create_text(
            520, 240,
            text="Quick Quiz\n\nDo you know how many PLANETS are there \n\nin our solar system?",
            fill="white",
            font=("Arial", 24, "bold"),
            justify="center"
        )
        # Creation of the entry box object
        self.entry = self.tk.Entry(self.root, 
                                   textvariable=self.user_answer, 
                                   font=("Arial", 16), 
                                   justify="center")
        self.canvas.create_window(520, 400, window=self.entry, width=100)
        self.entry.bind("<Return>", lambda event: self.check_answer()) # Bind the Return key on check_answer calling
        self.entry.focus_set() # Set the selection focus on the entry box

        self.submit_btn = self.tk.Button(self.root, 
                                         text="Submit", 
                                         font=("Arial", 14), 
                                         command=self.check_answer)
        self.canvas.create_window(520, 450, window=self.submit_btn)

    # Check the quiz answer
    def check_answer(self):
        answer = self.user_answer.get().strip().lower()

        if answer == "8": # Directing to the Transitional page
            self.controller.reset_screen(self.canvas, self.solar_bg)
            self.canvas.create_text(520, 200,
                                    text="Excellent! There are 8 planets in our solar system.",
                                    fill="white", 
                                    font=("Arial", 20, "bold"),
                                    justify="center")
            
            next_btn = self.tk.Button(self.root, text="Next Page",
                                    font=("Arial", 16, "bold"),
                                    command=lambda: self.controller.goto_menu(self.root, self.canvas, self.solar_bg, self.tk, self.planet))
            self.canvas.create_window(400, 400, window=next_btn, width=150)
            
            quit_btn = self.controller.create_quit_btn(self.root, self.canvas, 
                                                    self.tk, self.solar_bg)
            self.canvas.create_window(640, 400, window=quit_btn, width=150)

        elif answer == "quit":
            self.controller.quit_app(self.root, self.canvas, self.solar_bg)

        else:
            self.canvas.create_text(520, 500,
                                    text="Oops! That's not correct. Try again or type 'quit' to exit.",
                                    fill="red", font=("Arial", 14, "italic"),
                                    justify="center")
            self.entry.delete(0, self.tk.END) # Delete the input if it is not correct


# Set-up of the child class of planet selection
class PlanetSelection(PageElements):
    def __init__(self, root, canvas, solar_bg, tk, planet_instance, controller):
        super().__init__(root, canvas, solar_bg, tk, 
                         planet_instance, controller)
        self.message_text_id = None    
        self.create_widgets() # Call the "create_widgets()" method once the lambda function controller.goto_menu() is called when the "Next Page" button on the transitiona page is clicked

    def create_widgets(self):
        self.controller.reset_screen(self.canvas, self.solar_bg)

        menu_text = self.canvas.create_text(
            520, 240, 
            text="Planets in our solar system:\n\n\nMercury\tVenus\tEarth\tMars\n\nJupiter\tSaturn\tUranus\tNeptune",
            fill="white", 
            font=("Arial", 24, "bold"), 
            justify="center"
        )
        self.controller.fade_in(self.canvas, menu_text)

        self.planet_entry = self.tk.Entry(self.root, 
                                          font=("Arial", 16), justify="center")
        self.canvas.create_window(520, 420, window=self.planet_entry, width=300)

        submit_btn = self.tk.Button(self.root, text="SUBMIT", 
                                    font=("Arial", 14, "bold"),
                                    bg="#ffffff", 
                                    fg="#000000", 
                                    command=self.process_input)
        self.canvas.create_window(520, 470, window=submit_btn)

        self.planet_entry.bind("<Return>", lambda event: self.process_input())
    
    def show_message(self, text, color="white"):
        if self.message_text_id is not None:
            self.canvas.delete(self.message_text_id) # Prevent canvas from overlapping messages
        self.message_text_id = self.canvas.create_text(
            520, 520,
            text=text,
            fill=color,
            font=("Arial", 14, "bold"))
        
    def process_input(self):
        planet_name = self.planet_entry.get().strip().capitalize() # Place-holder of user input

        if planet_name == "Pluto":
            self.show_message("Pluto is no longer officially classified as a planet.", "orange")
            self.planet_entry.delete(0, self.tk.END)
            return

        if planet_name in self.controller.get_valid_planets():
            self.planet = self.controller.create_planet(planet_name) # Create a planet instance
            self.show_message(f"{planet_name} is selected. What would you like to know?", "white")

            MethodSelection(self.root, self.canvas, self.solar_bg, 
                            self.tk, self.planet, self.controller)
        
        elif planet_name == "Quit":
            self.controller.quit_app(self.root, self.canvas, self.solar_bg)

        else:
            self.show_message("Invalid planet name. Please try again.", "red")
            self.planet_entry.delete(0, self.tk.END)

# Set-up of the child class of the Method Selection Page
class MethodSelection(PageElements):
    def __init__(self, root, canvas, solar_bg, tk, planet_instance, controller):
        super().__init__(root, canvas, solar_bg, tk, planet_instance, controller)
        self.selection = self.tk.StringVar()
        self.method_selection() # Call Dropdown Menu in the method_selection method directly

    def method_selection(self):
        self.controller.reset_screen(self.canvas, self.solar_bg)

        label = self.canvas.create_text(
            520, 180,
            text="Select planet information to display:",
            fill="white",
            font=("Arial", 18, "bold")
        )

        options = [
            "Tell me everything about the planet",
            "How massive is the planet?",
            "Diameter (km)",        
            "Distance from the Sun",
            "Rotation period (hours)",
            "Orbital period (days)",
            "Number of moons",
            "Temperature (K)"
        ]

        self.selection.set(options[0]) # Initiation of the dropdown menu
        dropdown = self.tk.OptionMenu(self.root, self.selection, 
                                      *options, command=self.on_select)
        self.canvas.create_window(520, 80, window=dropdown, width=300)

        self.result_display = ResultDisplay(self.root, self.canvas, 
                                            self.solar_bg, 
                                            self.tk, 
                                            self.planet, 
                                            self.controller)

        quit_btn = self.controller.create_quit_btn(self.root, self.canvas, 
                                                 self.tk, self.solar_bg)
        self.canvas.create_window(520, 550, window=quit_btn, width=150)

        back_btn = self.tk.Button(self.root, text="Back to Planets", 
                                  font=("Arial", 14, "bold"),
                                  command=lambda: self.controller.goto_menu(self.root, self.canvas, self.solar_bg, self.tk, self.planet))
        self.canvas.create_window(520, 500, window=back_btn, width=150)

    def on_select(self, value): # Define the function to display planet info on the selection in dropdown menu
        self.result_display.display_info(value)

# Set-up the child class of the Result Display Element on Method Selection Page
class ResultDisplay(PageElements):
    def __init__(self, root, canvas, solar_bg, tk, planet_instance, controller):
        super().__init__(root, canvas, solar_bg, 
                         tk, planet_instance, controller)    
        self.text_id = None

    def display_info(self, selection):
        if selection == "Tell me everything about the planet":
            info = self.planet.everything()
        elif selection == "How massive is the planet?":
            info = self.planet.get_mass()
        elif selection == "Distance from the Sun":
            info = self.planet.get_distance()
        elif selection == "Number of moons":
            info = self.planet.get_moon()
        elif selection == "Rotation period (hours)":
            info = self.planet.get_rotation()
        elif selection == "Orbital period (days)":
            info = self.planet.get_orbit()
        elif selection == "Diameter (km)":
            info = self.planet.get_diameter()
        elif selection == "Temperature (K)":
            info = self.planet.get_temperature()
        else:
            info = "No information available."

        if self.text_id is not None:
            self.canvas.delete(self.text_id) # Prevent canvas from overlapping messages

        self.text_id = self.canvas.create_text(
            520, 300, text=info, fill="white",
            font=("Arial", 16), width=600, justify="center"
        )

# Set-up System control class
class SystemControl:
    def __init__(self):
        self.solar_bg = None  

    # I am inspired by the below posts in stackoverflow when dealing with fade in and button colors.
    # https://stackoverflow.com/questions/44170185/fade-widgets-or-pictures-in-and-out-tkinter/44180478#44180478
    # https://stackoverflow.com/questions/11340765/default-window-colour-tkinter-and-hex-colour-codes

    def fade_in(self, widget_or_canvas, item=None, alpha=0, reverse=False):
        if alpha > 1:
            return
        gray_level = int(255 * (1 - alpha) if reverse else 255 * alpha)
        color = f"#{gray_level:02x}{gray_level:02x}{gray_level:02x}"

        if item is None:
            widget_or_canvas.config(fg=color)
        else:
            widget_or_canvas.itemconfig(item, fill=color)

        widget_or_canvas.after(50, lambda: self.fade_in(widget_or_canvas, item, alpha + 0.05, reverse))

    def reset_screen(self, canvas, solar_bg):
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=solar_bg)

    def quit_app(self, root, canvas, solar_bg):
        self.reset_screen(canvas, solar_bg)

        message = "See you next time!"
        text_id = canvas.create_text(400, 300, text=message, 
                                     font=("Arial", 24), fill="#000000")
        self.fade_in(canvas, item=text_id, alpha=0)
        canvas.after(2500, root.destroy)

    def goto_menu(self, root, canvas, solar_bg, tk, planet):
        self.reset_screen(canvas, solar_bg)
        PlanetSelection(root, canvas, solar_bg, tk, planet, self)

    def get_valid_planets(self):
        return planet_dict.keys()

    def create_planet(self, name):
        return Planet(name) if name in planet_dict else None
    
    def create_quit_btn(self, root, canvas, tk, solar_bg):
        quit_btn = tk.Button(root, text="Quit",
                        font=("Arial", 16, "bold"),
                        command=lambda: self.quit_app(root, canvas, solar_bg))
        return quit_btn

    def show_start_button(self, root, canvas, solar_bg, tk, planet_instance):
        def start_quiz():
            quiz = Quiz(root, canvas, solar_bg, tk, planet_instance, self)
            quiz.init_quiz()
        start_btn = tk.Button(root,
                            bg="#000000",
                            fg="#000000",
                            bd=0,
                            text="START",
                            font=("Arial", 20, "bold"),
                            command=lambda: start_quiz())
        canvas.create_window(520, 500, window=start_btn)