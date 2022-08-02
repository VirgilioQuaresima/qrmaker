import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from qr_maker import *
import shutil
from PIL import Image, ImageTk



class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        root.geometry("500x1000")
        root.title('QrMaker')

        self.entrythingy = tk.Entry(width=50, font=('Arial 12'))
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        self.button=tk.Button(text="GENERA QR", command=self.generate_qr)

        self.button.pack()
        root.mainloop()

    def generate_qr(self):
        url=self.contents.get()
        link=Link(url)
        img=link.crate_qr()
        img=link.add_logo(img)
        display = ImageTk.PhotoImage(img.resize((400, 400)))
        self.label = tk.Label(root, image=display)
        self.label.image = display
        self.label.pack()
        self.sv_btn = tk.Button(root, text = 'SALVA', command = lambda : self.save(img))
        self.cl_btn = tk.Button(root, text = 'NUOVO', command = lambda : self.clear())
        self.sv_btn.pack(pady = 10)
        self.cl_btn.pack(pady = 10)

    def clear(self):
        self.label.destroy()
        self.sv_btn.destroy()
        self.cl_btn.destroy()
    
    def save(self,img):
        files = [('PNG', '*.png'),
                ('Text Document', '*.txt'),
                ('All Files', '*.*')]
        file = asksaveasfilename(filetypes = files, defaultextension = files)
        img.save(file)
        self.label.destroy()
        self.sv_btn.destroy()

if __name__ == "__main__":

    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()