from django import forms
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(label='이름')
    age = forms.IntegerField(label='나이')
    height = forms.IntegerField(label='키')
    weight = forms.IntegerField(label='몸무게')
    device_pw = forms.CharField(label='기기 비밀번호(숫자 4자리)')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.name = self.cleaned_data['name']
        user.profile.age = self.cleaned_data['age']
        user.profile.height = self.cleaned_data['height']
        user.profile.weight = self.cleaned_data['weight']
        user.profile.device_pw = self.cleaned_data['device_pw']
        user.save()
        return user