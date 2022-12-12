from rest_framework import serializers
from quickstart.models import Capteur


        
class CapteurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capteur
        fields = ['keyname', 'value']
        