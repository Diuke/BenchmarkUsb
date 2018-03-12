import tkinter as tk

import draw as draw
import threading

main_window = tk.Tk()

app = draw.Application(main_window)

app.mainloop()

#print(Bench.testCreate())
#print(Bench.testDelete())
