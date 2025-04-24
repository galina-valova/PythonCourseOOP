from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showwarning


class WelcomeWindow:
    def __init__(self):
        self.__window = None
        self.__name_entry = None
        self.__rows_number = None
        self.__columns_number = None
        self.__mines_number = None
        self.__start_button = None
        self.__controller = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__window = Tk()
        self.__window.title("New game")
        self.__window.iconbitmap(default="gui/icons/minesweeper_logo.ico")
        self.__window.geometry("410x250+450+200")
        self.__window.resizable(False, False)
        self.__window.protocol("WM_DELETE_WINDOW", self.exit_click)

        input_frame = ttk.Frame(self.__window)
        input_frame.pack()

        row_list = [
            "Enter name:",
            "Number of rows (max 15):",
            "Number of columns (max 30):",
            "Number of mines (max 58):"
        ]

        for i in range(len(row_list)):
            label = ttk.Label(input_frame, text=row_list[i], font=("Aptos", 12))
            label.grid(row=i, column=0, padx=4, pady=5, ipady=6, sticky="E")

        validate_name = self.__window.register(lambda input_text: self.check_name_size(input_text))
        self.__name_entry = ttk.Entry(input_frame, width=14, font=("Aptos", 12),
                                      validate="key",
                                      validatecommand=(validate_name, "%P"))
        self.__name_entry.grid(row=0, column=1, sticky="EW")
        self.__name_entry.bind("<FocusOut>", lambda event: self.is_empty_name())
        self.__name_entry.bind("<KeyRelease>", lambda event: (self.is_empty_input()))

        validate_sizes = self.__window.register(lambda new_value, max_value: self.check_sizes(new_value, max_value))
        initial_nrow = StringVar(value="9")
        self.__rows_number = ttk.Spinbox(input_frame, from_=3, to=15,
                                         font=("Aptos", 12), width=7,
                                         validate="key",
                                         validatecommand=(validate_sizes, "%P", 15),
                                         textvariable=initial_nrow)
        self.__rows_number.grid(row=1, column=1, sticky="W")
        self.__rows_number.bind("<FocusOut>", lambda event: self.is_empty_rows())
        self.__rows_number.bind("<KeyRelease>", lambda event: self.is_empty_input())
        self.__rows_number.bind("<Leave>", lambda event: self.update_mines())

        initial_ncol = StringVar(value="9")
        self.__columns_number = ttk.Spinbox(input_frame, from_=3, to=15,
                                            font=("Aptos", 12), width=7,
                                            validate="key",
                                            validatecommand=(validate_sizes, "%P", 30),
                                            textvariable=initial_ncol)
        self.__columns_number.grid(row=2, column=1, sticky="W")
        self.__columns_number.bind("<FocusOut>", lambda event: self.is_empty_columns())
        self.__columns_number.bind("<KeyRelease>", lambda event: self.is_empty_input())
        self.__columns_number.bind("<Leave>", lambda event: self.update_mines())

        validate_mines = self.__window.register(
            lambda new_value, max_value: self.check_mines_number(new_value, max_value)
        )
        initial_n_mines = StringVar(value="10")
        self.__mines_number = ttk.Spinbox(input_frame, from_=0, to=15,
                                          font=("Aptos", 12), width=7,
                                          validate="key",
                                          validatecommand=(validate_mines, "%P", 58),
                                          textvariable=initial_n_mines)
        self.__mines_number.grid(row=3, column=1, sticky="W")
        self.__mines_number.bind("<FocusOut>", lambda event: self.is_empty_mines())
        self.__mines_number.bind("<KeyRelease>", lambda event: (self.is_empty_input()))

        self.__start_button = Button(width=12, text="Start", font=("Aptos", 12),
                                     state=DISABLED, command=self.click_start)
        self.__start_button.pack(pady=7)

        self.__window.mainloop()

    @staticmethod
    def check_sizes(input_value, max_value):
        if input_value == "":
            return True
        try:
            value = int(input_value)
            return 1 <= value <= int(max_value)
        except ValueError:
            return False

    @staticmethod
    def check_name_size(input_text):
        return len(input_text) <= 10

    def is_empty_input(self):
        if (self.__name_entry.get() and self.__rows_number.get()
                and self.__columns_number.get() and self.__mines_number.get()):
            self.__start_button.config(state=NORMAL)
        else:
            self.__start_button.config(state=DISABLED)

    def is_empty_name(self):
        try:
            len((self.__name_entry.get())) > 0
        except ValueError:
            showwarning("Warning", "Please enter player name")
            self.__name_entry.focus()

    def is_empty_rows(self):
        try:
            int(self.__rows_number.get())
        except ValueError:
            showwarning("Warning", "Please enter number of rows")
            self.__rows_number.focus()

    def is_empty_columns(self):
        try:
            int(self.__columns_number.get())
        except ValueError:
            showwarning("Warning", "Please enter number of columns")
            self.__columns_number.focus()

    def is_empty_mines(self):
        try:
            int(self.__mines_number.get())
        except ValueError:
            showwarning("Warning", "Please enter number of mines")
            self.__mines_number.focus()

    def exit_click(self):
        if askokcancel("Quit", "Do you want to exit?"):
            self.__window.destroy()

    def check_mines_number(self, input_value, max_value):
        if input_value == "":
            return True

        try:
            int(input_value)
        except ValueError:
            return False

        nmines = int(input_value)
        nrow = int(self.__rows_number.get())
        ncol = int(self.__columns_number.get())
        threshold = int(nrow * ncol * 0.13)

        if nmines > threshold:
            showwarning("Warning", f"Number of mines does not correspond to field size."
                                   f" For such a field, {threshold} or less mines is possible.")
            self.__mines_number.set(f"{threshold}")
            self.__start_button.config(state=NORMAL)

        return 0 <= nmines <= int(max_value)

    def update_mines(self):
        try:
            nmines = int(self.__mines_number.get())
            nrow = int(self.__rows_number.get())
            ncol = int(self.__columns_number.get())
            threshold = int(nrow * ncol * 0.13)

            if nmines > threshold:
                showwarning("Warning", f"Number of mines must not exceed {threshold}.")
                self.__mines_number.delete(0, END)
                self.__mines_number.set(str(threshold))

        except ValueError:
            pass

    def click_start(self):
        nrow = int(self.__rows_number.get())
        ncol = int(self.__columns_number.get())
        nmines = int(self.__mines_number.get())
        player_name = self.__name_entry.get()
        self.__window.destroy()
        self.__controller.start_game(nrow, ncol, nmines, player_name)
