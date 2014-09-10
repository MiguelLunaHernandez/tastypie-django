from tastypie.utils.timezone import now
from django.contrib.auth,models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Entry(models.Model):
	user		= models.ForeingKey(User)
	pub_date	= models.DateTimeField(default=now)
	title		= models.charFild(max_length=200)
	slug		= models.slugField()
	body		= models.TextField()
	
	def __unicode__(self):
		return self.title

	def __unicode__(self):
		if not self.slug:
			self.slug = slugify(self.title)[:50]
		
		return super(Entre, self).save(*args, **kwargs)


