import tkinter as tk
from help import Help

class EndScreen:
    def __init__(self, root: tk, help: Help, game_controller) -> None:
        self.h = help
        self.button_frame = self.create_button_frame(root)
        # all buttons to be present
        self.restart_with_same_settings_button = self.create_button(self.button_frame, "Restart", self.test)
        self.exit_to_menu_button = self.create_button(self.button_frame, "Exit To Menu", self.test)
        self.exit_the_game = self.create_button(self.button_frame, "Exit Game", self.test)

    def create_button_frame(self, root) -> None:
        button_frame = tk.Frame(root, padx=10, pady=10, bg=self.h.frame_colour)
        button_frame.pack(fill=tk.BOTH, expand=True)
        return button_frame

    def create_button(self, frame, text, action):
        button = tk.Button(frame, width=7, height=3, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button

    def show(self) -> None:
        self.restart_with_same_settings_button.pack(pady=5)
        self.exit_to_menu_button.pack(pady=5)
        self.exit_the_game.pack(pady=5)
        
    def hide(self) -> None:
        self.restart_with_same_settings_button.pack_forget()
        self.exit_to_menu_button.pack_forget()
        self.exit_the_game.pack_forget()

    def test(self) -> None:
        return