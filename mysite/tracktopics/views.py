from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
import CheckTweetsForWords
from .forms import AddFieldsForm

from .models import TrackingTopic

def index(request):
    latest_topic_list = TrackingTopic.objects.all()
    template = loader.get_template('tracktopics/index.html')
    context = {
        'latest_topic_list': latest_topic_list,
    }
    return HttpResponse(template.render(context, request))
    
def results(request, trackingtopic_id):
    response = "You're looking at the tweets for the topic %s."
    topic = get_object_or_404(TrackingTopic, pk=trackingtopic_id)
    matchingtweets = CheckTweetsForWords.find_tweets(topic)
    print matchingtweets
    return render(request, 'tracktopics/results.html', {'topic': topic, 'matchingtweets': matchingtweets})
        
   
def addtrackingfields(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddFieldsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            trackingtopicobject = TrackingTopic.objects.create(topic_text=form.cleaned_data['topic'])
            trackingtopicobject.wordtotrack_set.create(word_text=form.cleaned_data['word'])
            trackingtopicobject.usertotrack_set.create(user_text=form.cleaned_data['user'])
            return HttpResponseRedirect('/tracktopics/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddFieldsForm()
    return render(request, 'tracktopics/addtrackingfields.html', {'form': form})