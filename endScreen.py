import _tkinter as tk
from help import Help

class EndScreen:
    def __init__(self, root: tk, help: Help) -> None:
        self.h = help
        self.button_frame = self.create_button_frame(root)
        # all buttons to be present
        self.restart_with_same_settings_button = self.create_button(root, "Restart", self.test, 0, 0)
        self.exit_to_menu_button = self.create_button(root, "Exit To Menu", self.test, 1, 0)
        self.exit_the_game = self.create_button(root, "Exit Game", self.test, 1, 0)
        
    def create_button_frame(self, root) -> None:
        button_frame = tk.Frame(root, padx = 10, pady = 10, bg=self.h.frame_colour)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        return button_frame
        
    def create_button(self, frame, text, action, row, column):
        button = tk.Button(frame, width=7, height=3, text=text, bg=self.h.button_colour, command=action)
        button.configure(font=(self.h.button_text_font, self.h.button_text_size))
        return button

    def show(self) -> None:
        self.button_frame.place(relx=0.33, rely=.55, anchor="center")
        self.restart_with_same_settings_button.grid(row=0, column=0, pady=5, padx=5)
        self.exit_to_menu_button.grid(row=0, column=1, pady=5, padx=5)
        self.exit_the_game.grid(row=1, column=0, pady=5, padx=5)
        
    def test(self) -> None:
        return self.show()