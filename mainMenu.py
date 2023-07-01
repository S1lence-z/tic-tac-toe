import tkinter as tk
from help import Help

class MainMenu:
    def __init__(self, root):
        h = Help()
        self.h = h
        title_frame = tk.Frame(root, pady=10, bg=h.frame_colour)
        title_frame.pack()

        # Main menu frame
        self.title = tk.Label(title_frame, padx=10, pady=10, text="Main Menu", font=(h.button_text_font, h.title_size), bg=h.title_colour)
        self.title.pack()

        # main menu window, the little stripe at the top of the page
        lista = tk.Menu(root)
        root.config(menu=lista)
        options_menu = tk.Menu(lista)
        lista.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart")
        options_menu.add_command(label="Exit", command=root.quit)
       
        # A grid for all the settings buttons, PvP, PvE, 3x3, 4x4
        buttonframe = tk.Frame(root, padx = 10, pady = 10, bg=h.frame_colour)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.place(relx=0.33, rely=.55, anchor="center")
        
        # A button for PvP
        self.pvp_button = tk.Button(buttonframe, width = 14, height=7, text="PvP", bg=h.button_colour, command=self.action0)
        self.pvp_button.configure(font=(h.button_text_font, h.button_text_size))
        self.pvp_button.grid(row=0, column=0, pady=5)
        
        # A button for PvE
        self.pve_button = tk.Button(buttonframe, width = 14, height=7, text="PvE", bg=h.button_colour, command=self.action1)
        self.pve_button.configure(font=(h.button_text_font, h.button_text_size))
        self.pve_button.grid(row=0, column=1, pady=5, padx=5)

        # A button for 3x3
        self.grid3_button = tk.Button(buttonframe, width=14, height=7, text="3x3", bg=h.button_colour, command=self.action2)
        self.grid3_button_button.configure(font=(h.button_text_font, h.button_text_size))
        self.grid3_button.grid(row=1, column=0, pady=5, padx=5)

        # A button for 4x4
        self.grid4_button = tk.Button(buttonframe, width=14, height=7, text="4x4", bg=h.button_colour, command=self.action3)
        self.grid4_button.configure(font=(h.button_text_font, h.button_text_size))
        self.grid4_button.grid(row=1, column=1, pady=5, padx=5)

        # Grid pro startovací tlačítko
        start_button_frame = tk.Frame(root, padx=10, pady=10, bg=h.frame_colour)
        start_button_frame.place(relx=.65, rely=.4)
        # Start button
        self.start_button = tk.Button(start_button_frame, width=14, height=7, text="START", fg=h.text_button_colour, bg=h.button_colour, command=self.action4)
        self.start_button.configure(font=(h.button_text_font, h.button_text_size))
        self.start_button.grid(row=1, column=1, pady=5, padx=5)

    # action functions to configure what each button does
    def action0(self):
        self.pvp_button.configure(bg=self.h.button_colour_clicked)
        self.pve_button.configure(bg=self.h.button_colour_inactive)

    def action1(self):
        self.pve_button.configure(bg=self.h.button_colour_clicked)
        self.pvp_button.configure(bg=self.h.button_colour_inactive)

    def action2(self):
        self.grid3_button.configure(bg=self.h.button_colour_clicked)
        self.grid4_button.configure(bg=self.h.button_colour_inactive)

    def action3(self):
        self.grid4_button.configure(bg=self.h.button_colour_clicked)
        self.grid3_button.configure(bg=self.h.button_colour_inactive)

    def action4(self):
        self.start_button.configure(bg=self.h.button_colour_clicked)