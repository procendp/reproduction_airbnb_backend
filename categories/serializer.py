from rest_framework import serializers
from .models import Category

# translate django to JSON for the browser

class CategorySerializer(serializers.Serializer):
    
    # explaining something what Category have to serialzer
    # from djnango DB model to JSON data
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    kind = serializers.ChoiceField(choices=Category.CategoryKindChoices.choices)
    created_at = serializers.DateTimeField(read_only=True)      # read_only=True : serializer에게 user가 error 없이 보낼 수 있게 해줌.. is_valid에서 안 걸림

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):   
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()

        return instance
