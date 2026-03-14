from django.db import models

# Create your models here.

# Note model 
# define fields along with type of each
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # __str__ method to define what we get when we ask for a particular instance of a model
    # This is for when we grab any Note model, we'll only the title and body
    def __str__(self):
        return '%s %s' % (self.title, self.body)

