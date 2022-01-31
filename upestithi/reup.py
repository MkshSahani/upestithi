import dashboard
import login
from  tkinter import *

def reopen_sigin():
	data1 = " "
	with open("enc.txt","r") as f:
		data1 = f.read()


	lst = data1.split(" ")
	print(lst[0])
	print(lst[1])
	yes, fname, lname, branch = login.logindash(lst[0], lst[1])
	if yes == True:
		dashwindow = Tk()
		dashwindow.geometry("1360x700")
		obj = dashboard.DashBoard(dashwindow,fname,lname,branch,["Del","programming","cpp"])
		obj.plot_graphh()
		obj.att_data(60, 40, 20)
		dashwindow.mainloop()
	else:
		print("not valid")

if __name__ == "__main__":			

	reopen_sigin()