from tkinter import *
from tkinter import ttk 
import os
from tkinter import messagebox
#user defined module

import reup
import ty

class AttandaceList:
	def __init__(self, root):
		root.title('AttandaceList')
		root.wm_iconbitmap('favicon.ico')
		self.font1 = ('Arial', -20, 'bold italic')
		root.resizable(0, 0)
		self.bkimage = PhotoImage(file = 'images.gif')
		self.bklabel = Label(root, height = 1360, width = 768, image = self.bkimage)
		self.bklabel.pack()


		self.mainlabel = Label(root, text= 'Please select the date'.title(), font = self.font1)
		self.mainlabel.place(x = 100, y = 10)

		self.datelabel = Label(root, text = 'Date', font = self.font1)
		self.datelabel.place(x = 10, y = 90)
		self.monthlabel = Label(root, text = 'Month', font = self.font1)
		self.monthlabel.place(x = 10, y = 140)
		self.yearlabel = Label(root, text = 'Year', font = self.font1)
		self.yearlabel.place(x = 10, y = 190)

		self.date = IntVar()
		self.month = StringVar()
		self.year = IntVar()

		self.spindate = Spinbox(root, from_ = 1, to = 31, textvariable = self.date, font = self.font1)
		self.spindate.place(x = 110, y = 90)
		self.spinmonth = Spinbox()

		self.m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		#self.m1 = [i.upper() for i in self.m]
		self.mon = tuple(self.m)

		self.spinmonth = Spinbox(root, textvariable = self.month, values = self.mon, font = self.font1)
		self.spinmonth.place(x = 110, y = 140)

		self.spinyear = Spinbox(root, from_ = 2018, to = 3000, font = self.font1, textvariable = self.year)
		self.spinyear.place(x = 110, y = 190) 

		self.confirm = ttk.Button(root, text = 'Get List'.title(), command = self.onconfirm)
		self.confirm.place(x = 120, y = 270)

		self.closeb = ttk.Button(root, text = 'Close', command = self.cancel_b)
		self.closeb.place(x = 270, y = 270)
		self.window = root

	def onconfirm(self):
	
		valdate = self.date.get()
		valmonth = self.month.get()
		valyear = self.year.get()

		fname = str(valdate) + " " + valmonth + ".xlsx"
		if os.path.isfile(fname):
			ffname = f"present_student.pdf" 
			print(fname)
			print(valdate)
			print(valmonth)
			print(valyear)
			print("working 1")
			ty.xltopdfconvert(fname,ffname)
			print("working 2")
			messagebox.showinfo("info",f"the pdf is created source name : {ffname}")
			os.system('C:/Users/acer/Documents/'+ffname)
		else:
			messagebox.showinfo("info","data is not avialable")		
	def cancel_b(self):
		self.window.destroy()
		reup.reopen_sigin()



class VideoPlay:
	def __init__(self, root):
		root.title('Recorded Video')
		root.wm_iconbitmap('favicon.ico')
		self.font1 = ('Arial', -20, 'bold italic')
		root.resizable(0, 0)
		self.bkimage = PhotoImage(file = 'images.gif')
		self.bklabel = Label(root, height = 1360, width = 768, image = self.bkimage)
		self.bklabel.pack()


		self.mainlabel = Label(root, text= 'Please select the date'.title(), font = self.font1)
		self.mainlabel.place(x = 100, y = 10)

		self.datelabel = Label(root, text = 'Date', font = self.font1)
		self.datelabel.place(x = 10, y = 90)
		self.monthlabel = Label(root, text = 'Month', font = self.font1)
		self.monthlabel.place(x = 10, y = 140)
		self.yearlabel = Label(root, text = 'Year', font = self.font1)
		self.yearlabel.place(x = 10, y = 190)

		self.date = IntVar()
		self.month = StringVar()
		self.year = IntVar()

		self.branch = StringVar()
		self.std = StringVar()

		self.spindate = Spinbox(root, from_ = 1, to = 31, textvariable = self.date, font = self.font1)
		self.spindate.place(x = 140, y = 90)
		self.spinmonth = Spinbox()

		self.m = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
		self.m1 = [i for i in self.m]
		self.mon = tuple(self.m1)

		self.spinmonth = Spinbox(root, textvariable = self.month, values = self.mon, font = self.font1)
		self.spinmonth.place(x = 140, y = 140)

		self.spinyear = Spinbox(root, from_ = 2019, to = 2020, font = self.font1, textvariable = self.year)
		self.spinyear.place(x = 140, y = 190) 

		self.branchtup = ("CSE","ME","ECE","EEE","IT","CIVIL")
		self.yeartup = ("first","second","third","fourth")

		self.monthlabel = Label(root, text = 'Branch', font = self.font1)
		self.monthlabel.place(x = 10, y = 240)
		self.yearlabel = Label(root, text = 'course year', font = self.font1)
		self.yearlabel.place(x = 10, y = 290)

		self.spinbranch = Spinbox(root, textvariable = self.branch, values = self.branchtup, font = self.font1)
		self.spinstd = Spinbox(root, textvariable = self.std, values = self.yeartup, font = self.font1)

		self.spinbranch.place(x = 140, y = 240)
		self.spinstd.place(x = 140, y = 290)



		self.confirm = ttk.Button(root, text = 'Play Video'.title(), command = self.onconfirm)
		self.confirm.place(x = 120, y = 340)

		self.closeb = ttk.Button(root, text = 'Close', command = self.cancel_b)
		self.closeb.place(x = 270, y = 340)
		self.window = root

	def onconfirm(self):
	
		valdate = self.date.get()
		valmonth = self.month.get()
		valyear = self.year.get()
		valb = self.branch.get()
		valstd = self.std.get()
		print(valdate)
		print(valmonth)
		print(valyear)
		print(valb)
		print(valstd)

		fname = str(valdate) + valmonth + ".avi"

		if os.path.isfile(fname):
			os.system(fname)
		else:
			messagebox.showinfo("Info", "data is not avialable")

	def cancel_b(self):
		self.window.destroy()
		reup.reopen_sigin()


class ListStudent:
	def __init__(self, root):
		root.wm_iconbitmap('favicon.ico')
		root.title('List of student')
		root.resizable(0, 0)
		self.bkimg = PhotoImage(file = 'images.gif')
		self.mainlabel  = Label(root, height = 768, width = 1360, image = self.bkimg)
		self.mainlabel.pack()
		self.font1 = ('Arial', -20, 'bold italic')

		self.branchtup = ("cse","me","ece","eee","it","civil")
		self.yeartup = (1,2,3,4)

		self.branch = StringVar()
		self.std = IntVar()

		self.mainlabel = Label(root, text = "List of stduent".title(), font = self.font1)
		self.mainlabel.place(x = 150, y = 100)

		self.lbranch = Label(root, text = 'Branch', font = self.font1)
		self.lyear = Label(root, text = 'Year', font = self.font1)
		self.lbranch.place(x = 100, y = 150)
		self.lyear.place(x = 100, y = 200)


		self.spinbranch = Spinbox(root, textvariable = self.branch, values = self.branchtup, font = self.font1)
		self.spinstd = Spinbox(root, textvariable = self.std, values = self.yeartup, font = self.font1)

		self.spinbranch.place(x = 200, y = 150)
		self.spinstd.place(x = 200, y = 200)



		self.confirm = ttk.Button(root, text = 'get list'.title(), command = self.onconfirm)
		self.confirm.place(x = 120, y = 250)

		self.closeb = ttk.Button(root, text = 'Close', command = self.cancel_b)
		self.closeb.place(x = 270, y = 250)
		self.window = root

	def onconfirm(self):
		valb = self.branch.get()
		valstd = self.std.get()

		fname = str(valstd) + '/' + valb + '/' + "class.xlsx"

		if os.path.isfile(fname):
			ffname = 'listofstudent.pdf'
			ty.xltopdfconvert(fname,ffname)
			messagebox.showinfo("Info",f"the pdf is creadted in {ffname}")
			
			os.system('C:/Users/acer/documents/'+ffname)
		else:
			messagebox.showinfo("data is not avialable")




	def cancel_b(self):
		self.window.destroy()
		reup.reopen_sigin()

class SyllabusSem:
	def __init__(self, root):
		root.wm_iconbitmap('favicon.ico')
		root.title("Syllabus".title())
		root.resizable(0, 0)
		self.bkimg = PhotoImage(file = 'images.gif')
		self.mainlabel  = Label(root, height = 768, width = 1360, image = self.bkimg)
		self.mainlabel.pack()
		self.font1 = ('Arial', -20, 'bold italic')

		self.branchtup = ("CSE","ME","ECE","EEE","IT","CIVIL")
		

		self.branch = StringVar()
		self.std = IntVar()

		self.mainlabel = Label(root, text = "Syllabus of semester".title(), font = self.font1)
		self.mainlabel.place(x = 150, y = 100)

		self.lbranch = Label(root, text = 'Branch', font = self.font1)
		self.lyear = Label(root, text = 'year', font = self.font1)
		self.lbranch.place(x = 100, y = 150)
		self.lyear.place(x = 100, y = 200)


		self.spinbranch = Spinbox(root, textvariable = self.branch, values = self.branchtup, font = self.font1)
		self.spinstd = Spinbox(root, textvariable = self.std, from_ = 1, to = 4, font = self.font1)

		self.spinbranch.place(x = 200, y = 150)
		self.spinstd.place(x = 200, y = 200)



		self.confirm = ttk.Button(root, text = 'get list'.title(), command = self.onconfirm)
		self.confirm.place(x = 120, y = 250)

		self.closeb = ttk.Button(root, text = 'Close', command = self.cancel_b)
		self.closeb.place(x = 270, y = 250)
		self.window = root

	def onconfirm(self):
		valb = self.branch.get()
		valstd = self.std.get()
		print(valb)
		print(valstd)

		
		fname = "syy" + valb + str(valstd) + ".pdf"

		if os.path.isfile(fname):
			messagebox.showinfo("info".title(), "Data found press Ok to views")
			os.system(fname)
		else:
			messagebox.showinfo("info".title(),"data not avialable")


	def cancel_b(self):
		self.window.destroy()
		reup.reopen_sigin()

class ListMarks:
	def __init__(self, root):
		root.title('Result of student')
		root.wm_iconbitmap('favicon.ico')
		self.font1 = ('Arial', -20, 'bold italic')
		root.resizable(0, 0)
		self.bkimage = PhotoImage(file = 'images.gif')
		self.bklabel = Label(root, height = 1360, width = 768, image = self.bkimage)
		self.bklabel.pack()


		self.mainlabel = Label(root, text= 'Please select the data'.title(), font = self.font1)
		self.mainlabel.place(x = 100, y = 10)

		
	
		self.monthlabel = Label(root, text = 'Month', font = self.font1)
		self.monthlabel.place(x = 10, y = 140)
		

		
		self.subject = StringVar()


		self.branch = StringVar()
		self.std = IntVar()


		self.m = ['Del','Electronics','Cpp','Datastructure','Database']
		self.m1 = [i.upper() for i in self.m]
		self.mon = tuple(self.m1)

		self.spinsubject = Spinbox(root, textvariable = self.subject, values = self.mon, font = self.font1)
		self.spinsubject.place(x = 140, y = 140)



		self.branchtup = ("CSE","ME","ECE","EEE","IT","CIVIL")
		self.yeartup = (1,2,3,4,5,6,7,8)

		self.monthlabel = Label(root, text = 'Branch', font = self.font1)
		self.monthlabel.place(x = 10, y = 190)
		self.yearlabel = Label(root, text = 'course year', font = self.font1)
		self.yearlabel.place(x = 10, y = 240)

		self.spinbranch = Spinbox(root, textvariable = self.branch, values = self.branchtup, font = self.font1)
		self.spinstd = Spinbox(root, textvariable = self.std, values = self.yeartup, font = self.font1)

		self.spinbranch.place(x = 140, y = 190)
		self.spinstd.place(x = 140, y = 240)



		self.confirm = ttk.Button(root, text = 'get result'.title(), command = self.onconfirm)
		self.confirm.place(x = 120, y = 340)

		self.closeb = ttk.Button(root, text = 'Close', command = self.cancel_b)
		self.closeb.place(x = 270, y = 340)
		self.window = root

	def onconfirm(self):
	
		valsubject = self.subject.get()
		valb = self.branch.get()
		valstd = self.std.get()
		print(valsubject)
		print(valb)
		print(valstd)

		fname = str(valstd) + '/' + valb + '/' + valsubject + ".xlsx"

		if os.path.isfile(fname):
			ffname = 'outmarks.pdf'
			ty.xltopdfconvert(fname,ffname)
			messagebox.showinfo("Info",f"the pdf is creadted in {ffname}")
			os.system('C:/Users/acer/Documents/'+ffname)

		else:
			messagebox.showinfo("data is not avialable")

	def cancel_b(self):
		self.window.destroy()
		reup.reopen_sigin()



if  __name__ == '__main__':
	mainwindow = Tk()
	mainwindow.geometry("600x400")
	obj = ListMarks(mainwindow)
	mainwindow.mainloop()