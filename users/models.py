from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import jwt
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('email not found')

        user = self.model(email=self.normalize_email(email.lower()))

        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):

        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Сountries(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True,
                              unique=True,
                              db_index=True,
                              max_length=50)
    
    username = models.CharField(max_length=50,
                                blank=True,
                                null=True)
    last_name = models.CharField(max_length=40,
                                 blank=True,
                                 null=True)
    first_name = models.CharField(max_length=40,
                                  blank=True,
                                  null=True)
    prefered_pronouns = models.CharField(max_length=40,
                                         blank=True,
                                         null=True)
    birthday = models.DateField(blank=True,
                                null=True)
    location = models.ForeignKey(Сountries,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk,
        },
            settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return token
