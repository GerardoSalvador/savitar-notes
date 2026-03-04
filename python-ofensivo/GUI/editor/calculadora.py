#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#6495d3", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.master.bind("<Key>", self.key_press) # Detecta el teclado

    def key_press(self, event):
        key = event.char
        if key == "\r":
            self.calculate()
            return
        elif key == "\x08":
            self.clear_display
            return
        elif key == "\x1b":
            self.master.quit()
            return

        self.click(key)

    def clear_display(self):
        self.display.delete(0, tk.END)
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0
    
    def calculate(self):
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)

        self.display.delete(0, "end")
        self.display.insert("end", round(self.total,3))
    
    def click(self, button):
        if self.op_verification:
            self.op_verification = False

        self.display.insert("end", button)

        if button in "0123456789" or button == ".":
            self.current += button
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
            
            self.current = ""

            self.op_verification = True
            self.op = button

        print(f"\n[+] Has presionado: {button}")
        print(f"[+] La primera combinacion es: {self.current}")
        print(f"[+] Status op_verification: {self.op_verification}")
        print(f"[+] Tipo de operacion que deseo efectuar: {self.op}")
        print(f"[+] Total: {self.total}")


    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=8, command= lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=8, command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=8, command=lambda: self.click(button))

        b.grid(row=row, column=col)

       
root = tk.Tk()
root.title("Aplicacion de toma de calculadora")

my_gui = Calculadora(root)

root.mainloop()