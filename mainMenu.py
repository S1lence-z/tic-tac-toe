import tkinter as tk
from help import Help

class MainMenu:
    def __init__(self, root: tk, help: Help, game_controller) -> None:
        self.h = help
        self.game_controller = game_controller
        self.create_menu_bar(root)
        # main menu title
        self.title_frame = self.create_title_frame(root)
        self.title_label = self.create_title_label(self.title_frame)        
        # create a frame and buttons to control game settings
        self.button_frame = self.create_button_frame(root)
        self.pvp_button = self.create_button(self.button_frame, "PvP", self.pvp_mode, 0, 0)
        self.pve_button = self.create_button(self.button_frame, "PvE", self.pve_mode, 0, 1)
        self.grid3_button = self.create_button(self.button_frame, "3x3", self.board3_change, 1, 0)
        self.grid4_button = self.create_button(self.button_frame, "4x4", self.board4_change, 1, 1)
        # create a frame and the start button
        self.start_button_frame = self.create_start_button_frame(root)
        self.start_button = self.create_start_button(self.start_button_frame, "START", self.start_game, 1, 1)
        
    def create_start_button_frame(self, root):
        start_button_frame = tk.Frame(root, padx=10, pady=10, bg=self.h.frame_colour)
        return start_button_frame
    
    def create_start_button(self, frame, text, action, row, column):
        start_button = tk.Button(frame, width=10, height=5, text=text, bg=self.h.start_button_colour, command=action)
        start_button.configure(font=(self.h.start_button_text_colour, self.h.button_text_size))
        return start_button
    
    def create_button_frame(self, root) -> None:
        button_frame = tk.Frame(root, padx = 10, pady = 10, bg=self.h.frame_colour)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        return button_frame
        
    def create_button(self, frame, text, action, row, column):
        button = tk.Button(frame, width=10, height=5, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button
        
    def create_title_frame(self, root) -> None:
        title_frame = tk.Frame(root, pady=10, bg=self.h.frame_colour)
        return title_frame
        
    def create_title_label(self, title_frame) -> None:
        title_label = tk.Label(title_frame, padx=10, pady=10, text="Main Menu", font=(self.h.title_text_font, self.h.title_size), bg=self.h.title_colour)
        return title_label
        
    def create_menu_bar(self, root) -> None:
        # main menu window, the little stripe/bar at the top of the page
        bar = tk.Menu(root)
        root.config(menu=bar)
        options_menu = tk.Menu(bar)
        bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart")
        options_menu.add_command(label="Exit", command=root.quit)
        
    def show(self) -> None:
        # the main menu title
        self.title_frame.pack()
        self.title_label.pack()
        # start frame and start button
        self.start_button_frame.place(relx=.65, rely=.4)
        self.start_button.grid(row=1, column=1, pady=5, padx=5)
        # the frame for other buttons and the buttons themselves
        self.button_frame.place(relx=0.33, rely=.55, anchor="center")
        self.pvp_button.grid(row=0, column=0, pady=5, padx=5)
        self.pve_button.grid(row=0, column=1, pady=5, padx=5)
        self.grid3_button.grid(row=1, column=0, pady=5, padx=5)
        self.grid4_button.grid(row=1, column=1, pady=5, padx=5)
        
    def hide(self) -> None:
        # the main menu title
        self.title_frame.pack_forget()
        self.title_label.pack_forget()
        # start frame and start button
        self.start_button_frame.forget()
        self.start_button.grid_forget()
        # the frame for other buttons and the buttons themselves
        self.button_frame.forget()
        self.pvp_button.grid_forget()
        self.pve_button.grid_forget()
        self.grid3_button.grid_forget()
        self.grid4_button.grid_forget()

    # action functions to configure what each button does
    def pvp_mode(self) -> None:
        self.pvp_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pve_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_game_mode("PvP")

    def pve_mode(self) -> None:
        self.pve_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pvp_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_game_mode("PvE")

    def board3_change(self) -> None:
        self.grid3_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid4_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_gameBoard_size("3")

    def board4_change(self) -> None:
        self.grid4_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid3_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_gameBoard_size("4")

    def start_game(self):
        self.game_controller.show_gameBoard()