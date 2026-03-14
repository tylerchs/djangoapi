#api/resources.py

from tastypie.resources import ModelResource
from api.models import Note

class NoteResource(ModelResource):
    queryset = Note.objects.all() # what models the resource is concerned with
    resource_name = 'note'