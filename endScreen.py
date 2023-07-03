import tkinter as tk
from help import Help

class EndScreen:
    def __init__(self, root: tk, help: Help, game_controller) -> None:
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
        title_frame = tk.Frame(root, pady=10, bg=self.h.frame_colour)
        return title_frame

    def create_title_label(self, title_frame) -> None:
        label = tk.Label(title_frame, padx=10, pady=10, text=f"Player {self.h.player} has won!", font=(self.h.title_text_font, self.h.title_size), bg=self.h.title_colour)
        return label

    def create_button_frame(self, root) -> None:
        button_frame = tk.Frame(root, padx=10, pady=70, bg=self.h.frame_colour)
        return button_frame

    def create_button(self, frame, text, action):
        button = tk.Button(frame, width=15, height=1, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button

    def show(self) -> None:
        # winning message at the top
        self.winning_message_frame.pack()
        self.winning_message.pack()
        # buttons
        self.button_frame.pack()
        self.restart_with_same_settings_button.pack(pady=5)
        self.exit_to_menu_button.pack(pady=5)
        self.exit_the_game.pack(pady=5)
        
    def hide(self) -> None:
        # winning message at the top
        self.winning_message_frame.pack_forget()
        self.winning_message.pack_forget()
        # buttons
        self.restart_with_same_settings_button.pack_forget()
        self.exit_to_menu_button.pack_forget()
        self.exit_the_game.pack_forget()
        
    def destroy_widgets(self):
        # Destroy all the widgets
        self.winning_message_frame.destroy()
        self.winning_message.destroy()
        self.button_frame.destroy()
        self.restart_with_same_settings_button.destroy()
        self.exit_to_menu_button.destroy()
        self.exit_the_game.destroy()

    def exit_to_menu(self) -> None:
        self.game_controller.exit_to_menu()
        
    def restart_with_same_settings(self) -> None:
        self.game_controller.restart_with_same_settings()