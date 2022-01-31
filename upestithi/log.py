from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

#user defined modules
from dashboard import *
import login

import os

class Log:
	def __init__(self, root):
		root.wm_iconbitmap('favicon.ico')
		root.title("Log in")

		#this is statusbar
		self.statusbar = Label(root, text = 'Please Enter the user name and password'.title(), relief = SUNKEN, anchor = W)
		self.statusbar.pack(side = BOTTOM, fill = X)


		#background image
		self.bkimg = PhotoImage(file = 'images.gif')
		self.bklabel = Label(root, image = self.bkimg, height = 768, width = 1360)
		self.bklabel.pack()

		#font
		self.fontl = ('Times', -20, 'bold')

		
		#login label

		self.mainlabel = ttk.Label(root, text = 'Log in', font = self.fontl)
		self.mainlabel.place(x = 250, y = 100)

		#user name
		self.lusername = ttk.Label(root, text = 'username', font = self.fontl)
		self.lusername.place(x = 160, y = 150)

		self.eusername = ttk.Entry(root, font = self.fontl)
		self.eusername.place(x = 260, y = 150)


		#password

		self.lpassword = ttk.Label(root, text = 'password', font = self.fontl)
		self.lpassword.place(x = 160, y = 200)

		self.epassword = ttk.Entry(root, font = self.fontl, show = "*")
		self.epassword.place(x = 260, y = 200)


		#buttons

		self.loginb = ttk.Button(root, text = 'Log in', command = self.loginvalues)
		self.loginb.place(x = 200, y = 250)

		self.exitb = ttk.Button(root, text = 'Exit', command = root.destroy)
		self.exitb.place(x = 300, y = 250)
		 
		self.window = root

	def loginvalues(self):
		name = self.eusername.get()
		passw = self.epassword.get()
		
		yes, fname, lname, branch = login.logindash(name, passw)

		

		if yes == True:
			if os.path.isfile("enc.txt"):
				os.system("del enc.txt")
				
			with open("enc.txt","w") as f:
				data = name + " " + passw
				f.write(data)
			self.window.destroy()
			dashwindow = Tk()
			dashwindow.geometry("1360x700")
			obj = DashBoard(dashwindow,fname,lname,branch,["Del","programming","cpp"])
			obj.plot_graphh()
			obj.att_data(60, 40, 20)
			dashwindow.mainloop()
		else:
			self.statusbar['text'] = "Your Username or Password is not correct : Invalid Input".title()
			messagebox.showinfo("Invalid Input","Your Username or Password is not correct")



if __name__ == "__main__":
	loginwindow = Tk()
	loginwindow.geometry("600x400")
	loginwindow.resizable(0, 0)

	logobj = Log(loginwindow)
	loginwindow.mainloop()


