from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
import CheckTweetsForWords
from .forms import AddFieldsForm

from .models import TrackingTopic

# Index page - shows all of the topics that are being tracked and a link to create a new topic
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
        
# Used to create a new topic to track - 
# TODO: needs to either only have the topic field and a separate page to add users and words/users
# or have the ability to add multiple words/users at a time or both
# TODO: need a way to edit existing topics
def addtrackingfields(request):
    
    if request.method == 'POST':
        # Users my form in forms.py to gather the information I need into an object
        form = AddFieldsForm(request.POST)
        # If its valid add this stuff to the database
        if form.is_valid():
            trackingtopicobject = TrackingTopic.objects.create(topic_text=form.cleaned_data['topic'])
            trackingtopicobject.wordtotrack_set.create(word_text=form.cleaned_data['word'])
            trackingtopicobject.usertotrack_set.create(user_text=form.cleaned_data['user'])
            return HttpResponseRedirect('/tracktopics/')
    else:
        form = AddFieldsForm()
    return render(request, 'tracktopics/addtrackingfields.html', {'form': form})