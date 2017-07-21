from django import forms


# class UserForm(forms.Form):
#     username = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '用户名',
#             }
#         )
#     )
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': '口令',
#             }
#         )
#     )
#
#     def clean(self):
#         if not self.is_valid():
#             raise forms.ValidationError(u"用户名和密码为必填项!")
#         else:
#             cleaned_data = super(UserForm, self).clean()


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class LocForm(forms.Form):
    id = forms.IntegerField(label='地址编号', required=True)
    name = forms.CharField(label='对应地址', required=True, max_length=50)
