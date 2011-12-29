from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=45)
    year = models.IntegerField()
    grapes = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    region = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="images")
    
    def __unicode__(self):
        return self.name
        
    def fields(self):
        # Get Model's fields
        return [ f.name for f in self._meta.fields 
                       if f.name not in ['mymodel_ptr'] ]

    def values(self):
        # Get values of the Resource
        def attr( f ):
            return str( getattr(self, f) )
        return dict([ (f, attr(f)) for f in self.fields() ])