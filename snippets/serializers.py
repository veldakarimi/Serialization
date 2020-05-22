#declaring serializers that work very similar to Django's forms. 
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    
def create(self, validated_data):
        #Create and return a new `Snippet` instance, given the validated data.
        
       
    return Snippet.objects.create(**validated_data)
    
    
def update(self, instance, validated_data):
    """
    Update and return an existing `Snippet` instance, given the validated data.
    """
    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.linenos = validated_data.get('linenos', instance.linenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance

'''create() and update() methods define how fully fledged 
    instances are created or modified when calling serializer.save()
    A serializer class is very similar to a Django Form class,
    and includes similar validation flags on the various fields, 
    such as required, max_length and default.
    The field flags can also control how the serializer should be
     displayed in certain circumstances, such as when rendering to HTML. 
    The {'base_template': 'textarea.html'} flag above is equivalent
     to using widget=widgets.Textarea on a Django Form class.
    This is particularly useful for controlling how the browsable 
    API should be displayed.
    It's important to remember that ModelSerializer classes don't
    do anything particularly magical, they are simply a shortcut for creating serializer classes:
    An automatically determined set of fields.
    Simple default implementations for the create() and update() methods.'''
    