from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager): # Custom manager to handle my custom user model
    def create_user(self, email, first_name, last_name, phone, password): # The fields that 'can' be included
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')
        user = self.model( # The user model - what a user "is"
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.set_password(password) # Hashes the password
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, phone, password):
        user = self.create_user(email, first_name, last_name, phone, password) # Calls the function above
        user.is_admin = True
        user.save(using=self._db)
        return user

# Replaces the built-in User model. It becomes the "User" model for my projects.

class CustomUser(AbstractBaseUser): # My own user model
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager() # Replacing the default user manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    
    # AUTH_USER_MODEL = something | replaces Djangos built in model with my own

    # USERNAME_FIELD and REQUIRED_FIELDS: These are class attributes in the CustomUser model that Django's authentication framework uses to know certain things about your user model. USERNAME_FIELD tells Django which field is used as the "username". In this case, it's the email field, meaning users will authenticate with their email address. REQUIRED_FIELDS is a list of the names of the model fields that will be prompted for when creating a user via the createsuperuser management command.

    # From get_user_model() import