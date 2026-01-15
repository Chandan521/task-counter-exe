import tkinter as tk
import json
import os

DATA_FILE = "task_data.json"

# ---------- Data Handling ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"task": 0, "reject": 0}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ---------- GUI ----------
root = tk.Tk()
root.title("Task Counter")
root.geometry("220x140")
root.resizable(False, False)
root.attributes("-topmost", True)  # ALWAYS ON TOP
root.configure(bg="#1e1e2f")

# Remove maximize/minimize
root.attributes("-toolwindow", True)

FONT_BIG = ("Segoe UI", 16, "bold")
FONT_SMALL = ("Segoe UI", 9)

# ---------- Task Counter ----------
def inc_task():
    data["task"] += 1
    task_label.config(text=data["task"])
    save_data()

def dec_task():
    if data["task"] > 0:
        data["task"] -= 1
        task_label.config(text=data["task"])
        save_data()

def reset_task():
    data["task"] = 0
    task_label.config(text=0)
    save_data()

# ---------- Reject Counter ----------
def inc_reject():
    data["reject"] += 1
    reject_label.config(text=data["reject"])
    save_data()

def dec_reject():
    if data["reject"] > 0:
        data["reject"] -= 1
        reject_label.config(text=data["reject"])
        save_data()

def reset_reject():
    data["reject"] = 0
    reject_label.config(text=0)
    save_data()

# ---------- UI Layout ----------
tk.Label(root, text="TASK", fg="white", bg="#1e1e2f", font=FONT_SMALL).pack()
frame1 = tk.Frame(root, bg="#1e1e2f")
frame1.pack()

tk.Button(frame1, text="−", width=3, command=dec_task).pack(side="left")
task_label = tk.Label(frame1, text=data["task"], fg="#00ffcc", bg="#1e1e2f", font=FONT_BIG)
task_label.pack(side="left", padx=6)
tk.Button(frame1, text="+", width=3, command=inc_task).pack(side="left")

tk.Button(root, text="Reset Task", font=FONT_SMALL, command=reset_task).pack(pady=2)

tk.Label(root, text="REJECT", fg="white", bg="#1e1e2f", font=FONT_SMALL).pack()
frame2 = tk.Frame(root, bg="#1e1e2f")
frame2.pack()

tk.Button(frame2, text="−", width=3, command=dec_reject).pack(side="left")
reject_label = tk.Label(frame2, text=data["reject"], fg="#ff4c4c", bg="#1e1e2f", font=FONT_BIG)
reject_label.pack(side="left", padx=6)
tk.Button(frame2, text="+", width=3, command=inc_reject).pack(side="left")

tk.Button(root, text="Reset Reject", font=FONT_SMALL, command=reset_reject).pack(pady=2)

root.mainloop()
