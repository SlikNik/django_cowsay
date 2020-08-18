from django.forms import ModelForm
from cowsay.models import CowSay
from subprocess import run, PIPE


class CowSayForm(ModelForm):
    class Meta:
        model = CowSay
        fields = ['text']
        exclude = ['date']

    def get_cowsay(self, text):
        output = run(["cowsay", text],  stdout=PIPE, stderr=PIPE, universal_newlines=True)
        return output
