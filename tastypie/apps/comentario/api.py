from tastypie.resources import ModelResource
from cometario.models import Entry

class EntryResource(ModelResource):
	class Meta:
		queryset = Entry.objects.all()
		resource_name = 'entry'

