import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import offline
import pandas as pd
import numpy as np
from selenium import webdriver
N = 500
x = np.linspace(0, 1, N)
y = np.random.randn(N)
def xltograph(inputfile_name):
	df = pd.read_excel(inputfile_name)


	data = [
		go.Scatter(
			x=df['Date'], # assign x as the dataframe column 'x'
			y=df['Total Student'],
			name="12th may"
		)
	]
	lay=go.Layout(title="Total attendance report",yaxis=dict(title="Total Present"),xaxis=dict(title="Date"))
	# IPython notebook
	# py.iplot(data, filename='pandas/basic-line-plot')
	fig=go.Figure(data=data,layout=lay)
	offline.plot(fig,auto_open=True )
xltograph('dailyrecord.xlsx')