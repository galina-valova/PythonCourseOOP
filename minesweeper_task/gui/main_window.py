from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askokcancel
import os


class MainWindow:
    def __init__(self):
        self.__scores_results = None
        self.__state_frame = None
        self.__root = None
        self.__field_frame = None
        self.__controller = None
        self.__mines_count_label = None
        self.__nmines = None
        self.__new_game_button = None
        self.__time_var = None
        self.__flag_count = 0
        self.__icons = {}

    def set_controller(self, controller):
        self.__controller = controller

    @property
    def state_frame(self):
        return self.__state_frame

    def start(self, nrow, ncol, nmines):
        self.__root = Tk()
        self.__root.title("Minesweeper")
        self.__root.iconbitmap(default="gui/icons/minesweeper_logo.ico")
        self.__root.geometry("453x523+450+200")
        self.__root.resizable(False, False)
        self.__icons["new_game"] = PhotoImage(file="gui/icons/new_game.png")
        self.__icons["game_over"] = PhotoImage(file="gui/icons/game_over.png")
        self.__icons["win_game"] = PhotoImage(file="gui/icons/win_game.png")
        self.__icons["flag"] = PhotoImage(file="gui/icons/flag.png")
        self.__icons["mine"] = PhotoImage(file="gui/icons/mine.png")
        self.__nmines = nmines
        self.set_menu()
        self.set_game_field(nrow, ncol, nmines)
        self.__root.protocol("WM_DELETE_WINDOW", self.exit_click)
        self.__root.mainloop()

    def set_menu(self):
        menu = Menu()
        menu.add_cascade(label="Scores", command=self.scores_click)
        menu.add_cascade(label="About", command=self.about_click)
        menu.add_cascade(label="Exit", command=self.exit_click)
        self.__root.configure(menu=menu)

    @staticmethod
    def about_click():
        showinfo("About", "Minesweeper version is 1.0. Created on February, 23")

    def scores_click(self):
        scores = self.__controller.get_score()
        scores_window = Toplevel()
        scores_window.title("Players scores")
        scores_window.geometry("300x400+450+200")
        scores_window.resizable(False, False)
        scores_window.grab_set()

        header_frame = ttk.Frame(scores_window)
        header_frame.pack(fill=X, padx=5, pady=5)
        name_title_label = Label(header_frame, text="Name", font=("Aptos", 14, "bold"))
        name_title_label.pack(side=LEFT, padx=20)
        score_title_label = Label(header_frame, text="Win time", font=("Aptos", 14, "bold"))
        score_title_label.pack(side=RIGHT, padx=30)

        scrollbar = Scrollbar(scores_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.__scores_results = Text(scores_window,
                                     yscrollcommand=scrollbar.set,
                                     wrap=NONE,
                                     font=("Aptos", 12),
                                     padx=30)
        self.__scores_results.pack()
        self.__scores_results.config(height=17)
        scrollbar.config(command=self.__scores_results.yview)

        for i in range(len(scores)):
            self.__scores_results.insert(END, f"{scores[i]["name"]}\t{scores[i]["time"]}\n")

        self.__scores_results.configure(tabs=("150", "200"))

        clear_button = Button(scores_window, text="Clear score", command=self.clear_score, font=("Aptos", 14))
        clear_button.pack()

    def exit_click(self):
        if askokcancel("Quit", "Do you want to exit?"):
            self.__root.destroy()

    def clear_score(self):
        self.__scores_results.delete('1.0', END)
        score_file = "model/data/players_scores.json"

        try:
            os.remove(score_file)
        except OSError:
            return False

    def set_game_field(self, nrow, ncol, nmines):
        state_frame_style = ttk.Style()
        state_frame_style.configure("State.TFrame", background="#B3C1E5")
        self.__state_frame = ttk.Frame(borderwidth=1,
                                       relief=RIDGE,
                                       padding=[5, 5],
                                       style="State.TFrame")
        self.__state_frame.pack(fill=X, padx=4, pady=5)
        self.__state_frame.grid_rowconfigure(0, weight=1)
        self.__state_frame.grid_columnconfigure(0, weight=1)
        self.__state_frame.grid_columnconfigure(1, weight=1)
        self.__state_frame.grid_columnconfigure(2, weight=1)

        self.__mines_count_label = ttk.Label(self.__state_frame,
                                             text=str(nmines),
                                             font=("Aptos", 30, "bold"),
                                             foreground="#322F56",
                                             background="#B3C1E5",
                                             width=2)
        self.__mines_count_label.grid(row=0, column=0)

        self.__new_game_button = Button(self.__state_frame,
                                        image=self.__icons["new_game"],
                                        text="new game",
                                        compound=TOP,
                                        bg="#B3C1E5",
                                        border=0,
                                        command=self.__controller.reinit_game)
        self.__new_game_button.grid(row=0, column=1, padx=5)

        self.__time_var = StringVar(value="0")
        timer_label = ttk.Label(self.__state_frame,
                                textvariable=self.__time_var,
                                font=("Aptos", 30, "bold"),
                                foreground="#322F56",
                                background="#B3C1E5",
                                width=3)
        timer_label.grid(row=0, column=2)

        main_frame = ttk.Frame(borderwidth=1,
                               relief=RIDGE,
                               padding=[5, 5])
        main_frame.pack(expand=True, fill=BOTH, padx=5, pady=5)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.__field_frame = ttk.Frame(main_frame)
        self.__field_frame.grid(row=0, column=0)

        for widget in self.__field_frame.winfo_children():
            widget.destroy()

        self.create_game_field(nrow, ncol)
        self.__root.update()
        new_height = self.__root.winfo_reqheight()
        new_width = self.__root.winfo_reqwidth()
        self.__root.geometry(f"{new_width}x{new_height}+450+200")

    def create_game_field(self, nrow, ncol):
        self.__new_game_button["image"] = self.__icons["new_game"]
        self.__new_game_button["text"] = "New game"
        self.__mines_count_label["text"] = self.__nmines
        self.__flag_count = 0

        for row in range(nrow):
            for column in range(ncol):
                field_cell = Button(self.__field_frame,
                                    width=5,
                                    height=2,
                                    bg="#B3C1E5")
                field_cell.grid(row=row, column=column, sticky=NSEW, padx=1, pady=1)
                field_cell.bind("<Button-1>", lambda event, x=row, y=column: self.__controller.click_left(x, y))
                field_cell.bind("<Button-3>", lambda event, x=row, y=column: self.__controller.click_right(x, y))

    def disable_cells(self, unopened_cells):
        for coordinates in unopened_cells:
            x, y = coordinates[0], coordinates[1]
            unopened_button = self.__field_frame.grid_slaves(row=x, column=y)[0]
            unopened_button["state"] = "disabled"
            unopened_button.unbind("<Button-1>")
            unopened_button.unbind("<Button-3>")

    def show_mines(self, cell_coordinates):
        for x, y, status in zip(cell_coordinates["x"], cell_coordinates["y"], cell_coordinates["status"]):
            cell_label = Label(self.__field_frame,
                               image=self.__icons["mine"],
                               bg="white",
                               relief=RIDGE)
            cell_label.grid(row=x, column=y, sticky=NSEW, padx=1, pady=1)
            self.__new_game_button["image"] = self.__icons["game_over"]
            self.__new_game_button["text"] = "Game over"

    def show_opened_cells(self, cell_coordinates):
        for x, y, status in zip(cell_coordinates["x"], cell_coordinates["y"], cell_coordinates["status"]):
            cell_label = Label(self.__field_frame,
                               text=str(status) if status != 0 else "",
                               font=("Aptos", 13, "bold"),
                               foreground="#322F56",
                               bg="white",
                               relief=RIDGE)
            cell_label.grid(row=x, column=y, sticky=NSEW, padx=1, pady=1)

    def set_flag(self, cell_coordinates):
        x = cell_coordinates["x"]
        y = cell_coordinates["y"]
        flagged_button = self.__field_frame.grid_slaves(row=x, column=y)[0]

        if cell_coordinates["status"]:
            flagged_button["image"] = self.__icons["flag"]
            flagged_button["state"] = "disabled"
            self.__flag_count += 1
            flagged_button.unbind("<Button-1>")
        else:
            flagged_button["image"] = ""
            self.__flag_count -= 1
            flagged_button.bind("<Button-1>", lambda event: self.__controller.click_left(x, y))

        self.__mines_count_label.config(text=f"{self.__nmines - self.__flag_count}")

    def set_win_logo(self):
        self.__new_game_button["image"] = self.__icons["win_game"]
        self.__new_game_button["text"] = "You win!"

    def update_time(self, seconds):
        self.__time_var.set(f"{seconds}")
