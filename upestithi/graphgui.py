from tkinter import *
from tkinter import ttk


class Grapgen:
	def __init__(self, root):
		root.geometry("600x400")
		root.title('Graph')
		root.wm_iconbitmap('favicon.ico')

		self.ffont = ('Times', -30, '')






if __name__ == "__main__":
	mainwindow = Tk()
	obj = Grapgen(mainwindow)
	mainwindow.rootmainloop()