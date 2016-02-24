from django.db import models

# This stuff is cool and weird with the migrations and stuff
# When I "migrate" it creates the appropriate tables in my db
# But they also become strange classes. When I call TrackingObject.object is it accessing the database then or 
# is this TrackingObject loaded in the app? How do I ensure my changes persist in the db? Right now everything is,
# TODO: look up save(), when the app accessing is the db

class TrackingTopic(models.Model):
    topic_text = models.CharField(max_length=200)
    # add representation of the class
    def __str__(self):
        return self.topic_text

# Can I access these directly, ie: WordToTrack.object.all() doesnt seem to work
class WordToTrack(models.Model):
    topic = models.ForeignKey(TrackingTopic, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    # add representation of the class
    def __str__(self):
        return self.word_text


class UserToTrack(models.Model):
    topic = models.ForeignKey(TrackingTopic, on_delete=models.CASCADE)
    user_text = models.CharField(max_length=200)
    # add representation of the class
    def __str__(self):
        return self.user_text