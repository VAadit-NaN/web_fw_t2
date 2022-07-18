from django.shortcuts import render

from dashboard.models import CountryData

# Create your views here.
def index(request):
    data = CountryData.objects.all()

    context = {
        'data':data
    }
    return render(request, 'dashboard/index.html', context)

def handle_csv(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        #POST logic here
    else:
        return render(request, 'admin/upload_csv.html')
