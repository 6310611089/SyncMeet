from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_facebook_or_instagram(value):
    if not value.startswith('https://www.facebook.com/') and not value.startswith('https://www.instagram.com/'):
        raise ValidationError(
            'Invalid link. Must be a link to Facebook or Instagram.')


class UserInfo(models.Model):

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')

    account_UID = models.PositiveIntegerField(unique=True)

    profile_image = models.ImageField(upload_to='uploads/', blank=True)

    prefix_phone_number = models.CharField(max_length=3, default='+66')
    phone_number = models.CharField(max_length=15)

    sir_name = models.CharField(max_length=15)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default='other')

    age = models.PositiveIntegerField()
    contact = models.URLField(
        validators=[URLValidator(), validate_facebook_or_instagram])

    def __str__(self):
        return f'{ self.user_id.username }'


class Friend(models.Model):
    user_id = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name='user')
    friend_id = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name='friend')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.friend_id.user_id.username } is { self.user_id.user_id.username }'s friend"
