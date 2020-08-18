from django.forms import ModelForm
from cowsay.models import CowSay


class CowSayForm(ModelForm):
    class Meta:
        model = CowSay
        fields = ['text']
        exclude = ['date']

