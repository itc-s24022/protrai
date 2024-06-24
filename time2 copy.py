import datetime
import tkinter as tk

def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text=current_time)
    root.after(1000, update_time)  # 1秒後に update_time を再実行する

root = tk.Tk()
root.title("現在の時刻")

# ラベルを作成して配置
lbl = tk.Label(root, text="", font=("Helvetica", 20))
lbl.pack(padx=20, pady=20)

# 最初の時刻表示を更新
update_time()

root.mainloop()
