from django.db import models
from django.core.validators import RegexValidator

CHAR_LIMIT = 255
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class TeamMember(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=CHAR_LIMIT, blank=False)
    last_name = models.CharField(max_length=CHAR_LIMIT, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    email = models.EmailField(max_length=CHAR_LIMIT, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    role = models.CharField(max_length=1, blank=False)
    
    def __str__(self):
        return self.email


