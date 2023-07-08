import tkinter as tk
from help import Help

class MainMenu:
    """
    Class representing the main menu of the game.
    """
    def __init__(self, root: tk, help: Help, game_controller) -> None:
        """
        Initializes the MainMenu object with the provided root window, help object, and game controller.

        Args:
            root (tk.Tk): The root window of the application.
            help (Help): An instance of the Help class for managing game settings and messages.
            game_controller (object): The game controller object responsible for controlling the game flow.
        """
        self.h = help
        self.game_controller = game_controller
        self.create_menu_bar(root)
        self.title_frame = self.create_title_frame(root)
        self.title_label = self.create_title_label(self.title_frame)
        self.button_frame = self.create_button_frame(root)
        self.pvp_button = self.create_button(self.button_frame, "PvP", self.pvp_mode, 0, 0)
        self.pve_button = self.create_button(self.button_frame, "PvE", self.pve_mode, 0, 1)
        self.grid3_button = self.create_button(self.button_frame, "3x3", self.board3_change, 1, 0)
        self.grid5_button = self.create_button(self.button_frame, "5x5", self.board5_change, 1, 1)
        self.start_button_frame = self.create_start_button_frame(root)
        self.start_button = self.create_start_button(self.start_button_frame, "START", self.start_game, 1, 1)
        
    def create_start_button_frame(self, root):
        """
        Create a frame to contain the start button.

        Args:
            root (tk.Tk): The root window of the application.

        Returns:
            tk.Frame: The created frame for the start button.
        """
        start_button_frame = tk.Frame(root, padx=10, pady=10, bg=self.h.frame_colour)
        return start_button_frame
    
    def create_start_button(self, frame, text, action, row, column):
        """
        Create the start button with the provided parameters.

        Args:
            frame (tk.Frame): The frame to contain the start button.
            text (str): The text to be displayed on the start button.
            action (function): The function to be called when the start button is clicked.
            row (int): The row index of the start button in the grid.
            column (int): The column index of the start button in the grid.

        Returns:
            tk.Button: The created start button.
        """
        start_button = tk.Button(frame, width=7, height=3, text=text, bg=self.h.start_button_colour, command=action)
        start_button.configure(font=(self.h.start_button_text_colour, self.h.button_text_size))
        return start_button
    
    def create_button_frame(self, root) -> None:
        """
        Create a frame to contain the buttons.

        Args:
            root (tk.Tk): The root window of the application.

        Returns:
            tk.Frame: The created frame for the buttons.
        """
        button_frame = tk.Frame(root, padx=10, pady=10, bg=self.h.frame_colour)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        return button_frame
        
    def create_button(self, frame, text, action, row, column):
        """
        Create a button with the provided parameters.

        Args:
            frame (tk.Frame): The frame to contain the button.
            text (str): The text to be displayed on the button.
            action (function): The function to be called when the button is clicked.
            row (int): The row index of the button in the grid.
            column (int): The column index of the button in the grid.

        Returns:
            tk.Button: The created button.
        """
        button = tk.Button(frame, width=7, height=3, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button
        
    def create_title_frame(self, root) -> None:
        """
        Create a frame to contain the title label.

        Args:
            root (tk.Tk): The root window of the application.

        Returns:
            tk.Frame: The created frame for the title label.
        """
        title_frame = tk.Frame(root, pady=10, bg=self.h.frame_colour)
        return title_frame
        
    def create_title_label(self, title_frame) -> None:
        """
        Create the title label with the provided parameters.

        Args:
            title_frame (tk.Frame): The frame to contain the title label.

        Returns:
            tk.Label: The created title label.
        """
        title_label = tk.Label(title_frame, padx=10, pady=10, text="Main Menu", font=(self.h.title_text_font, self.h.title_size), bg=self.h.title_colour)
        return title_label
        
    def create_menu_bar(self, root) -> None:
        """
        Create the menu bar for the main menu window.

        Args:
            root (tk.Tk): The root window of the application.
        """
        bar = tk.Menu(root)
        root.config(menu=bar)
        options_menu = tk.Menu(bar)
        bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart", command=self.game_controller.exit_to_menu)
        options_menu.add_command(label="Exit", command=root.quit)
        
    def show(self) -> None:
        """
        Show the main menu and its widgets.
        """
        self.title_frame.pack()
        self.title_label.pack()
        self.start_button_frame.place(relx=.65, rely=.4)
        self.start_button.grid(row=1, column=1, pady=5, padx=5)
        self.button_frame.place(relx=0.33, rely=.55, anchor="center")
        self.pvp_button.grid(row=0, column=0, pady=5, padx=5)
        self.pve_button.grid(row=0, column=1, pady=5, padx=5)
        self.grid3_button.grid(row=1, column=0, pady=5, padx=5)
        self.grid5_button.grid(row=1, column=1, pady=5, padx=5)
        
    def hide(self) -> None:
        """
        Hide the main menu and its widgets.
        """
        self.title_frame.pack_forget()
        self.title_label.pack_forget()
        self.start_button_frame.forget()
        self.start_button.grid_forget()
        self.button_frame.forget()
        self.pvp_button.grid_forget()
        self.pve_button.grid_forget()
        self.grid3_button.grid_forget()
        self.grid5_button.grid_forget()
        
    def destroy_widgets(self) -> None:
        """
        Destroy all the widgets in the main menu.
        """
        self.title_frame.destroy()
        self.title_label.destroy()
        self.start_button_frame.destroy()
        self.start_button.destroy()
        self.button_frame.destroy()
        self.pvp_button.destroy()
        self.pve_button.destroy()
        self.grid3_button.destroy()
        self.grid5_button.destroy()

    def pvp_mode(self) -> None:
        """
        Set the game mode to Player vs Player (PvP).
        """
        self.pvp_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pve_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_game_mode("PvP")

    def pve_mode(self) -> None:
        """
        Set the game mode to Player vs Environment (PvE).
        """
        self.pve_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.pvp_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_game_mode("PvE")

    def board3_change(self) -> None:
        """
        Change the game board size to 3x3.
        """
        self.grid3_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid5_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_gameBoard_size("3")

    def board5_change(self) -> None:
        """
        Change the game board size to 5x5.
        """
        self.grid5_button.configure(bg=self.h.button_colour_clicked, fg=self.h.button_text_colour_clicked)
        self.grid3_button.configure(bg=self.h.button_colour_inactive, fg=self.h.button_text_colour_inactive)
        self.game_controller.change_gameBoard_size("5")

    def start_game(self):
        """
        Start the game.
        """
        self.game_controller.start_game()