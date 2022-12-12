from django.db import models

class Capteur(models.Model):
      temperature = models.fields.CharField(max_length=10 , null=True)
      humidite = models.fields.CharField(max_length=10, null=True)
      pression = models.fields.CharField(max_length=10, null=True)
      
      def _str_(self):
        return f'{self.name}' 
