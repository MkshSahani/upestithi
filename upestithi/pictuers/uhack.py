import face_recognition
import cv2
import numpy as np
import pandas as pd
import smtplib as smt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as ddt
forcc=cv2.VideoWriter_fourcc(*'MJPG')
writer=cv2.VideoWriter('record.avi',forcc,1,(640,480))
sew=smt.SMTP('smtp.gmail.com',587)
sew.starttls()
sew.login('ishugambhir2001@gmail.com','ishu1234')
vid=cv2.VideoCapture(0)
d2=pd.read_excel('dailyrecord.xlsx')
df=pd.read_excel('class.xlsx')
Total_stdents=df.shape[0]
print(Total_stdents)
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
	ret,frame=vid.read()
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
				present.append(miv)
				name.append(df.ix[miv,'Name'])
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
		cv2.putText(frame,neta,(left+6,buttom-6),font,1.0,(255,255,255),1)
	writer.write(frame)
	cv2.imshow("hello",frame)
	if cv2.waitKey(2) == 27:
		break
	
vid.release()
cv2.destroyAllWindows()
present=list(set(present))
present_name=[]
print(present)
for iu in range(0,Total_stdents):
	if iu in present:
		present_name.append(df.ix[iu,'Name'])
		df.ix[iu,'Total Presents']+=1
	if iu not in present:
		message=MIMEMultipart('alternative')
		message['Subject']='Attendance Notice'
		message['From']='ishugambhir2001@gmail.com'
		message['To']=df.ix[iu,'Email']
		text="""\
		<html>
		<head></head>
		<body>
		<h1> dear {0},</h1>
		<b>you have been marked absent by our software on <i>{1},{2},{3}at{4}:{5} {6}</i></b></body>
		</html>
		""".format(df.ix[iu,'Name'],ddt.datetime.now().strftime("%d"),ddt.datetime.now().strftime("%b"),ddt.datetime.now().strftime("%Y"),ddt.datetime.now().strftime("%I"),ddt.datetime.now().strftime("%M"),ddt.datetime.now().strftime("%p"))
		met=MIMEText(text,'html')
		message.attach(met)
		sew.sendmail('ishugambhir2001@gmail.com',df.ix[iu,'Email'],message.as_string())
existing_length=d2.shape[0]
l=d2.ix[:,'Date']
l1=d2.ix[:,'Total Student']
l=[i for i in l]
l1=[i for i in l1]
filename=ddt.datetime.now().strftime("%d")+" "+ddt.datetime.now().strftime("%b")+".xlsx"
l.append(ddt.datetime.now().strftime("%d")+" "+ddt.datetime.now().strftime("%b"))
l1.append(len(present))
dic={'Date':l,'Total Student':l1}
dic2={'List of Present Students':present_name}
d2=pd.DataFrame(dic)
d2.to_excel('dailyrecord.xlsx',index=False)
d2=pd.DataFrame(dic2)

d2.to_excel(filename,index=False)
df.to_excel('class.xlsx')