from django import forms
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(label='이름')
    age = forms.IntegerField(label='나이')
    height = forms.IntegerField(label='키')
    weight = forms.IntegerField(label='몸무게')


    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.name = self.cleaned_data['name']
        user.profile.age = self.cleaned_data['age']
        user.profile.height = self.cleaned_data['height']
        user.profile.weight = self.cleaned_data['weight']
        user.save()
        return user