import tkinter as tk

def handle_Button(name):
    print(str(name) + " has been pressed")

window = tk.Tk()
"""
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
button1 = tk.Button(
    text="button 1",
    width=25,
    height = 10,
    command = lambda: handle_Button("1")

)
button1.pack()
button2 = tk.Button(
    text="button 2",
    height = 10,
    
    command = lambda: handle_Button("2")

)
button1.pack(fill=tk.BOTH,expand=True)
button2.pack(fill=tk.BOTH,expand=True)
"""


for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        bx = i
        by = j
        button = tk.Button(master=frame, text=f"Row {i}\nColumn {j}",command = lambda: handle_Button(f"{bx},{by}"))
        button.pack(padx=5, pady=5,fill=tk.BOTH,expand=True)
        
window.mainloop()