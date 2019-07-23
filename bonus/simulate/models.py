from django.db import models

# Create your models here.
class Resource(models.Model):
    resource = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.resource


class Method(models.Model):
    resource_fk = models.ForeignKey(Resource, on_delete=models.CASCADE)
    method = models.CharField(max_length=10)
    def descrip(self):
        output = {
            'list' : 'Retrieves (GET) a list of zero or more resource.',
            'insert' : 'Creates (POST) a new resource.',
            'update' : 'Modifies (PUT) an existing resource to reflect data in your request',
            'delete' : 'Remove (DELETE) a specific resource'
        }
        return output[self.method]

    def __str__(self):
        return self.method

