from django import forms
# from vege.models import Receipe
from djangoapp.models import Data

# class makeform(forms.ModelForm):
#     class Meta:
#         model = Receipe
#         fields = ('receipe_name','receipe_description')
class makeform(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('name','email','msg')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'msg':forms.TextInput(attrs={'class':'form-control'}),
           
            
            
            # 'image':forms.ImageField()
        }


        