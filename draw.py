from tkinter import messagebox
from tkinter import ttk
import file as bench


class Application(ttk.Frame):
    Bench = bench.BenchTests()

    def __init__(self, main_window):

        super().__init__(main_window)
        main_window.title("Benchmark")

        self.combo = ttk.Combobox(self, state="readonly")
        self.combo["values"] = ["Python", "C", "C++", "Java"]
        self.combo.current(0)
        self.combo.place(x=50, y=50)

        self.button = ttk.Button(self, text="Calculate", command=self.test)
        self.button.place(x=220, y=50)
        main_window.configure(width=400, height=200)
        self.place(width=400, height=200)
        self.fillComboBox(self.Bench.usbDrives)

    def fillComboBox(self, args):
        if not args:
            messagebox.showerror("Error", "Error message")
            self.root.destroy()
        else:
            self.combo["values"] = args
            self.combo.current(0)

    def test(self):
        print(self.Bench.test4k())
        print(self.Bench.testSequential())
        print(self.Bench.testCreate())
        print(self.Bench.testDelete())


