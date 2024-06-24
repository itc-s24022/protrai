import datetime
import tkinter as tk

def upload_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text=current_time)
    root.after(1000, upload_time)  # Schedule upload_time() to run again after 1000 milliseconds (1 second)

root = tk.Tk()
root.title("現在の時刻")

lbl = tk.Label(root, font=("Helvetica", 24))  # Specify a font size for better visibility
lbl.pack(padx=20, pady=20)  # Add padding around the label for better layout

upload_time()  # Initial call to start displaying the time

root.mainloop()
