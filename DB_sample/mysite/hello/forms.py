from django import forms


class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    password = forms.CharField(
        label='パスワード',
        max_length=64,
        required=True,
        widget=forms.TextInput()
    )