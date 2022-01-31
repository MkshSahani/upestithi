from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
import os
from tkinter import messagebox

class Report:
	def __init__(self, root):
		root.title("Report card generator".title())
		root.geometry("600x400")
		root.wm_iconbitmap('favicon.ico')
		root.resizable(0, 0)

		#statusbar

		self.statusbar = Label(root, relief = SUNKEN, anchor = W, text = 'please enter the file path')
		self.statusbar.pack(side = BOTTOM, fill = X)
		

		#menubar

		self.menubar = Menu(root)
		root.config(menu = self.menubar)

		self.exitmenu = Menu(root, tearoff = 0)
		self.exitmenu.add_command(label = 'Exit', command = root.destroy)

		self.menubar.add_cascade(label = 'Exit', menu = self.exitmenu)

		self.bkimg = PhotoImage(file = "images.gif")
		#background
		self.bklable = Label(root, image = self.bkimg, height = 768, width = 1360)
		self.bklable.pack()

		#maintitle
		self.mfont = ('Times', -30,'bold')
		self.maintitle = Label(root, text = 'Reprot card generator'.title(), font = self.mfont)
		self.maintitle.place(x = 150, y = 80)


		#browse file
		self.llfont = ('Times', -20, 'bold')
		self.lfilename = ttk.Label(root, text = 'select file : ', font = self.llfont)
		self.lfilename.place(x = 120, y = 180)

		self.efilename = Text(root, font = self.llfont, height = 1, width = 20)
		self.efilename.place(x = 220, y = 180)

		self.bfilename = ttk.Button(root, text = 'Browse', command = self.browsefile)
		self.bfilename.place(x = 440, y = 182)

		self.createbutton = ttk.Button(root, text = 'get report card'.title(), command = self.getreportfunc)
		self.createbutton.place(x = 280, y = 230)


	def getreportfunc(self):
		pass


	def browsefile(self):
		self.fname = filedialog.askopenfilename()
		print(self.fname)
		self.sfname = os.path.basename(self.fname)
		self.extenstion = self.sfname[-4 : ]
		if self.extenstion != "xlsx":
			self.efilename.delete(0.0, END)
			messagebox.showinfo("Info", "Give a excel file\ncontain all the data of student")
		else:
			self.efilename.delete(0.0, END)
			self.efilename.insert(0.0, self.sfname)
			print(self.sfname)


if __name__ == "__main__":
	report = Tk()
	obj = Report(report)
	report.mainloop()