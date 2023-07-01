import tkinter as tk
import random

font1 = "Arial"
font1_size = 12
title_size = 20
button_colour = "green"
button_colour_clicked = "red"
button_colour_inactive = "black"
text_button_colour = "blue"
frame_colour = "grey"
title_colour = "white"
# je třeba unifikovat title frame na obou stránkách, ať ho v každé nemusím zavádět zvlášť
# je třeba vytvořit clasu na všechna tato jednotlivá nastavení

players = ["X", "O"]
player = random.choice(players)
board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

class MainMenu:
    def __init__(self, root):
        title_frame = tk.Frame(root, pady=10, bg=frame_colour)
        title_frame.pack()

        # Tohle je můj hlavní frame, ve kterém vše leží
        self.title = tk.Label(title_frame, padx=10, pady=10, text="Main Menu", font=(font1, title_size), bg=title_colour)
        self.title.pack()

        # Menu pro ukončení a restart 
        lista = tk.Menu(root)
        root .config(menu=lista)
        options_menu = tk.Menu(lista)
        lista.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart")
        options_menu.add_command(label="Exit", command=root.quit)
       
        # Grid pro tlačítka nastavující hru
        buttonframe = tk.Frame(root, padx = 10, pady = 10, bg=frame_colour)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.place(relx=0.33, rely=.55, anchor="center")
        
        # Tlačítko pro PVP
        self.pvp_button = tk.Button(buttonframe, width = 14, height=7,  text="PvP", font=(font1, font1_size), bg=button_colour,command=self.action0)
        self.pvp_button.grid(row=0, column=0, pady=5)
        
        # Tlačítko pro PVE
        self.pve_button = tk.Button(buttonframe, width = 14, height=7, text="PvE", font=(font1, font1_size), bg=button_colour, command=self.action1)
        self.pve_button.grid(row=0, column=1, pady=5, padx=5)

        # Tlačítko pro 3x3
        self.grid3_button = tk.Button(buttonframe, width=14, height=7, text="3x3", font=(font1, font1_size), bg=button_colour, command=self.action2)
        self.grid3_button.grid(row=1, column=0, pady=5, padx=5)

        # Tlačítko pro 4x4
        self.grid4_button = tk.Button(buttonframe, width=14, height=7, text="4x4", font=(font1, font1_size), bg=button_colour, command=self.action3)
        self.grid4_button.grid(row=1, column=1, pady=5, padx=5)

        # Grid pro startovací tlačítko
        start_button_frame = tk.Frame(root, padx=10, pady=10, bg=frame_colour)
        start_button_frame.place(relx=.65, rely=.4)

        # Startovací tlačítko
        self.start_button = tk.Button(start_button_frame, width=14, height=7, text="START", font=(font1, font1_size), fg=text_button_colour,bg=button_colour, command=self.action4)
        self.start_button.grid(row=1, column=1, pady=5, padx=5)

    # Jednotlivé funkce na změnu barvy + lze sem i přidat funkce na nastavení herního pole?
    def action0(self):
        self.pvp_button.configure(bg=button_colour_clicked)
        self.pve_button.configure(bg=button_colour_inactive)

    def action1(self):
        self.pve_button.configure(bg=button_colour_clicked)
        self.pvp_button.configure(bg=button_colour_inactive)

    def action2(self):
        self.grid3_button.configure(bg=button_colour_clicked)
        self.grid4_button.configure(bg=button_colour_inactive)

    def action3(self):
        self.grid4_button.configure(bg=button_colour_clicked)
        self.grid3_button.configure(bg=button_colour_inactive)

    def action4(self):
        self.start_button.configure(bg=button_colour_clicked)


class TicTacToeBoard:
    def __init__(self, board):
        title_frame = tk.Frame(board, pady=10, bg=frame_colour)
        title_frame.pack()
       
        player_turn_label = tk.Label(title_frame, padx=10, pady=10, text=player + " turn", font=(font1, title_size), bg=title_colour)
        player_turn_label.pack(side="top")
        self.create_board3(board)

    def create_board3(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")
        
        for row in range(3):
            for column in range(3):
                board3[row][column] = tk.Button(board_frame, text="", width=16, height=8)
                board3[row][column].grid(row=row, column=column)

def main():
    window = tk.Tk()
    window.minsize(500, 500)
    window.maxsize(500, 500)
    window.title("Tic-Tac-Toe Game")
    window.configure(bg="grey")
    gui = MainMenu(window)
    # gui = TicTacToeBoard(window2)
    window.mainloop()

main()