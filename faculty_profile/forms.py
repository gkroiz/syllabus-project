from django import forms
from faculty_profile.models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    faculty_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Faculty ID (front of your UMBC email)', 'style': 'width: 350px;', 'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 350px;', 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 350px;', 'class': 'form-control'}))
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        # check if extra_fields exist. If they don't exist assign 0 to them
        if not extra_fields:
            extra_fields = 0

        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['office_hour_field_{index}'.format(index=index + 1)] = forms.CharField(max_length=100)

    def get_fields(self):
        return self.fields
