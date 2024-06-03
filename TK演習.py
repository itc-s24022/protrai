#GUIで動くアプリ
import tkinter as tk
root = tk.Tk()

root.geometry("300x200")#win_size
root.title("AAA")
ldl = tk.Label(text="Hello World")
ldl.pack()


root.mainloop()
