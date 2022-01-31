from tkinter import *
from tkinter import ttk 
import time

#user defined modules

import reup

class Extrac:
	def __init__(self, root):

		root.resizable(0, 0)
		root.wm_iconbitmap('favicon.ico')
		root.title("Extra class")
		self.fontl = ('Times', -30, 'bold')

		#background

		self.bkimg = PhotoImage(file = 'images.gif')
		self.bklabel = Label(root, height = 768, width = 1360, image = self.bkimg)
		self.bklabel.pack()


		#title
		self.mainlabel = ttk.Label(root, text = 'for extra class select date'.title(), font = self.fontl)
		self.mainlabel.place(x = 100, y = 50)


		self.fontll = ('Times', -20, 'bold')
		#for date
		self.ldate = ttk.Label(root, text = 'Date', font = self.fontll)
		self.ldate.place(x = 50, y = 100)

		self.gdate = IntVar()

		self.spindate = Spinbox(root, textvariable = self.gdate, from_ = 1, to = 31, font = self.fontll)
		self.spindate.place(x = 150, y = 100)


		#for brance

		self.lbranch = ttk.Label(root, text = "Branch", font = self.fontll)
		self.lbranch.place(x = 50, y = 150)

		self.tupbranch = ("CSE","EEE","ECE","CIVIL","IT")


		self.gbranch = StringVar()
		self.spinbranch = Spinbox(root, textvariable = self.gbranch, values = self.tupbranch, font = self.fontll)
		self.spinbranch.place(x = 150, y = 150)


		#for semester

		self.gsemester = IntVar()
		self.lsemester = ttk.Label(root, text = 'Semester', font = self.fontll)
		self.lsemester.place(x = 50, y = 200)

		self.spinsemester = Spinbox(root, textvariable = self.gsemester, from_ = 1, to = 8, font = self.fontll)
		self.spinsemester.place(x = 150, y = 200)


		#time slot
		self.gslot = StringVar()
		
		self.lslot = ttk.Label(root, text = 'Slot', font = self.fontll)
		self.lslot.place(x = 50, y = 250)

		self.tuptime = ("9-10 AM", "10-11 AM","11-12 AM","12-1 AM","2-3 AM","3-4 AM","4-5 AM")

		self.spintime = Spinbox(root, textvariable = self.gslot, values = self.tuptime, font = self.fontll)
		self.spintime.place(x = 150, y = 250)


		#lh

		self.ghall = StringVar()
		self.lhall = ttk.Label(root, text = 'Hall', font = self.fontll)
		self.lhall.place(x = 50, y = 300)

		self.tuphall = ("LH1","LH2","LH3","LH4","LH5","LH6","LH7","LH8","LH9","LH10","LH11")
		self.spinhall = Spinbox(root, textvariable = self.ghall, values = self.tuphall, font = self.fontll)
		self.spinhall.place(x = 150, y = 300)

		#button

		self.confirmb = ttk.Button(root, text = 'Confirm', command = self.confirmclass)
		self.cancelb = ttk.Button(root, text = 'Cancel', command = self.cancelbutton)
		self.confirmb.place(x = 400, y = 300)
		self.cancelb.place(x = 500, y = 300)
		self.windowmain = root
	def confirmclass(self):
		print(self.gdate.get())
		print(self.gbranch.get())
		print(self.gsemester.get())
		print(self.gslot.get())
		print(self.ghall.get())

	def cancelbutton(self):
		self.windowmain.destroy()
		reup.reopen_sigin()
if __name__ == "__main__":
	window = Tk()
	window.geometry("600x400")
	obj = Extraclass(window)
	window.mainloop()