from django import forms
from django.utils.translation import gettext as _
from app.models import User
from app.models import PersonalDetails , BankDetails , AddressDetails, LoanApplication

class PersonalDetailForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': _('Nidheer'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'first-name',
            'required': 'true',
            'type': 'text',
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': _('Chaudhary'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )
    pan_number = forms.CharField(
        label='PAN Number',
        widget=forms.TextInput(attrs={
            'placeholder': _('ABCDE1234F'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'pan_number',
            'required': 'true',
            'type': 'text',
        })
    )
    pin_code = forms.IntegerField(
        label='PIN Code',
        widget=forms.TextInput(attrs={
            'placeholder': _('123435'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'pin_code',
            'required': 'true',
            'type': 'text',
        })
    )
    state = forms.CharField(
        label='State',
        widget=forms.TextInput(attrs={
           'placeholder': _('Uttar Pradesh'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'state',
            'required': 'true',
            'type': 'text',
        })
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={
            'placeholder': _('Agra'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'city',
            'required': 'true',
            'type': 'text',
        })
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={
            'placeholder': _('Sec-102, Agra'),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'address',
            'required': 'true',
            'type': 'text',

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
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'last_name',
            'required': 'true',
            'type': 'text',
        })
    )


    account_holder_name = forms.CharField(
        label=_('Account Holder Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'account_holder_name',
            'required': 'true',
            'type': 'text',
        })
    )

    ifsc_code = forms.CharField(
        label=_('IFSC Code'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'ifsc_code',
            'required': 'true',
            'type': 'text',
        })
    )

    branch = forms.CharField(
        label=_('Branch Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'branch',
            'required': 'true',
            'type': 'text',
        })
    )

    check_image = forms.ImageField(
        label=_('Picture Of Check'),
        widget=forms.FileInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'permanent_address_proof',
        })
    )

    class Meta:
        model = BankDetails
        fields = ['account_number', 'account_holder_name','ifsc_code', 'branch', 'check_image']

class AddressDetailForm(forms.ModelForm):
    current_address = forms.CharField(
        label=_('Current Address'),
        widget=forms.TextInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'current_address',
            'required': 'true',
            'type': 'text',
        })
    )

    current_address_proof = forms.ImageField(
        label=_('Current Address Proof'),
        widget=forms.FileInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'current_address_proof',
        })
    )

    permanent_address = forms.CharField(
        label=_('Permanent Address'),
        widget=forms.TextInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'permanent_address',
            'required': 'true',
            'type': 'text',
        })
    )

    permanent_address_proof = forms.ImageField(
        label=_('Permanent Address Proof'),
        widget=forms.FileInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'permanent_address_proof',
        })
    )

    class Meta:
        model = AddressDetails  
        fields = ['current_address', 'current_address_proof', 'permanent_address', 'permanent_address_proof']


# create form for loan application taking reference from above

class LoanApplicationForm(forms.ModelForm):
    proposal_amt = forms.IntegerField(
        label=_('Loan Amount'),
        widget=forms.TextInput(attrs={
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'proposal_amt',
            'required': 'true',
            'type': 'number',
        })
    )

    # reason = forms.CharField(
    #     label=_('Loan Reason'),
    #     widget=forms.TextInput(attrs={
    #         'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
    #         'id': 'reason',
    #         'required': 'true',
    #         'type': 'text',
    #     })
    # )

    reason = forms.CharField(
        label=_('Loan Reason'),
        widget=forms.Textarea(attrs={
            'class': 'block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'id': 'reason',
            'required': 'true',
            'type': 'text',
            'rows': '3',
        })
    )

    class Meta:
        model = LoanApplication
        fields = ['proposal_amt', 'reason']