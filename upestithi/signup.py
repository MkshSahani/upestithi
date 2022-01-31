from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import firstpage
#user defined 
#import hashlib
import login

class Signup:
	def __init__(self, root):



		#font 
		self.label_font = ('Times', -20, 'bold')



		#propetry of the window
		root.geometry("600x400")
		root.title("Sign up".title())
		root.resizable(0, 0)
		root.wm_iconbitmap('favicon.ico')
		self.backgroundimage = 'images.gif'
		self.backgroundimage = PhotoImage(file = self.backgroundimage)
		self.backlabel = Label(root, image = self.backgroundimage, height = 768, width = 1360)
		self.backlabel.pack()
		#signup label

		#self.signlabel = ttk.Label(root, text = 'sign up'.title(), font = self.label_font)
		#self.signlabel.place(x = 150, y = 10)


		#names
		self.firstname = ttk.Label(root, text = 'first name : '.title(), font = self.label_font)
		self.efirstname = ttk.Entry(root, font = self.label_font)

		self.lastname = ttk.Label(root, text = 'second name : '.title(), font = self.label_font)
		self.elastname = ttk.Entry(root, font = self.label_font)
		#password
		self.fpassword = ttk.Label(root, text = 'password'.title(), font = self.label_font)
		self.efpassword = ttk.Entry(root, font = self.label_font, show = "*")
		self.branch = ttk.Label(root, text = 'branch'.title(), font = self.label_font)
		self.ebranch = ttk.Entry(root, font = self.label_font)
		#email 
		self.email = ttk.Label(root, text = 'email'.title(), font = self.label_font)
		self.eemail = ttk.Entry(root, font = self.label_font)
		#user name
		self.username = ttk.Label(root, text = 'user names'.title(), font = self.label_font)
		self.eusername = ttk.Entry(root, font = self.label_font)


		#packing the elements

		self.firstname.place(x = 50, y = 60)
		self.efirstname.place(x = 220, y = 60)
		self.lastname.place(x = 50, y = 110)
		self.elastname.place(x = 220, y = 110)
		
		self.fpassword.place(x = 50, y = 160)
		self.efpassword.place(x = 220, y = 160)
		self.branch.place(x = 50, y = 210)
		self.ebranch.place(x = 220, y = 210)
		self.email.place(x = 50, y = 260)
		self.eemail.place(x = 220, y = 260)
		self.username.place(x = 50, y = 310)
		self.eusername.place(x = 220, y = 310)



		#register button

		self.registerbutton = ttk.Button(root, text = 'Register', command = self.signup_on)
		self.registerbutton.place(x = 500, y = 250)
		self.exitbutton = ttk.Button(root, text = 'Exit', command = self.exitbutton)
		self.exitbutton.place(x = 500, y = 300)

		self.window	= root



	def signup_on(self):
		fname = self.efirstname.get()
		lname = self.elastname.get()
		sbranch = self.ebranch.get()
		semail = self.eemail.get()
		susername = self.eusername.get()

		if fname == "" or lname == "" or sbranch == "" or semail == "" or susername == "":
			messagebox.showinfo("info", "some fields are empty")

		else:
			try:		
				login.signin(self.efirstname.get(),self.elastname.get(),self.efpassword.get(),self.ebranch.get(),self.eemail.get(),self.eusername.get())
				messagebox.showinfo("Info",f"Thanks {self.efirstname.get()} {self.elastname.get()} Data is registerd \n please exit the sign up".title())
			
			
			except:
				messagebox.showinfo("info", f"the user name {susername} is already taken")
	
			
		'''
		print(self.efirstname.get())
		print(self.elastname.get())
		print(self.eemail.get())
		print(self.eusername.get())
		print(self.efpassword.get())
		print(self.ebranch.get())
		'''

	def exitbutton(self):
		self.window.destroy()
		mainwindow = Tk()
		mainwindow.wm_iconbitmap('favicon.ico')
		mainwindow.title("Upestithi")
		mainwindow.geometry("600x400")
		mainwindow.resizable(0, 0)
		obj = firstpage.Firstpage(mainwindow)
		mainwindow.mainloop()

if __name__ == "__main__":
	signapp = Tk()
	signupwindow = Signup(signapp)
	signapp.mainloop()


