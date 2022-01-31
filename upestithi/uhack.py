import face_recognition
import cv2
import numpy as np
import pandas as pd
import smtplib as smt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as ddt
import requests
import numpy as np
def automation(ab):
	
	
	forcc=cv2.VideoWriter_fourcc(*'MJPG')
	writer=cv2.VideoWriter(ddt.datetime.now().strftime('%d')+ddt.datetime.now().strftime('%b')+'.avi',forcc,1,(640,480))
	sew=smt.SMTP('smtp.gmail.com',587)
	sew.starttls()
	sew.login('co18326@ccet.ac.in','Ishu17@19')
	vid=cv2.VideoCapture(0)
	d2=pd.read_excel('dailyrecord.xlsx',engine='openpyxl')
	df=pd.read_excel('class.xlsx',engine='openpyxl')
	Total_stdents=df.shape[0]
	er=[]
	present=[]
	for i in range(0,Total_stdents):
		picture_file='pictuers/{0}.jpg'.format(i)
		prisha=face_recognition.load_image_file(picture_file)
		prisha_face=face_recognition.face_encodings(prisha)[0]
		er.append(prisha_face)
	frame_checker=True

	while True:
		name=[]
		if ab==0:
			ret,frame=vid.read()
		if ab==1:
			url='http://192.168.43.99:8080/shot.jpg'
			img_resp=requests.get(url)
			img1_obj=np.array(bytearray(img_resp.content),dtype=np.uint8)
			frame=cv2.imdecode(img1_obj,-1)
		small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
		rgb=small_frame[:,:,::-1]
	
		
		face_avalable=face_recognition.face_locations(rgb)
		face_ebcv=face_recognition.face_encodings(rgb,face_avalable)
		if frame_checker:
			for it in face_ebcv:
				mathes=face_recognition.compare_faces(er,it)
				distances=face_recognition.face_distance(er,it)
				miv=np.argmin(distances)
				if mathes[miv]:
					print(miv)
					present.append(miv)
					name.append(df.iloc[miv,1])
				else:
					name.append('Unknown')
		feame_checker=not frame_checker
		for (top,right,buttom,left),neta in zip(face_avalable,name):
			top*=4
			right*=4
			buttom*=4
			left*=4
			cv2.rectangle(frame,(left,top),(right,buttom),(0,0,255),2)
			cv2.rectangle(frame,(left,buttom-35),(right,buttom),(0,0,255),cv2.FILLED)
			font=cv2.FONT_HERSHEY_DUPLEX
			print(neta)
			cv2.putText(frame,neta,(left+6,buttom-6),font,1.0,(255,255,255),1,cv2.LINE_AA)
		writer.write(frame)
		cv2.imshow("Student Attandance Automation System",frame)
		if cv2.waitKey(2) == 27:
			break
	
	vid.release()
	cv2.destroyAllWindows()
	present=list(set(present))
	present_name=[]
	print(present)
	for iu in range(0,Total_stdents):
		if iu in present:
			present_name.append(df.iloc[iu,1])
			df.iloc[iu,3]+=1
		if iu not in present:
			message=MIMEMultipart('alternative')
			message['Subject']='Attendance Notice'
			message['From']='co18326@ccet.ac.in'
			message['To']=df.iloc[iu,2]
			text="""\
			<html>
			<head></head>
			<body>
			<h1> dear {0},</h1>
			<b>you have been marked absent by our software on <i>{1},{2},{3}at{4}:{5} {6}</i></b></body>
			</html>
			""".format(df.iloc[iu,1],ddt.datetime.now().strftime("%d"),ddt.datetime.now().strftime("%b"),ddt.datetime.now().strftime("%Y"),ddt.datetime.now().strftime("%I"),ddt.datetime.now().strftime("%M"),ddt.datetime.now().strftime("%p"))
			met=MIMEText(text,'html')
			message.attach(met)
			sew.sendmail('co1836@ccet.ac.in',df.iloc[iu,2],message.as_string())
	existing_length=d2.shape[0]
	isss={}
	l=d2.iloc[:,0]
	l1=d2.iloc[:,1]
	
	l=[i for i in l]
	l1=[i for i in l1]
	for i,n in zip(l,l1):
		isss[i]=n
	filename=ddt.datetime.now().strftime("%d")+" "+ddt.datetime.now().strftime("%b")+".xlsx"
	isss[ddt.datetime.now().strftime("%d")+" "+ddt.datetime.now().strftime("%b")]=len(present)
	l1.append(len(present))
	dic={'Date':list(isss.keys()),'Total Student':[ isss[list(isss.keys())[i]] for i in range(0,len(list(isss.keys())))]}
	dic2={'List of Present Students':present_name}
	d2=pd.DataFrame(dic)
	d2.to_excel('dailyrecord.xlsx',index=False)
	d2=pd.DataFrame(dic2)

	d2.to_excel(filename,index=False)
	#df.to_excel('class.xlsx')
	return present_name

if __name__ == "__main__":
	lk=automation(0)