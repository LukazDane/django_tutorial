from django.db import models

# Create your models here.
# events\events\models.py


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    guests = models.ForeignKey('Guest', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s Date: %s, Venue: %s, Managed By: %s, Description: %s, Guestlist: %s" % (self.name, self.event_date, self.venue, self.manager, self.description, self.guests)


class Guest(models.Model):
    name = models.CharField('Contact Name', max_length=120)
    events = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.events, self.name)
