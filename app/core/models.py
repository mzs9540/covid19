from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=20, default='India')
    phone = models.CharField(max_length=20, default='+91')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class CovidNews(models.Model):
    """Store the news of crawler based on covid 19"""

    title = models.CharField(max_length=5000)
    href = models.CharField(max_length=5000)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = 'Covid News'
        ordering = ['-date']

    def __str__(self):
        return self.title


class WorldCovidStats(models.Model):
    """Store the covid19 stats of whole world"""
    country = models.CharField(max_length=30)
    total_case = models.FloatField()
    new_case = models.FloatField()
    total_recovered = models.FloatField()
    active_case = models.FloatField()
    cases_per_million = models.FloatField()
    deaths_per_million = models.FloatField()
    total_death = models.FloatField()
    new_death = models.FloatField()
    # serious_critical = models.CharField(max_length=20)
    # total_test = models.CharField(max_length=20)
    # test_per_million = models.CharField(max_length=20)

    class Meta:
        ordering = ['-total_case']

    def __str__(self): return self.country


class IndiaCovidStats(models.Model):
    """Store the covid19 stats of India"""
    city = models.CharField(max_length=30)
    total_case = models.CharField(max_length=20)
    new_case = models.CharField(max_length=20)
    total_death = models.CharField(max_length=20)
    new_death = models.CharField(max_length=20)
    total_recovered = models.CharField(max_length=20)
    active_case = models.CharField(max_length=20)
    serious_critical = models.CharField(max_length=20)
    cases_per_million = models.CharField(max_length=20)
    deaths_per_million = models.CharField(max_length=20)
    total_test = models.CharField(max_length=20)
    test_per_million = models.CharField(max_length=20)

    def __str__(self): return self.city
