from django import forms

class MessageForm(forms.Form):
    people = forms.IntegerField(
        label='人数',
        required=True,
        initial=1,
        widget=forms.NumberInput(),
    )
    solt_butter = forms.IntegerField(
        label='塩',
        required=True,
        initial=0,
        widget=forms.NumberInput(),
    )
    curry = forms.IntegerField(
        label='カレー',
        required=True,
        initial=0,
        widget=forms.NumberInput(),
    )
    caramel = forms.IntegerField(
        label='キャラメル',
        required=True,
        initial=0,
        widget=forms.NumberInput(),
    )
    chocolate = forms.IntegerField(
        label='チョコレート',
        required=True,
        initial=0,
        widget=forms.NumberInput(),
    )
    enter = forms.CharField(
        label='その他',
        required=False,
        widget=forms.Textarea(),
    )
