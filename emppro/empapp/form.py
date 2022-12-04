from django import forms


class EmpForm(forms.Form):
    name = forms.CharField(
        label = "Enter Your Name:",
        widget = forms.TextInput(
        attrs = {
             'placeholder':"Your Name",
             'class':'form.control'
         }
        )
    )
    salary = forms.IntegerField(
        label = "Enter Your Salary",
        widget = forms.NumberInput(
            attrs={
                'placeholder':'Your Salary',
                'class':'form.control'
            }
        )
    )
    company = forms.CharField(
        label =" Enter Your Company ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Company ',
                'class': 'form.control'
            }
        )
    )
