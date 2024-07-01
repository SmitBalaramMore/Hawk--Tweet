from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404,message

# Create your views here.

def ALL_Tweets(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,"alltweets.html",{'tweets':tweets})

def Create_Tweets(request):
    if request.method=="POST":
        forms=TweetForm(request.POST,request.FILES)
        if forms.is_valid():
            tweet=forms.save(commit=True)
            tweet.user=request.user
            tweet.save()
            return redirect("ALL_tweet")
    else:
        forms=TweetForm()
    return render(request,"TweetForm.html",{"forms":forms})


def Edit_tweets(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
      forms=TweetForm(request.POST,request.FILES,instance=tweet)
      if forms.is_valid():
          tweet=forms.save(commit=False)
          tweet.user=request.user
          tweet.save()
          return redirect ("ALL_Tweets") 
    else:
        forms=TweetForm(instance=tweet)
    return render (request,"alltweets.html",{"forms":forms})


def Delete_tweets(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect("ALL_Tweets")
    return render(request,"tweet_confrim_delete.html",{'tweet':tweet})


        

 
