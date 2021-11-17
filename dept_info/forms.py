from django import forms


class DeptInfo(forms.Form):
    dept_info = forms.CharField(widget=forms.Textarea)

    # This gets rid of the label
    def __init__(self, *args, **kwargs):
        super(DeptInfo, self).__init__(*args, **kwargs)
        self.fields['dept_info'].label = ""
