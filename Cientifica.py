import tkinter as tk
from tkinter import ttk
import math
from scipy import integrate

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")
        master.geometry("712x324")
        self.total = tk.StringVar()

        # Cria um ttk.Frame com borda arredondada
        frame = ttk.Frame(master, style="MyFrame.TFrame")
        frame.grid(row=0, column=0, columnspan=8, sticky="ew", pady=8)

        self.entry = ttk.Entry(frame, textvariable=self.total, font=("Helvetica", 20))
        self.entry.pack(fill="x", padx=5, pady=5)

        # Configura o estilo do frame
        style = ttk.Style()
        style.configure("MyFrame.TFrame", 
                        background="light gray", 
                        borderwidth=5, 
                        relief="groove",
                        )
        
        self.create_buttons()

        self.integral_mode = False
        self.a = None
        self.b = None
        self.func = None

    def create_buttons(self):
        button_list = [
            ['/', '7', '8', '9', 'log(x)', 'sin', '10^x', '%'],
            ['*', '4', '5', '6', '1/x', 'cos', '±', ')'],
            ['-', '1', '2', '3', 'x!', 'tan', '∫', '('],
            ['+', '=', '0', 'C', '⌫', '√', '^2', 'π']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
                self.master.rowconfigure(i + 1, weight=1)
                self.master.columnconfigure(0, weight=1)
                self.master.columnconfigure(1, weight=1)
                self.master.columnconfigure(2, weight=1)
                self.master.columnconfigure(3, weight=1)
                self.master.columnconfigure(4, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == 'C':
            self.total.set("")
        elif button_text == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == '^2':
            try:
                result = float(self.entry.get()) ** 2
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == '1/x':
            try:
                result = 1 / float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == '10^x':
            try:
                result = 10 ** float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == '√':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Erro")
        elif button_text == '⌫':
            display_text = self.entry.get()
            if display_text:  # Verifica se o campo de exibição não está vazio
                self.entry.delete(0, tk.END)  # Limpa todo o campo de exibição
                self.entry.insert(0, display_text[:-1])  # Insere o texto sem o último caracter no campo de exibição
        elif button_text == 'π':
            result = math.pi
            self.total.set(result)
        elif button_text == '%':
            result = self.entry.insert(tk.END, '/100')
        elif button_text == '±':
            self.entry.insert(tk.END, '-')
        elif button_text == '∫':
            self.integral_mode = True
            self.total.set("Insira o limite inferior (a):")
        else:
            if self.integral_mode:
                if self.a is None:
                    self.a = float(button_text)
                    self.total.set("Insira o limite superior (b):")
                elif self.b is None:
                    self.b = float(button_text)
                    self.total.set("Insira a função (por exemplo, x**2):")
                else:
                    self.func = button_text
                    result, error = integrate.quad(lambda x: eval(self.func), self.a, self.b)
                    self.total.set(result)
                    self.integral_mode = False
                    self.a = None
                    self.b = None
                    self.func = None
            else:
                self.total.set(self.entry.get() + button_text)

if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()