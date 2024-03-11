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

    remark = forms.CharField(
        label = "Remark",
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'personalRemark',
            'required': 'true',
            'type': 'text',

        })
    )


    class Meta:
        model = PersonalDetails
        fields = ['first_name', 'last_name', 'pan_number', 'pin_code', 'state', 'city', 'address', 'remark']

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

    # check_image = forms.ImageField(
    #     label=_('Picture Of Check'),
    #     widget=forms.FileInput(attrs={
    #         'class': 'p-2 border border-gray-300 rounded-md',
    #         'id': 'permanent_address_proof',
    #     })
    # )

    remark = forms.CharField(
        label = "Remark",
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'bankRemark',
            'required': 'true',
            'type': 'text',

        })
    )

    class Meta:
        model = BankDetails
        fields = ['account_number', 'account_holder_name','ifsc_code', 'branch','remark']

class AddressDetailForm(forms.ModelForm):
    current_address = forms.CharField(
        label=_('Current Address'),
        widget=forms.TextInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'current_address',
            'required': 'false',
            'type': 'text',
        })
    )



    permanent_address = forms.CharField(
        label=_('Permanent Address'),
        widget=forms.TextInput(attrs={
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'permanent_address',
            'required': 'false',
            'type': 'text',
        })
    )



    remark = forms.CharField(
        label = "Remark",
        widget=forms.TextInput(attrs={
            'placeholder': _(''),
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'addressRemark',
            'required': 'false',
            'type': 'text',

        })
    )
    class Meta:
        model = AddressDetails 
        fields = ['current_address', 'permanent_address', 'remark']



class LoanApplicationForm(forms.ModelForm):
    # status = forms.ChoiceField(
    #     label='Status',
    #     choices=LoanApplication.USER_STATUS,
    #     widget=forms.Select(attrs={
    #         'class': 'p-2 border border-gray-300 rounded-md',
    #         'id': 'status',
    #         'required': True,
    #     })
    # )
    forms.CharField(
        label='Reason',
        widget=forms.TextInput(attrs={
            'placeholder': 'Reason',
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'reason',
            'required': False, 
            
            'type': 'text',
        })
    )
    proposal_amt = forms.IntegerField(
        label='Approved Amount',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter approved loan amount',
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'approved_amt',
            'required': False, 
            'type': 'number',
        })
    )
    approved_amt = forms.IntegerField(
        label='Approved Amount',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter approved loan amount',
            'class': 'p-2 border border-gray-300 rounded-md',
            'id': 'approved_amt',
            'required': True, 
            'type': 'number',
        })
    )

    class Meta:
        model = LoanApplication
        fields = ['reason', 'proposal_amt']
