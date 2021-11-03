from django.forms import ModelForm
from .models import Project

class ProjectForm (ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'description', 'demo_link', 'source_link',
        'tags', 'featured_image' ,'featured_image']