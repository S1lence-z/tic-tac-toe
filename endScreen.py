import tkinter as tk
from help import Help

class EndScreen:
    """
    Represents the end screen of the TicTacToe game.
    
    Attributes:
        h (Help): An instance of the Help class that provides configuration settings.
        game_controller: The game controller object that controls the game flow.
        button_frame: The frame that holds the buttons.
        winning_message_frame: The frame that holds the winning message label.
        winning_message: The label that displays the winning message.
        restart_with_same_settings_button: The button to restart the game with the same settings.
        exit_to_menu_button: The button to exit to the main menu.
        exit_the_game: The button to exit the game completely.
    """
    
    def __init__(self, root: tk, help: Help, game_controller) -> None:
        """
        Initializes the EndScreen instance.
        
        Args:
            root (tk): The root tkinter object.
            help (Help): An instance of the Help class that provides configuration settings.
            game_controller: The game controller object that controls the game flow.
        """
        self.h = help
        self.game_controller = game_controller
        self.button_frame = self.create_button_frame(root)
        self.winning_message_frame = self.create_title_frame(root)
        self.winning_message = self.create_title_label(self.winning_message_frame)
        # all buttons to be present
        self.restart_with_same_settings_button = self.create_button(self.button_frame, "Restart", self.restart_with_same_settings)
        self.exit_to_menu_button = self.create_button(self.button_frame, "Exit To Menu", self.exit_to_menu)
        self.exit_the_game = self.create_button(self.button_frame, "Exit Game", root.quit)
        
    def create_title_frame(self, root) -> None:
        """
        Creates and returns the title frame.
        
        Args:
            root: The root tkinter object.
            
        Returns:
            The created title frame.
        """
        title_frame = tk.Frame(root, pady=10, bg=self.h.frame_colour)
        return title_frame

    def create_title_label(self, title_frame) -> None:
        """
        Creates and returns the title label.
        
        Args:
            title_frame: The title frame where the label will be placed.
            
        Returns:
            The created title label.
        """
        label = tk.Label(title_frame, padx=10, pady=10, font=(self.h.title_text_font, self.h.title_size), bg=self.h.title_colour)
        return label

    def create_button_frame(self, root) -> None:
        """
        Creates and returns the button frame.
        
        Args:
            root: The root tkinter object.
            
        Returns:
            The created button frame.
        """
        button_frame = tk.Frame(root, padx=10, pady=70, bg=self.h.frame_colour)
        return button_frame

    def create_button(self, frame, text, action) -> tk.Button:
        """
        Creates and returns a button.
        
        Args:
            frame: The frame where the button will be placed.
            text: The text displayed on the button.
            action: The function to be executed when the button is clicked.
            
        Returns:
            The created button.
        """
        button = tk.Button(frame, width=15, height=1, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button

    def show(self, label_text) -> None:
        """
        Displays the end screen with the specified winning message.
        
        Args:
            label_text: The winning message to be displayed.
        """
        # winning message at the top
        self.winning_message_frame.pack()
        self.winning_message.configure(text=label_text)
        self.winning_message.pack()
        # buttons
        self.button_frame.pack()
        self.restart_with_same_settings_button.pack(pady=5)
        self.exit_to_menu_button.pack(pady=5)
        self.exit_the_game.pack(pady=5)
        
    def hide(self) -> None:
        """
        Hides the end screen.
        """
        # winning message at the top
        self.winning_message_frame.pack_forget()
        self.winning_message.pack_forget()
        # buttons
        self.restart_with_same_settings_button.pack_forget()
        self.exit_to_menu_button.pack_forget()
        self.exit_the_game.pack_forget()
        
    def destroy_widgets(self) -> None:
        """
        Destroys all the widgets in the end screen.
        """
        self.winning_message_frame.destroy()
        self.winning_message.destroy()
        self.button_frame.destroy()
        self.restart_with_same_settings_button.destroy()
        self.exit_to_menu_button.destroy()
        self.exit_the_game.destroy()

    def exit_to_menu(self) -> None:
        """
        Exits the game and returns to the main menu.
        """
        self.game_controller.exit_to_menu()
        
    def restart_with_same_settings(self) -> None:
        """
        Restarts the game with the same settings.
        """
        self.game_controller.restart_with_same_settings()