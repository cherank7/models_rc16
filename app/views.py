from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    tn=input('enter a topic nm:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Topic data inserted successfully')


def insert_web(request):
    tn=input('enter a name:')
    n=input('enter a name:')
    u=input('enter a url:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('WEb data inserted successfully')




def insert_topic(request):
    lot=Topic.objects.all()
    d={'names':lot}
    return render(request,'insert_topic.html',context=d)



def insert_web(request):
    wo=Webpage.objects.all()
    d={'web':wo}
    return render(request,'insert_web.html',context=d)