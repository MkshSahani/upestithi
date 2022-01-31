import pandas as pd
def datamerg(marks_list,attendance_list):
	Marks_list=[[]]
	df=pd.read_excel(marks_list)
	t=list(df.columns)
	for i in range(1,len(t)):
		Marks_list.append([u for u in df.ix[:,t[i]]])
	dt=pd.read_excel(attendance_list)
	tr=list(dt.columns)
	dic={}
    
	for uy in range(0,len(tr)):
		klqw=[i for i in dt.ix[:,tr[uy]]]
		dic[tr[uy]]=klqw
	for ty in range(1,len(Marks_list)):
		dic[t[ty]]=Marks_list[ty]
	dic.pop('Unnamed:',None)
	da=pd.DataFrame(dic)
            
	da.to_excel('combination.xlsx') 
datamerg('Del.xlsx','class.xlsx')
