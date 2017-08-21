from django import forms

class DataForm(forms.Form):
    name = forms.CharField(max_length=100)
    email= forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(),
        help_text="Write your message here ..."
    )
    sender = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(DataForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name or not email or not message:
            raise forms.ValidationError("All fields are required")



