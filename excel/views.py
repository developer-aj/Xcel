from django.shortcuts import render, redirect
from .models import Data
from .forms import XlsForm
import xlrd

# Create your views here.
def main(request):
	d = Data.objects.all().order_by('roll')
	return render(request, 'excel/index.html', {'d': d})

def post_new(request):
	if request.method == "POST":
		form = XlsForm(request.POST, request.FILES)
        	if form.is_valid():
           		handle_uploaded_file(request.FILES['xfile'])
			#extraction
			extract('temp.xls')
			return redirect('excel.views.main')
	else:
		form = XlsForm()
	return render(request, 'excel/new.html', {'form': form})

def handle_uploaded_file(f):
    with open('temp.xls', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def extract(path):
	book = xlrd.open_workbook(path)
	n = book.nsheets
	for i in xrange(n):
		worksheet = book.sheet_by_index(i)
		for j in xrange(worksheet.nrows):
			data = Data(roll=str(worksheet.cell(j,0).value), pwd=str(worksheet.cell(j,1).value))
			data.save()
