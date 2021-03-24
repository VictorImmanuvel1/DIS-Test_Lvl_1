from django.forms import ModelForm
from .models import User,Mark

class registerform(ModelForm):
    class Meta:
        model=User
        fields='__all__'

class markform(ModelForm):
    class Meta:
        model=Mark
        #exclude = ('mid',)
        fields = '__all__'