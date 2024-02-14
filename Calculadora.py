import tkinter as tk
from tkinter import ttk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x550")
        self.resizable(False, False)

        self.resultado_var = tk.StringVar()
        self.crear_interfaz()

    def crear_interfaz(self):
        style = ttk.Style(self)
        style.configure("TButton", padding=10, font=("Arial", 12), width=4)

        entry = ttk.Entry(self, textvariable=self.resultado_var, justify="right", font=("Arial", 20), state="disabled")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'DEL'
        ]

        fila_val = 1
        columna_val = 0

        for boton in botones:
            if boton == '=':
                ttk.Button(self, text=boton, command=lambda b=boton: self.presionar(b)).grid(row=fila_val, column=columna_val, rowspan=2, sticky="nsew")
            elif boton in ['C', 'DEL']:
                ttk.Button(self, text=boton, command=lambda b=boton: self.presionar(b)).grid(row=fila_val, column=columna_val, sticky="nsew")
            else:
                ttk.Button(self, text=boton, command=lambda b=boton: self.presionar(b)).grid(row=fila_val, column=columna_val, sticky="nsew")
                
            columna_val += 1
            if columna_val > 2:
                columna_val = 0
                fila_val += 1

        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i - 1, weight=1)

    def presionar(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Error")
        elif valor == 'C':
            self.resultado_var.set("")
        elif valor == 'DEL':
            current_text = self.resultado_var.get()
            self.resultado_var.set(current_text[:-1])
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
