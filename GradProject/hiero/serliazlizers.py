from rest_framework import serializers

from .models import Image
from GradProject.fields import Base64FileField

class ImageSerializer(serializers.ModelSerializer):
    # image=Base64FileField(max_length=None,use_url=True,required=False)
    class Meta:
        model = Image
        fields = '__all__'