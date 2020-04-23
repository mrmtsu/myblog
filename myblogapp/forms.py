from django import forms

class Contact(forms.Form):
  subject = forms.CharField(label='お名前', max_length=100)
  sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しくご入力ください。')
  message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)
  myself = forms.BooleanField(label='同じ内容を受け取る', required=False)