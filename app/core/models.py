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


class IndiaCovid19Update(models.Model):
    """Store the covid19 Update of India"""
    title = models.CharField(max_length=1000)
    date = models.DateField()
    href = models.CharField(max_length=2000)

    class Meta:
        ordering = ['-date']


class IndiaFullCovidStats(models.Model):
    """Store the covid19 stats of India"""
    state = models.CharField(max_length=30)
    total_case = models.IntegerField()
    total_death = models.IntegerField()
    total_recovered = models.IntegerField()

    class Meta:
        ordering = ['-total_case']
        verbose_name_plural = "India Statewise Covid19 stats"

    def __str__(self): return f'{self.state} - {self.total_case}'


class BaseCountryStats(models.Model):
    """Base Template for Countries Stats"""
    date = models.DateField()
    confirmed = models.IntegerField()
    recovered = models.IntegerField()
    deaths = models.IntegerField()


class ChinaCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('China', self.date)


class UsCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('US', self.date)


class GermanyCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Germany', self.date)


class ItalyCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Italy', self.date)


class TurkeyCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Turkey', self.date)


class RussiaCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Russia', self.date)


class UKCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('UK', self.date)


class UkraineCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Ukraine', self.date)


class IranCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Iran', self.date)


class FranceCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('France', self.date)


class SpainCovidStats(BaseCountryStats):
    """Store covid19 Stats from april"""

    def __str__(self):
        return '{} - {}'.format('Spain', self.date)


class IndiaCovidStats(BaseCountryStats):
    """Store India Covid Data Date wise"""

    def __str__(self):
        return '{} - {}'.format('India', self.date)


class WorldMapCovidStats(BaseCountryStats):
    """Store India Covid Data Date wise"""
    lat = models.FloatField()
    lon = models.FloatField()
    province = models.CharField(max_length=100, default='None')
    country = models.CharField(max_length=100, default='None')

    def __str__(self):
        return '{} - {}'.format('India', self.date)
