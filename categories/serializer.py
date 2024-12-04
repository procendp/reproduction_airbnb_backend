from rest_framework import serializers

# translate django to JSON for the browser

class CategorySerializer(serializers.Serializer):
    
    # explaining something what Category have to serialzer
    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)      # read_only=True : serializer에게 user가 error 없이 보낼 수 있게 해줌.. is_valid에서 안 걸림
