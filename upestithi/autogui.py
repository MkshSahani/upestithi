"""

	
"""
from tkinter import messagebox
from tkinter import *
from tkinter import ttk 

#self created modules
import firstpage
import uhack



class Autogui:
	def __init__(self, root):
		root.resizable(0, 0)
		root.geometry("600x400")
		root.title("Attandance System".title())
		root.wm_iconbitmap('favicon.ico')

		self.bkimg = PhotoImage(file =  'images.gif')

		self.bglabel = Label(root, height = 768, width = 1360, image = self.bkimg)
		self.bglabel.pack()


		#title

		self.lfont = ('Times', -30, 'bold')

		self.maintitle = ttk.Label(root, text = 'Please select the class'.title(), font = self.lfont)
		self.maintitle.place(x = 160, y = 80)

		#hall spin box

		self.llfont = ('Times', -20, 'bold')
		self.lhall = Label(root, text = 'Hall : ', font = self.llfont)
		self.lhall.place(x = 180, y = 200)


		self.listhalls = ("LH1","LH2")

		self.ehall = StringVar()

		self.spinhall = Spinbox(root, textvariable = self.ehall, values = self.listhalls, font = self.llfont)
		self.spinhall.place(x = 240, y = 200)


		self.cam1button = ttk.Button(root, text = 'start', command = self.cam1func)
		self.cam1button.place(x = 200, y = 250)
		'''
		self.cam2button = ttk.Button(root, text = 'Camera 2', command = self.cam2func)
		self.cam2button.place(x = 280, y = 250)
		'''
		self.cancelbutton = ttk.Button(root, text = 'Exit', command = self.cancelbuttonworking)
		self.cancelbutton.place(x = 300, y = 250)


		self.window = root


	def cam1func(self):
		self.window.destroy()
		hall_number = self.ehall.get()
		if hall_number == "LH1":
			uhack.automation(0)
		elif hall_number	== "LH2":
			uhack.automation(1)
		

	

	def cancelbuttonworking(self):
		self.window.destroy()
		mainwindow = Tk()
		mainwindow.wm_iconbitmap('favicon.ico')
		mainwindow.title("Upestithi")
		mainwindow.geometry("600x400")
		mainwindow.resizable(0, 0)
		obj = firstpage.Firstpage(mainwindow)
		mainwindow.mainloop()

if __name__ == "__main__":
	autowindow = Tk()
	obj = Autogui(autowindow)
	autowindow.mainloop()

