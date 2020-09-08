from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse

from .models import Tweet

# Create your views here.

def home_view(request,*args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"pages/home.html",context={},status=200)


def tweet_detail_view(request,tweet_id,*args,**kwargs):
    data={
        "id":tweet_id,
        #"contetn":obj.content, 

    }
    status=200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message']="Not found"
        status=404


    #return HttpResponse("<h1>Hello World</h1>")
    
    return JsonResponse(data,status=status) #same as json.dumps 
    return HttpResponse(f"<h1>Hello World {tweet_id}-{obj.content}</h1>")
    #path('tweets/<int:tweet_id>',tweet_detail_view),

