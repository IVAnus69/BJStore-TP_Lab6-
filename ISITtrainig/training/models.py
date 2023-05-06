from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('Название', max_length=50)
    addr = models.CharField('Адрес', max_length=50)

    def __str__(self):
        return self.name


class Training(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('Название', max_length=50)
    direction = models.CharField('Направление', max_length=50)
    date = models.DateField('Дата')
    exp = models.BooleanField('Опыт')
    educ = models.BooleanField('Образование')
    idFKCompany = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField('Изображение профиля', upload_to='images/')
    proftocomp = models.ManyToManyField(Company, through="ProfileToCompanies")


class ProfileToCompanies(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
