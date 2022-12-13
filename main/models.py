from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    """User Profile manages basic user information
    """
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile'
    )
    dob = models.DateField(
        "date of birth",
        blank=True,
        null=True,
        help_text="Get offers on your birthday"
    )

    class Meta:
        verbose_name_plural = "UserProfiles"
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username
