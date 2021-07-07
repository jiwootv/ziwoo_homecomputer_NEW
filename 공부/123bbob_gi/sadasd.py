import tkinter as tk

root = tk.Tk()
root.title("아2콘 연습")
root.geometry("640x400+100+100")
root.resizable(True, True)
image = tk.PhotoImage(file="tera-a.gif")

label = tk.Label(root, image=image)

label.pack()

root.mainloop()