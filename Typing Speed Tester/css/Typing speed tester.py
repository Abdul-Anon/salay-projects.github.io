import tkinter as tk
from tkinter import ttk
import itertools
class Root:
     def __init__(self, master):

        super().__init__()
        self.master = master        

        style = ttk.Style()
        style_1 = {'foreground': 'red', 'background': 'black'}
        style_2 = {'foreground': 'yellow', 'background': 'grey'}
        mapping_1 = {'background': [('pressed', 'gold'), ('active', 'magenta')]}
        mapping_2 = {'background': [('pressed', 'chocolate'), ('active', 'blue4')]}
        style_cycle = itertools.cycle([style_1, style_2])
        mapping_cycle = itertools.cycle([mapping_1, mapping_2])

        def switch_style():
            style_choice = next(style_cycle)
            mapping_choice = next(mapping_cycle)
            style.configure('TButton', **style_choice)
            style.map('TButton', **mapping_choice)
        button = ttk.Button(root, text="style switch", command=switch_style,
        style="TButton")
        button.pack(padx=50, pady=50)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Typing Speed Tester")
    window = Root(root)
    root.mainloop()
