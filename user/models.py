from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser



# Create your models here.
class CustomUserManager(BaseUserManager):

    """
        description - our manager for the user model
    """

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    

class User(AbstractUser):
    """
        description - extends the abstract user by adding username, email and date_of_birth
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)


    objects = CustomUserManager()        # set our model manager for the user
    USERNAME_FIELD = 'email'             # let user use email instead of username
    REQUIRED_FIELDS = ['username']       # set username to be required

    def __str__(self) -> str:
        return self.email
