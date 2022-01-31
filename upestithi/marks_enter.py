import pandas as pd
def update_marks(branch,subject,semester,rollno,score):
	df=pd.read_excel(semester+'/'+branch+'/'+subject+'.xlsx')
	dic={}
	t=list(df.columns)
	for i in range (0,df.shape[0]):
		dic['{0}'.format(df.ix[i,t[0]])]=df.ix[i,t[1]]
	
	
	dic[rollno.upper()]=score
	ls=list(dic.keys())
	
	
	
	dc={'Rollno':ls,'Marks':[dic['{0}'.format(ls[i])] for i in range(0,len(ls))]}
	aq=pd.DataFrame(dc)
	aq.to_excel(semester+'/'+branch+'/'+subject+'.xlsx')

if __name__ == "__main__":

	update_marks('cse','Del','1','CO18326','25')