from django import forms
from django.core import validators

### Creating Validator (Global)
def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("Name needs to start with 'Z'")
    



class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
                                required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)],
                                )


    ## Manually creating local VALIDATOR for single field:
    ## def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOT BOT!!!!")
    #     return botcatcher

    ## Manually creating local VALIDATOR for MULTIPLE FIELDS:
    def  clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        Vmail = all_clean_data['verify_email']
        
        if Vmail != email:
            raise forms.ValidationError("Email does not match.")
        

