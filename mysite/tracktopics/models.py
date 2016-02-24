from django.db import models

class TrackingTopic(models.Model):
    topic_text = models.CharField(max_length=200)
    # add representation of the class
    def __str__(self):
        return self.topic_text

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