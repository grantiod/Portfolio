from tkinter import Entry, Button, Tk, END, mainloop

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")

        self.e = Entry(self.root, width=35, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_click(self, number):
        # e.delete(0, END)
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))

    def button_clearAll(self):
        self.e.delete(0, END)

    def button_addVals(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.e.delete(0, END)

    def button_subVals(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        self.e.delete(0, END)

    def button_mulVals(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.e.delete(0, END)

    def button_divVals(self):
        first_number = self.e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.e.delete(0, END)

    def button_equals(self):
        if math == "addition":
            second_number = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, f_num + int(second_number))
        elif math == "subtraction":
            second_number = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, f_num - int(second_number))
        elif math == "multiplication":
            second_number = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, f_num * int(second_number))
        elif math == "division":
            second_number = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, f_num / int(second_number))

    def run(self):
        # define buttons
        self.button_1 = Button(self.root, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = Button(self.root, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = Button(self.root, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = Button(self.root, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = Button(self.root, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = Button(self.root, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = Button(self.root, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = Button(self.root, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = Button(self.root, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = Button(self.root, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_add = Button(self.root, text="+", padx=39, pady=20, command=self.button_addVals)
        self.button_subtract = Button(self.root, text="-", padx=41, pady=20, command=self.button_subVals)
        self.button_multiply = Button(self.root, text="x", padx=40, pady=20, command=self.button_mulVals)
        self.button_divide = Button(self.root, text="/", padx=41, pady=20, command=self.button_divVals)
        self.button_equal = Button(self.root, text="=", padx=90, pady=20, command=self.button_equals)
        self.button_clear = Button(self.root, text="Clear", padx=79, pady=20, command=self.button_clearAll)

        # put buttons on screen
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_add.grid(row=5, column=0)
        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)
        self.button_equal.grid(row=5, column=1, columnspan=2)

        mainloop()