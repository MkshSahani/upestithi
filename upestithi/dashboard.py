"""

	dashboard for user to allow the user
	to acess all the features.

	dashboard is for every user.


"""

from tkinter import *
from tkinter import ttk 
from threading import *
import time
import cv2
import PIL.Image,PIL.ImageTk
import pandas as pd
import numpy as np

import pandas as pd
from tkinter import messagebox
import matplotlib
import os

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure

#our defined libaray

from list import *
import Extraclass
import marks_enter

#aumtation

import uhack

#automation

class DashBoard:
	def __init__(self, root, name, position, branch_, sub):
		root.state('zoomed')
		root.wm_iconbitmap('favicon.ico')
		self.name = name
		self.position = position
		self.branch_ = branch_
		self.sub = sub
		root.title(f"{self.name} / {self.position} / {self.branch_} ")

		self.listsubject = tuple(self.sub)


		#self.currtime = date.today()
		self.menubar = Menu(root)
		root.config(menu = self.menubar)
		
		self.toolmenu = Menu(root, tearoff = 0)
		self.toolmenu.add_command(label = "Start Attandance system", command = self.automatesys)
		self.toolmenu.add_command(label = "Attandance Data", command = self.attandance_list)
		self.toolmenu.add_command(label = "Video records", command = self.record_vedio)
		self.toolmenu.add_command(label = "Result data", command = self.listofmarks)
		#self.toolmenu.add_command(label = "Add the class", command = self.add_class)
		#self.toolmenu.add_Separator()
		self.toolmenu.add_command(label = "Exit", command = root.destroy)


		self.datamenu = Menu(root, tearoff = 0)
		self.datamenu.add_command(label  = "Get report card".title())
	

		self.helpmenu = Menu(root, tearoff = 0)
		self.helpmenu.add_command(label = "Help")


		self.menubar.add_cascade(label = "Tool", menu = self.toolmenu)
		self.menubar.add_cascade(label = "Data", menu = self.datamenu)
		self.menubar.add_cascade(label = "Help", menu = self.helpmenu)

		
		
		
		#top most frame

		self.font1 = ('Times', -20, 'bold')

		self.topframe = Frame(root, height = 50, width = 1360, bg = 'sky blue')
		self.topframe.place(x = 0, y = 0)

		self.wlabel = Label(self.topframe, text = 'Welcome in Upestithi', font = self.font1, bg = 'sky blue', fg = 'white')
		self.wlabel.place(x = 5, y = 10)
	
		self.signoutbutton = ttk.Button(self.topframe, text = 'sign out'.title(), command = self.sigout_profile)
		self.signoutbutton.place(x = 1250, y = 15)


		#notice board

		self.notice = Frame(root, height = 450, width = 200)
		self.notice.place(x = 5, y = 70)

		self.namelabel = Label(self.notice, text = f"Welcome {self.name}", font = self.font1, fg = 'blue')
		self.namelabel.pack()

		self.get_list_of_present = ttk.Button(self.notice, text = 'present student list'.title(), command = self.attandance_list)
		self.get_list_of_present.pack(pady = 10)
		self.get_list_of_student = ttk.Button(self.notice, text = '     List of student    '.title(), command = self.liststudent)
		self.get_list_of_student.pack(pady = 10)
		self.get_list_of_marks = ttk.Button(self.notice, text =   '    List of marks       '.title(), command = self.listofmarks)
		self.get_list_of_marks.pack(pady = 10)
		self.get_syllabus = ttk.Button(self.notice, text =        '       syllabus              '.title(), command = self.syllabuslist)
		self.get_syllabus.pack(pady = 10)
		self.get_video_record = ttk.Button(self.notice, text =    '    Video recording      '.title(), command = self.record_vedio)
		self.get_video_record.pack(pady = 10)


		#for graph

		self.graphc = Canvas(root, height = 400, width = 1000)
		self.graphc.place(x = 200, y = 70)

		self.graphlabel = Label(root, text = 'Attandance vs Date', font = self.font1, bg = 'white')
		self.graphlabel.place(x = 600, y = 70)

		

		#personal details
		self.attandance_frame = Frame(root, height = 450, width = 200)
		self.attandance_frame.place(x = 1200, y = 70)
		self.att_label = ttk.Label(self.attandance_frame, text = 'personal details'.title())
		self.att_label.pack(padx = 20)


		#result fead
		
		self.bframe = Frame(root, bg = 'sky blue', width = 1360, height = 400)
		self.bframe.place(x = 0, y = 400)

		self.rtitle = Label(root, bg = 'sky blue', text = 'Result feed'.title(), font = self.font1)
		self.rtitle.place(x = 600, y = 400)
		self.branch = StringVar()
		self.std = StringVar()
		
		self.llstd = ("1","2","3","4","5","6","7","8")

		self.esubject = StringVar()

		self.font1 = ('Times', -20, 'bold')
		self.branchtup = ("CSE","ME","ECE","EEE","IT","CIVIL")



		self.branchlabel = ttk.Label(root, text = "branch".title(), font = self.font1)
		self.spinbranch = Spinbox(root, textvariable = self.branch, values = self.branchtup, font = self.font1)
		self.branchlabel.place(x = 50, y = 470)
		self.spinbranch.place(x = 150, y = 470)

		self.stdlabel = ttk.Label(root, text = "semester".title(), font = self.font1)
		self.spinstd = Spinbox(root, textvariable = self.std, values = self.llstd, font = self.font1)
		self.stdlabel.place(x = 50, y = 550)
		self.spinstd.place(x = 150, y = 550)


		self.subjectlabel = ttk.Label(root, text = 'Subject', font = self.font1)
		self.spinsubject = Spinbox(root,font = self.font1, textvariable = self.esubject, values = self.listsubject)
		self.subjectlabel.place(x = 450, y = 470)
		self.spinsubject.place(x = 550, y = 470)


		self.rollnolabel = ttk.Label(root, text = 'Roll no ', font = self.font1)
		self.erollno = ttk.Entry(root, font = self.font1)
		self.rollnolabel.place(x = 450, y = 550)
		self.erollno.place(x = 550, y = 550)


		self.scorelabel = ttk.Label(root, text = 'Score', font = self.font1)
		self.escore = ttk.Entry(root, font = self.font1)
		self.scorelabel.place(x = 800, y = 470)
		self.escore.place(x = 900, y = 470)

		self.scoresubmit = ttk.Button(root, text = 'Submit Score', command = self.submit_score)
		self.scoresubmit.place(x = 1150, y = 470)


		self.statusbar = Label(root, relief =  SUNKEN, anchor = W, text  = f'Welcome in Upestithi mr.{self.name}')
		self.statusbar.pack(side= BOTTOM, fill = X)

		self.window = root



	def automatesys(self):
		self.window.destroy()
		if self.branch_ == "CSE" or self.branch_ == "cse":
			uhack.automation(0)
		else:
			uhack.automation(1)


	def sigout_profile(self):
		os.system("del enc.txt")
		self.window.destroy()



	def att_data(self, total, present, absent):
		self.tlabel = ttk.Label(self.attandance_frame, text = f"First Name : {self.name}")
		self.plabel = ttk.Label(self.attandance_frame, text = f"Last Name : {self.position}")
		self.alabel = ttk.Label(self.attandance_frame, text = f"branch  : {self.branch_}")
		self.tlabel.pack(padx = 10, pady = 20)
		self.plabel.pack(padx = 10, pady  =20)
		self.alabel.pack(padx = 10, pady = 20)


	def plot_graphh(self):
		fname = "dailyrecord.xlsx"
		f = Figure(figsize = (10,3), dpi = 100)
		a = f.add_subplot(111)
		#b = f.add_subplot(111)

		df=pd.read_excel(fname,engine='openpyxl')
		x=[i for i in df.iloc[:,0]]
		y=[i for i in df.iloc[:,1]]

 		

		

		#z = pow(x , 3)
		
		a.plot(x,y,label = 'Working')
		a.legend(['Attandance with data'], loc = 3)
		#b.plot(x,[0, 4,7,8,9,12,19,29,175,788,52,22,12,10], label = "w")
		Canvas = FigureCanvasTkAgg(f, self.graphc)
		#Canvas.show()
		Canvas.get_tk_widget().pack()


	def attandance_list(self):
		self.window.destroy()
		self.attapp = Tk()
		self.attapp.geometry("500x400")
		self.att_list = AttandaceList(self.attapp)
		self.attapp.mainloop()


	def record_vedio(self):
		self.window.destroy()
		self.vttapp = Tk()
		self.vttapp.geometry("500x400")
		self.vtt_list = VideoPlay(self.vttapp)
		self.vttapp.mainloop()



	def liststudent(self):
		self.window.destroy()
		self.stuapp = Tk()
		self.stuapp.geometry("500x400")
		self.stu_list = ListStudent(self.stuapp)
		self.stuapp.mainloop()


	def syllabuslist(self):
		self.window.destroy()
		self.syllapp = Tk()
		self.syllapp.geometry("500x400")
		self.syll_list =SyllabusSem(self.syllapp)
		self.syllapp.mainloop()


	def listofmarks(self):
		self.window.destroy()
		self.marksapp = Tk()
		self.marksapp.geometry("500x400")
		self.result_stu = ListMarks(self.marksapp)
		self.marksapp.mainloop()		


	def submit_score(self):
		branch_  = self.branch.get()
		semester_ = self.std.get()
		roll_ = self.erollno.get()
		subject_ = self.esubject.get()
		score_ = self.escore.get()

		
		marks_enter.update_marks(branch_.lower(),subject_,semester_,roll_,score_)
		messagebox.showinfo("Info","Data is updated")
	def add_class(self):
		self.window.destroy()
		self.addapp = Tk()
		self.addapp.geometry("600x400")

		addclass = Extraclass.Extrac(self.addapp)
		self.addapp.mainloop()

		
'''

	def listofpresent(self):



class ListPresent:
	def __init__(self, root):
		root.wm_iconbitmap('favicon.ico')
		root.

'''

if __name__ == "__main__":

	root = Tk()
	root.geometry("1360x700")
	obj = DashBoard(root,"mukesh","professor","CSE",["Del","programming","c++"])
	obj.plot_graphh()
	obj.att_data(60, 40, 20)
	root.mainloop()