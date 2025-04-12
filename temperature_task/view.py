from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
from temperature_task.scale import Scale


class View:
    def __init__(self):
        self.__root = None
        self.__input_entry = None
        self.__from_scale = None
        self.__to_scale = None
        self.__output_text = None
        self.__controller = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root = Tk()
        self.__root.title("Temperature converter")
        self.__root.iconbitmap(default="temperature_icon.ico")
        self.__root.geometry("435x400+450+200")
        self.__root.resizable(False, False)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)

        for row in range(7):
            self.__root.grid_rowconfigure(row, weight=1)

        input_frame = ttk.Frame(borderwidth=1, relief=RIDGE, padding=[10, 10])
        input_frame.pack(fill=X, padx=4, pady=10)
        output_frame = ttk.Frame(borderwidth=1, relief=RIDGE, padding=[10, 10])
        output_frame.pack(fill=X, padx=4, pady=2)
        button_frame = ttk.Frame(borderwidth=1, relief=RIDGE, padding=[10, 10])
        button_frame.pack(fill=X, padx=4, pady=10)

        from_label = ttk.Label(input_frame, text="From:", font=("Aptos", 12, "bold"))
        from_label.grid(row=0, column=0, padx=5, pady=7, sticky=EW)
        to_label = ttk.Label(input_frame, text="To:", font=("Aptos", 12, "bold"))
        to_label.grid(row=0, column=1, padx=5, pady=7, sticky=EW)

        scales = ["Celsius", "Fahrenheit", "Kelvin"]
        state_1 = StringVar(value=scales[0])
        state_2 = StringVar(value=scales[0])

        self.__from_scale = ttk.Combobox(input_frame, values=scales, textvariable=state_1,
                                         state="readonly", font=("Aptos", 12))
        self.__from_scale.grid(row=1, column=0)
        self.__to_scale = ttk.Combobox(input_frame, values=scales, textvariable=state_2,
                                       state="readonly", font=("Aptos", 12))
        self.__to_scale.grid(row=1, column=1)

        input_label = ttk.Label(input_frame, text="Input:", font=("Aptos", 12, "bold"))
        input_label.grid(row=2, column=0, padx=5, pady=7, sticky=EW)

        self.__input_entry = ttk.Entry(input_frame, font=("Aptos", 12))
        self.__input_entry.grid(row=3, column=0, columnspan=2, sticky=EW)

        result_label = ttk.Label(output_frame, text="Result:", font=("Aptos", 12, "bold"))
        result_label.grid(row=4, column=0, padx=5, pady=7, sticky=EW)

        self.__output_text = ScrolledText(output_frame, width=43, height=4, font=("Aptos", 12), state=DISABLED)
        self.__output_text.grid(row=5, column=0)

        convert_button = Button(button_frame, text="Convert", width=20, font=("Aptos", 12),
                                command=self.__convert_temperature)
        convert_button.grid(row=6, column=0, padx=5, pady=7, sticky=EW)

        clear_button = Button(button_frame, text="Clear", width=20, font=("Aptos", 12), command=self.clear)
        clear_button.grid(row=6, column=1, padx=10, pady=7, sticky=NE)

        self.__root.mainloop()

    def clear(self):
        self.__output_text.configure(state=NORMAL)
        self.__output_text.delete("1.0", END)
        self.__output_text.configure(state=DISABLED)
        self.__input_entry.delete(0, END)

    def __convert_temperature(self):
        try:
            input_temperature = float(self.__input_entry.get())
            input_scale = Scale(self.__from_scale.get())
            output_scale = Scale(self.__to_scale.get())
            self.__controller.convert(input_temperature, input_scale, output_scale)
        except ValueError:
            showerror(title="Error", message="Temperature must be number")

    def show(self, output_temperature):
        self.__output_text.configure(state=NORMAL)
        self.__output_text.insert("1.0", f"{output_temperature}\n")
        self.__output_text.configure(state=DISABLED)
