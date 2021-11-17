from django import forms


class DeptInfo(forms.Form):
    dept_info = forms.CharField(label='Enter department information', widget=forms.Textarea)
