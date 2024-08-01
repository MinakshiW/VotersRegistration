import uuid

from django.db import models
from django.core import validators

# Create your model here.
def generate_unic_Id():
    return uuid.uuid4().hex[:8].upper()

class Voters(models.Model):
    vid = models.CharField(max_length=10, primary_key=True, default = generate_unic_Id, editable = False)
    fname = models.CharField(max_length=34,
                             validators=[validators.RegexValidator('^[a-zA-Z]{2,}$',
                                                                   message='Please enter proper first name with minimum 2 characters')])
    lname = models.CharField(max_length=34,
                             validators=[validators.RegexValidator('^[a-zA-Z]{2,}$',
                                                                   message='Please enter proper last name with minimum 2 characters')])
    gender = models.CharField(max_length=23)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=23)
    state = models.CharField(max_length=23)
    pincode = models.CharField(max_length=12,
                               validators=[validators.RegexValidator('^[1-9]{1}[0-9]{2}[0-9]{3}$',
                                                                     message='Please Enter Valid 6-digit Pincode')]
                               )
    dob = models.DateField()
    contact = models.CharField(max_length=23,
                               validators=[validators.RegexValidator('^(\+\d{1,3}[- ]?)?\d{10}$',
                                                                     message='Please Enter Proper Contact Number')])