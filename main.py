import tkinter as tk
from PIL import ImageTk, Image
from tk_func import SystemControl, Quiz
from planet import planet_dict

def main():
    root = tk.Tk()
    root.title("Solar System Explorer")
    root.geometry("1040x600")
    root.resizable(False, False)

    # Creation of the canvas
    # https://stackoverflow.com/questions/13212300/how-to-reconfigure-tkinter-canvas-items
    canvas = tk.Canvas(root, width=1040, height=600)
    canvas.pack()

    # Loading the background
    solar_bg = ImageTk.PhotoImage(Image.open("solar_bg.png"))
    canvas.create_image(0, 0, anchor="nw", image=solar_bg)

    # Creation of the SystemControl instance
    controller = SystemControl()

    text1 = canvas.create_text(520, 100,
                               text="Hello! Would you like to know more about the planets of our solar system?",
                               fill="#000000",
                               font=("Arial", 17, "bold"),
                               width=1000)

    text2 = canvas.create_text(520, 300,
                               text="LET'S GET STARTED!",
                               fill="#000000",
                               font=("Arial", 32, "bold"),
                               width=1000)

    # Use the fade-in effect of the SystemControl instance on text 1 and 2, and show_start_button methods
    controller.fade_in(canvas, text1)
    root.after(2000, lambda: controller.fade_in(canvas, text2))
    root.after(4000, lambda: controller.show_start_button(root, canvas, solar_bg, tk, controller))

    root.mainloop()

if __name__ == "__main__":
    main()


'''
This project was powered by the following resources:

Python Documentation:
https://docs.python.org/3/
Used for understanding core Python syntax and language features.

Tkinter Documentation:
https://docs.python.org/3/library/tkinter.html
https://tkinter-docs.readthedocs.io/en/latest/
https://tkdocs.com/tutorial/index.html
Used extensively to build the GUI for user interactions.

NASA Planetary Data:
https://solarsystem.nasa.gov/planets/overview/
Reliable scientific data was sourced here for accurate values of mass, orbit, etc.

Wikipedia - Planet Information:
https://en.wikipedia.org/wiki/Solar_System
Used to cross-verify and simplify data for educational purposes.

Stack Overflow Discussions:
Many solutions and syntax clarifications came from the Python community on Stack Overflow. Specific thread references are included as comments within the .py files.

TutorialsPoint:
Basic tutorial of color configuration in tkinter.
https://www.tutorialspoint.com/python/tk_colors.htm
https://www.tutorialspoint.com/how-to-change-the-color-of-everything-in-a-tkinter-gui

YouTube:
https://www.youtube.com/@TkinterPython
This Youtube channel contains huge amount of tutorials about Tkinter library
https://www.youtube.com/watch?v=k8JI7vk2Tbw
This video provides insights of the text fade-in effect
https://www.youtube.com/watch?v=YXPyB4XeYLA&t=12096s
The Tkinter tutorial video by freeCodeCamp I have been using for seeking insights and ideas

ChatGPT:
https://chatgpt.com/share/683c2d52-90e8-8002-9758-6b27163d3a42
I have consulted CHATGPT about the logic and feasibility of some functions in the program, especially the fade in effect

GeeksforGeeks:
https://www.geeksforgeeks.org/python-tkinter-tutorial/
https://www.geeksforgeeks.org/python-focus_set-and-focus_get-method/
https://www.geeksforgeeks.org/how-to-bind-the-enter-key-to-a-tkinter-window/
https://www.geeksforgeeks.org/how-to-clear-the-entry-widget-after-button-press-in-tkinter/
Posts that discuss some in-programme operations: focus_set(), entry.bind() and entry.delete()

Image Credit:
https://www.nasa.gov/wp-content/uploads/2023/03/119527main_image_feature_357_ys_full.jpg
Background image from NASA/JPL-Caltech/T. Pyle (SSC)
I manually adjusted the brightness, contrast, and color tone to make it better fit the GUI interface.
Source: NASA/JPL Caltech
'''
