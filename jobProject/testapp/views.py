from django.shortcuts import render
from testapp.models import AndheriJob,ThaneJob,DadarJob

# Create your views here.
def indexView(request):
    return render(request,'testapp/index.html')

def andheri_job_view(request):
    job_list=AndheriJob.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/AndheriJob.html',context=my_dict)

def thane_job_view(request):
    job_list=ThaneJob.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/ThaneJob.html',context=my_dict)

def dadar_job_view(request):
    job_list=DadarJob.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/DadarJob.html',context=my_dict)
