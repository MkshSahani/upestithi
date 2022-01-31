#first page of the application use to decide 
"""
	
	contain two option where to go
	start the attandance system or
	start the dashbord for the 
	professor.

"""


#modules
from tkinter import *
from tkinter import ttk


#user created modules
from log import *
from signup import *
from autogui import *

class Firstpage:
	def __init__(self,root):
		self.file1 = "images.gif"
		self.photo = PhotoImage(file = self.file1)
		self.backgroundimage = Label(root, height = 768, width = 1360, image = self.photo)
		self.backgroundimage.pack()

		#font
		self.labeltextfont = ('Times', -30, 'bold')

		#welcome text

		self.welcometext = ttk.Label(root, text ='Upestithi'.title(), font = self.labeltextfont)
		self.welcometext.place(x = 230, y = 100)



		#button for start the program
		self.automate = ttk.Button(root, text  = 'Start', command = self.startfun)
		self.login = ttk.Button(root, text = 'Log in', command = self.loginfun)
		self.automate.place(x = 150, y = 200)
		self.login.place(x = 250, y = 200)

		self.signupb = ttk.Button(root, text = 'Sign up', command = self.signup)
		self.signupb.place(x = 350, y = 200)
		self.window = root

	def startfun(self):
		self.window.destroy()
		autowindow = Tk()
		obj = Autogui(autowindow)
		autowindow.mainloop()


	def loginfun(self):
		self.window.destroy()
		loginpage = Tk()
		loginpage.geometry("600x400")
		loginpage.resizable(0, 0)
		obj = Log(loginpage)
		loginpage.mainloop()

	def signup(self):
		self.window.destroy()
		signuppage = Tk()
		signuppage.geometry("600x400")
		signuppage.resizable(0, 0)
		obj = Signup(signuppage)
		signuppage.mainloop()


if __name__ == "__main__":

	root = Tk()
	root.wm_iconbitmap('favicon.ico')
	root.title("Upestithi")
	root.geometry("600x400")
	root.resizable(0, 0)
	obj = Firstpage(root)
	root.mainloop()
