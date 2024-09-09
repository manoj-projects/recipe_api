from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        transformed_data = self.transform_data(representation)
        return transformed_data

    def transform_field_name(self, field_name):
        parts = field_name.split('_')
        return ''.join(part.capitalize() for part in parts)
    
    def transform_data(self, data):
        """Apply transformation to all field names in the serialized data."""
        transformed_data = {}
        for key, value in data.items():
            new_key = self.transform_field_name(key)
            transformed_data[new_key] = value
        return transformed_data

def transform_field_name(field_name):
    """Transform snake_case to CamelCase."""
    parts = field_name.split('_')
    return ''.join(part.capitalize() for part in parts)

def custom_serializer(data):
    transformed_data = []
    res={}
    for item in data:
      transformed_item = {transform_field_name(k): v for k, v in item.items()}
      transformed_data.append(transformed_item)
    
    return transformed_data
