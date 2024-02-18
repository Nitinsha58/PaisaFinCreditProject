from django import forms
from django.utils.translation import gettext as _
from .models import User
from .models import PersonalDetails , BankDetails , AddressDetails

class UserForm(forms.ModelForm):

    phone = forms.RegexField(
        regex=r'\d{9,15}$',
        help_text=_('Enter 10 digit phone number'),
        error_messages={'invalid': _('Invalid phone number')},
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'phone',
            'required': 'true',
            'type': 'tel',
        })
    )

    password1 = forms.RegexField(
        label=_('Password'),
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+]{8,}$',
        help_text=_('Minimum 8 characters with at least 1 letter and 1 number and one special character from !@#$%^&*()_+'),
        error_messages={'required': _('Password is required'), 'invalid': _('Invalid password')},
        widget=forms.PasswordInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'password',
            'required': 'true',
            'type': 'password',
        })
    )

    terms_accepted = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'peer h-4 w-4 rounded border-2 translate-y-1 mr-1 border-gray-300 accent-blue-500 focus:ring-2 focus:ring-blue-500',
            'id': 'terms',
            'type': 'checkbox',
            'checked': True,
        }),
        required=False,
    )
    #  w-4 h-4  rounded-md accent-blue-500 focus:ring-2 focus:ring-blue-500
    # <input type="checkbox" id="terms" name="terms" checked class="">

    def clean_terms_accepted(self):
        terms_accepted = self.cleaned_data.get('terms_accepted')
        if not terms_accepted:
            raise forms.ValidationError(_('You must accept the terms and conditions.'))
        return True  # Set it to True if checkbox is checked

    def clean(self):
        cleaned_data = super().clean()
        # Add additional form-wide validation here if needed
        return cleaned_data

    class Meta:
        model = User
        fields = ['phone', 'password1',  'terms_accepted']

class PersonalDetailForm(forms.ModelForm):

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'first_name',
            'required': 'true',
            'type': 'text',
        })
    )

    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )
    class Meta:
        model = PersonalDetails
        fields = ['first_name', 'last_name']


class PersonalDetailComForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'first_name',
            'required': 'true',
            'type': 'text',
            
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )
    pan_number = forms.CharField(
        label='PAN Number',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'pan_number',
            'required': 'true',
            'type': 'text',
        })
    )
    pin_code = forms.IntegerField(
        label='PIN Code',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'pin_code',
            'required': 'true',
            'type': 'text',
        })
    )
    state = forms.CharField(
        label='State',
        widget=forms.TextInput(attrs={
           'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'state',
            'required': 'true',
            'type': 'text',
        })
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'city',
            'required': 'true',
            'type': 'text',
        })
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'address',
            'required': 'true',
            'type': 'text',

        })
    )
    remark = forms.CharField(
        label='Remark',
        required=False, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter any remarks',
            'class': 'form-control',
        })
    )

    class Meta:
        model = PersonalDetails
        fields = ['first_name', 'last_name', 'pan_number', 'pin_code', 'state', 'city', 'address']

class BankDetailForm(forms.ModelForm):


    account_number = forms.CharField(
        label=_('Account Number'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )


    account_holder_name = forms.CharField(
        label=_('Account Holder Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )

    ifsc_code = forms.CharField(
        label=_('IFSC Code'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )

    branch = forms.CharField(
        label=_('Branch Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )


    check_pic = forms.CharField(
        label=_('Picture Of Check'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'file',
        })
    )

    class Meta:
        model = BankDetails
        fields = ['account_number', 'account_holder_name','ifsc_code', 'check_pic']

class AddressDetailForm(forms.ModelForm):
    current_address = forms.CharField(
        label=_('Current Address'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )


    current_address_Proof = forms.CharField(
        label=_('Current Address Proof'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'file',
        })
    )


    permanent_address = forms.CharField(
        label=_('Permanent Address'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )


    permanent_address_Proof = forms.CharField(
        label=_('Permanent Address Proof'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'last_name',
            'required': 'true',
            'type': 'file',
        })
    )

    class Meta:
        model = AddressDetails  
        fields = ['current_address', 'current_address_Proof', 'permanent_address', 'permanent_address_Proof']



    