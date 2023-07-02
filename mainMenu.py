import tkinter as tk
from help import Help

class MainMenu:
    def __init__(self, root: tk, help: Help()) -> None:
        self.h = help
        self.create_title_frame(root, help)
        self.create_menu_bar(root)
        # create a frame and buttons to control game settings
        button_frame = self.create_button_frame(root)
        self.pvp_button = self.create_button(button_frame, "PvP", self.action0, 0, 0)
        self.pve_button = self.create_button(button_frame, "PvE", self.action1, 0, 1)
        self.grid3_button = self.create_button(button_frame, "3x3", self.action2, 1, 0)
        self.grid4_button = self.create_button(button_frame, "4x4", self.action3, 1, 1)
        # create a frame and the start button
        start_button_frame = self.create_start_button_frame(root)
        self.start_button = self.create_start_button(start_button_frame, "START", self.action4, 1, 1)
        
    def create_start_button_frame(self, root):
        start_button_frame = tk.Frame(root, padx=10, pady=10, bg=self.h.frame_colour)
        start_button_frame.place(relx=.65, rely=.4)
        return start_button_frame
    
    def create_start_button(self, frame, text, action, row, column):
        start_button = tk.Button(frame, width=14, height=7, text=text, bg=self.h.start_button_colour, command=action)
        start_button.configure(font=(self.h.start_button_text_colour, self.h.button_text_size))
        start_button.grid(row=row, column=column, pady=5, padx=5)
        return start_button
    
    def create_button_frame(self, root) -> None:
        button_frame = tk.Frame(root, padx = 10, pady = 10, bg=self.h.frame_colour)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.place(relx=0.33, rely=.55, anchor="center")
        return button_frame
        
    def create_button(self, frame, text, action, row, column):
        button = tk.Button(frame, width=14, height=7, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        button.grid(row=row, column=column, pady=5, padx=5)
        return button
        
    def create_title_frame(self, root, h) -> None:
        title_frame = tk.Frame(root, pady=10, bg=h.frame_colour)
        title_frame.pack()

        # Main menu frame
        self.title = tk.Label(title_frame, padx=10, pady=10, text="Main Menu", font=(h.title_text_font, h.title_size), bg=h.title_colour)
        self.title.pack()
        
    def create_menu_bar(self, root) -> None:
        # main menu window, the little stripe/bar at the top of the page
        bar = tk.Menu(root)
        root.config(menu=bar)
        
        options_menu = tk.Menu(bar)
        bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart")
        options_menu.add_command(label="Exit", command=root.quit)
        

    # action functions to configure what each button does
    def action0(self) -> None:
        self.pvp_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pve_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)

    def action1(self) -> None:
        self.pve_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pvp_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)

    def action2(self) -> None:
        self.grid3_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid4_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)

    def action3(self) -> None:
        self.grid4_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid3_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)

    def action4(self) -> None:
        self.start_button.configure(bg=self.h.button_colour_clicked)