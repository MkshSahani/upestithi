from win32com import client
import openpyxl
from openpyxl.chart import BarChart,Reference
def xltopdfconvert(inputfile_name,outfile_name):
	xlApp = client.Dispatch("Excel.Application")
	books = xlApp.Workbooks.Open('E:/New folder (3)/{0}'.format(inputfile_name))
	ws = books.Worksheets[0]
	ws.PageSetup.PrintGridlines=1
	ws.SaveAs('{0}'.format(outfile_name),FileFormat=57)
	books.Close(SaveChanges=False)
	xlApp.Quit()

	#ws.Visible = 1
	#ws.ExportAsFixedFormat(0, 'C:/Users/acer/desktop/New folder (3)/{0}'.format(outfile_name))

if __name__ == "__main__":
	xltopdfconvert('28 May.xlsx','out.pdf')