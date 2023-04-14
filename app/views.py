from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic Inserted successfully ')
    return render(request,'insert_topic.html')




def insert_webpage(request):

    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        return HttpResponse('Webpage Inserted successfully ')
    return render(request,'insert_webpage.html',context=d)


        
    

def insert_access(request):
    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
        AO=AccessRecords.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()

        return HttpResponse('Access Records Inserted successfully ')
    return render(request,'insert_access.html',context=d)

def display_webpage(request):
    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpage.html',context=d)
\
    
def display_topic(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    return render(request,'display_topic.html',context=d)


def display_access(request):
    access=AccessRecords.objects.all()
    d={'access':access}
    return render(request,'display_access.html',context=d)
    



    
    