from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# User Manager 
class UserManager(BaseUserManager):
    def create_user(self, email, password, username=None):
        if not email:
            raise ValueError('Your Official Email is Required')
        if not password:
            raise ValueError('Unique and Uncommon Password is Required')
        
        
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password, username=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
# Custom User

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
