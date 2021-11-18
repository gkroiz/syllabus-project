from django import forms
from .models import DeptInfo


class DeptInfo(forms.ModelForm):
    dept_info = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = DeptInfo
        fields = {'dept_info'}

    # This gets rid of the label
    def __init__(self, *args, **kwargs):
        super(DeptInfo, self).__init__(*args, **kwargs)
        self.fields['dept_info'].label = ""
