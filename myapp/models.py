from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATE_TYPES = (
	(0, 'Monday'),
	(1, 'Tuesday'),
	(2, 'Wednesday'),
	(3, 'Thursday'),
	(4, 'Friday'),
	(5, 'Saturday'),
	(6, 'Sunday'),
)

class Add_act(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="image", blank=True)
	def __unicode__(self):
		return u"%s"%(self.name)

class Poll(models.Model):
	user_id = models.ForeignKey(Add_act)
	vote = models.IntegerField(choices=STATE_TYPES, default=0, null=True)

