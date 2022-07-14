from rest_framework import serializers
from new_app.models import ExampleModel

# Create your serializers here.
class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('firstname', 'lastname')