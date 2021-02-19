import tkinter as tk 
root = tk.Tk()
photo = tk.PhotoImage(file = "play_image2.png")
a = tk.Label(image = photo)
a.pack()
root.mainloop()