from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from users.models import User

class PersonalDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    pan_number = models.CharField(max_length=10, null=True)
    pin_code = models.IntegerField(null=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AddressDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    current_address = models.CharField(max_length=100, null=True)
    current_address_proof = models.ImageField(upload_to='address_proofs/', null=True)
    permanent_address = models.CharField(max_length=100, null=True)
    permanent_address_proof = models.ImageField(upload_to='address_proofs/', null=True)
    remark = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BankDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    account_number = models.IntegerField(null=True)
    account_holder_name = models.CharField(max_length=50, null=True)
    ifsc_code = models.CharField(max_length=11, null=True)
    branch = models.CharField(max_length=50, null=True)
    check_image = models.ImageField(upload_to='checks/', null=True)
    remark = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LoanApplication(models.Model):

    USER_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=300, null=True)
    proposal_amt = models.IntegerField(null=True)
    approved_amt = models.IntegerField(null=True)
    is_approved = models.BooleanField(default=False, null=True)
    status = models.CharField(max_length=30, null=True, choices=USER_STATUS, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
